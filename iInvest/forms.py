from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, validators, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
	openid=TextField('openid',validators=[Required()])
	remember_me=BooleanField('remember_me',default=False)

class RegistrationForm(Form):
	username =TextField('username',[validators.Length(min=4,max=25)])
	email=TextField('Exmail Address',[validators.Length(min=6,max=35)])
	password=PasswordField('New password', [validators.Required(),validators.EqualTo('confirm',message='Passwords must match')])

	confirm=PasswordField('Repeat Password')
	accept_tos=BooleanField('I accept the TOS',[validators.Required()])