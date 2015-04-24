from iInvest import db,app
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
import flask_login as login
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User,AssetManagement,AssetManagementPreorder
#from forms import AssetManagementForm

from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
from forms import LoginForm, RegistrationForm

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'
 #   return render_template('index.html')

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

# Create customized model view class
class UserManageView(sqla.ModelView):
    can_create = False
    
    def is_accessible(self):
        return login.current_user.is_authenticated()
  

class AssetManageView(sqla.ModelView):

    column_list = ('name','reason','threshold')
    column_sortable_list = ('name','reason')

    form_args = dict(
                    reason=dict(validators=[validators.required()])
                )


    def create_form(self):
        form = super(AssetManageView,self).create_form()
        return form

    def is_accessible(self):
        return login.current_user.is_authenticated()	
    column_display_pk = True


class PreorderManageView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()
	column_display_pk = True
	column_sortable_list=(('asset_management',AssetManagement.name),'phone',('user',User.name))
    #need test
	form_ajax_refs = {
        'asset_management': {
            'fields': (AssetManagement.name,)
        },
        'user': {
            'fields': (User.name,)
        }
    }



# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'iInvest:', index_view=MyAdminIndexView(), base_template='my_master.html')

# Add view
admin.add_view(UserManageView(User, db.session))
admin.add_view(AssetManageView(AssetManagement, db.session))
admin.add_view(PreorderManageView(AssetManagementPreorder, db.session))


