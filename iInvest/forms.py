from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, BooleanField, FloatField, StringField, TextAreaField, validators, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
	openid=TextField('openid',validators=[Required()])
	remember_me=BooleanField('remember_me',default=False)

class RegistrationForm(Form):
	phone =TextField('phone',[validators.Length(min=4,max=25)])
	password=PasswordField('New password', [validators.Required(),validators.EqualTo('confirm',message='Passwords must match')])

	confirm=PasswordField('Repeat Password')
	accept_tos=BooleanField('I accept the rules',[validators.Required()])

class TrustProductForm(Form):
	name =StringField('product name',[validators.Length(min=1,max=20),validators.Required()])
	reason =StringField('reason',[validators.Length(min=1,max=20),validators.Required()])
	threshold =IntegerField('threshold',[validators.NumberRange(min=1,max=50000000),validators.Required()])
	dueTime =IntegerField('dueTime',[validators.NumberRange(min=1,max=100),validators.Required()])
	shortDesc =StringField('shortDesc',[validators.Length(min=1,max=40),validators.Required()])
	profitRate =FloatField('profitRate',[validators.NumberRange(min=0.01,max=5),validators.Required()])
	profitType =StringField('profitType',[validators.Length(min=1,max=40),validators.Required()])
	profitDesc =StringField('profitDesc',[validators.Length(min=1,max=40),validators.Required()])
	profitClose =StringField('profitClose',[validators.Length(min=1,max=40),validators.Required()])
	status =IntegerField('status',[validators.NumberRange(min=1,max=5),validators.Required()])
	organization =StringField('organization',[validators.Length(min=1,max=40),validators.Required()])
	investType =StringField('investType',[validators.Length(min=1,max=40),validators.Required()])
	investArea =StringField('investArea',[validators.Length(min=1,max=40),validators.Required()])
	total =IntegerField('total',[validators.NumberRange(min=1,max=50000000),validators.Required()])
	detailDesc =TextAreaField('detailDesc',[validators.Length(min=1,max=250),validators.Required()])
	riskControl =TextAreaField('riskControl',[validators.Length(min=1,max=250),validators.Required()])


class AssetManagementForm(Form):
	name =StringField('product name',[validators.Length(min=1,max=20),validators.Required()])
	reason =StringField('reason',[validators.Length(min=1,max=20),validators.Required()])
	threshold =IntegerField('threshold',[validators.NumberRange(min=1,max=50000000),validators.Required()])
	dueTime =IntegerField('dueTime',[validators.NumberRange(min=1,max=100),validators.Required()])
	shortDesc =StringField('shortDesc',[validators.Length(min=1,max=40),validators.Required()])
	profitRate =FloatField('profitRate',[validators.NumberRange(min=0.01,max=5),validators.Required()])
	profitType =StringField('profitType',[validators.Length(min=1,max=40),validators.Required()])
	profitDesc =StringField('profitDesc',[validators.Length(min=1,max=40),validators.Required()])
	profitClose =StringField('profitClose',[validators.Length(min=1,max=40),validators.Required()])
	status =IntegerField('status',[validators.NumberRange(min=1,max=5),validators.Required()])
	organization =StringField('organization',[validators.Length(min=1,max=40),validators.Required()])
	investType =StringField('investType',[validators.Length(min=1,max=40),validators.Required()])
	investArea =StringField('investArea',[validators.Length(min=1,max=40),validators.Required()])
	total =IntegerField('total',[validators.NumberRange(min=1,max=50000000),validators.Required()])
	detailDesc =TextAreaField('detailDesc',[validators.Length(min=1,max=250),validators.Required()])
	riskControl =TextAreaField('riskControl',[validators.Length(min=1,max=250),validators.Required()])
