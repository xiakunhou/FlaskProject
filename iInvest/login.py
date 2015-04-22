from iInvest import db,app
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
import flask_login as login
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from models import User,AssetManagement,AssetManagementPreorder
#from forms import AssetManagementForm

from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters



# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    name = fields.TextField(validators=[validators.required()])
    passwd = fields.PasswordField(validators=[validators.required()])

    def validate_name(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.passwd, self.passwd.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()


class RegistrationForm(form.Form):
    name = fields.TextField(validators=[validators.required()])
    phone = fields.TextField()
    email = fields.TextField()
    idNumber = fields.TextField()
    gender = fields.TextField()
    level = fields.TextField()
    birthday = fields.TextField()
    passwd = fields.PasswordField(validators=[validators.required()])

    def validate_name(self, field):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            

            #form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            passwd = generate_password_hash(form.passwd.data)
            user = User(phone=form.phone.data,passwd=passwd,name=form.name.data)
            

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
	return '<a href="/admin/">Click me to get to Admin!</a>'
 #   return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'iInvest:', index_view=MyAdminIndexView(), base_template='my_master.html')

# Add view
admin.add_view(MyModelView(User, db.session))


# Customized User model admin
class UserAdmin(sqla.ModelView):
	#column_display_pk = True

    def is_accessible(self):
        return login.current_user.is_authenticated()
    column_display_pk = True
    
	#form_args = dict(
	#		uname = dict(label='name',validators=[validators.required()]),
	#		phones = dict(label='phone',validators=[validators.required()])

	#	)
    

class AssetAdmin(sqla.ModelView):

    column_list = ('name','reason','threshold')
    column_sortable_list = ('name','reason')

    form_args = dict(
                    reason=dict(validators=[validators.required()])
                )
    def create_form(self):
        form = super(AssetAdmin,self).create_form()
        return form

    def is_accessible(self):
        return login.current_user.is_authenticated()
	
    column_display_pk = True


	

    

class AssetView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()
	column_list = ('name','reason','threshold')
	column_sortable_list = ('name')



	#form = AssetManagementForm
    

	def create_form(self):
		form = super(AssetView,self).create_form()
		return form


class PreorderAdmin(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()
	column_display_pk = True
	#column_list = (AssetManagement.name,'phone',User.name)
	column_sortable_list=(('asset_management',AssetManagement.name),'phone',('user',User.name))
	#column_searchable_list = ('name')
	#column_filters = ('')
	form_ajax_refs = {
        'asset_management': {
            'fields': (AssetManagement.name,)
        },
        'user': {
            'fields': (User.name,)
        }
    }

    


# Add views
#admin.add_view(UserAdmin(User, db.session))
admin.add_view(AssetAdmin(AssetManagement, db.session))
admin.add_view(PreorderAdmin(AssetManagementPreorder, db.session))


