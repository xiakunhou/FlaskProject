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

class ProductForm(Form):
	name =TextField('product name',[validators.Length(min=4,max=40),validators.Required()])
	threshold =TextField('threshold',[validators.Length(min=4,max=40)])
	dueTime =TextField('dueTime',[validators.Length(min=4,max=40)])
	shortDesc =TextField('shortDesc',[validators.Length(min=4,max=40)])
	profitRate =TextField('profitRate',[validators.Length(min=4,max=40)])
	profitType =TextField('profitType',[validators.Length(min=4,max=40)])
	profitDesc =TextField('profitDesc',[validators.Length(min=4,max=40)])
	status =TextField('status',[validators.Length(min=4,max=40)])
	organization =TextField('organization',[validators.Length(min=4,max=40)])
	investType =TextField('investType',[validators.Length(min=4,max=40)])
	investArea =TextField('investArea',[validators.Length(min=4,max=40)])
	total =TextField('total',[validators.Length(min=4,max=40)])
	detailDesc =TextField('detailDesc',[validators.Length(min=4,max=40)])
	riskControl =TextField('riskControl',[validators.Length(min=4,max=40)])

class TrustProductForm(Form):
	name =TextField('product name',[validators.Length(min=4,max=20),validators.Required()])
	threshold =TextField('threshold',[validators.Length(min=4,max=40),validators.Required()])
	dueTime =TextField('dueTime',[validators.Length(min=4,max=40),validators.Required()])
	shortDesc =TextField('shortDesc',[validators.Length(min=4,max=40),validators.Required()])
	profitRate =TextField('profitRate',[validators.Length(min=4,max=40),validators.Required()])
	profitType =TextField('profitType',[validators.Length(min=4,max=40),validators.Required()])
	profitDesc =TextField('profitDesc',[validators.Length(min=4,max=40),validators.Required()])
	status =TextField('status',[validators.Length(min=4,max=40),validators.Required()])
	organization =TextField('organization',[validators.Length(min=4,max=40),validators.Required()])
	investType =TextField('investType',[validators.Length(min=4,max=40),validators.Required()])
	investArea =TextField('investArea',[validators.Length(min=4,max=40),validators.Required()])
	total =TextField('total',[validators.Length(min=4,max=40),validators.Required()])
	detailDesc =TextField('detailDesc',[validators.Length(min=4,max=250),validators.Required()])
	riskControl =TextField('riskControl',[validators.Length(min=4,max=250),validators.Required()])
