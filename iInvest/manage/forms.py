from iInvest import db
from iInvest.models import User
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash

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
