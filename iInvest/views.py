#coding:utf-8
from iInvest import app, db
from flask import render_template,flash,redirect, request, abort, url_for, session
from forms import LoginForm, RegistrationForm, ProductForm
from models import Product
import json
import flask
    	
@app.route('/')
def home():
	resp=flask.Response('foo bar baz')
	resp.headers['Access-Control-Allow-Origin']='*'
	return resp

@app.route('/index')
def index():
	user={'nickname':'MM'}
	posts=[
	{'author':{'nickname':'John'},
	 'body':'Beautiful day in Portland!'
	},
	{'author':{'nickname':'Susan'},
	 'body':'The Avengers movie was so cool!'
	}
	]
	return render_template('index.html',user=user,title='Home',posts=posts)

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
#         return redirect('/index')
# 	return render_template('login.html',title = 'Sign In',form = form)

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    password=request.form['password']
    if name=='admin' and password=='admin':
    	flash('you are logged in!')
    	session['admin_logged']=True
    	return redirect(url_for('get_products'))

@app.route('/logout')
def logout():
	session.pop('admin_logged', None)
	flash('Logged out!')
	return redirect(url_for('get_products'))


@app.route('/register', methods=['GET','POST'])
def register():
	form=RegistrationForm(request.form)
	if request.method=='POST' and form.validate():
		user=User(form.username.data,form.email.data,form.password.data)
		db.add(user)
		db.commit()
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/products', methods=['GET'])
def get_products():
	# p=Product(name='sadfasdf', threshold=12100, dueTime='asdasd', shortDesc='123123', profitRate='123123', profitType='1231231', profitDesc='123123', status='123123',organization='123132',investType='123123',investArea='123123',total=2300,detailDesc='asd',riskControl=1)
	# db.session.add(p)
	# db.session.commit()
	products=Product.query.all()
	if 'json'!=request.args.get('format'):
		return render_template('products.html',products=products)
	else:
		productsList=[]
		for product in products:
			productsList.append(Product.product2dict(product))
		return json.dumps(productsList, ensure_ascii=False).encode('utf8')

@app.route('/products', methods=['POST'])
def create_product():
	#if not request.json or 'name' not in request.json:
	#	abort(404)
	# name=request.json['name']
	# threshold=request.json.get('threshold', 1000000)
	# dueTime=request.json.get('dueTime', 'aa')
	# shortDesc=request.json.get('shortDesc')
	# profitRate=request.json.get('profitRate',0.10)
	# profitType=request.json.get('profitType', 'zhaiquan')
	# profitDesc=request.json.get('profitDesc','this is a good desc')
	# status=request.json.get('status', 'this is status')
	# organization=request.json.get('organization', 'org1')
	# investType=request.json.get('investType', 'investType')
	# investArea=request.json.get('investArea', 'investArea')
	# total=request.json.get('total',5000000)
	# detailDesc=request.json.get('detailDesc','detailDesc')
	# riskControl=request.json.get('riskControl', 'riskControl')
	form=ProductForm(request.form)
	p=Product(name=form.name.data, threshold=form.threshold.data, dueTime=form.dueTime.data, shortDesc=form.shortDesc.data, profitRate=form.profitRate.data, profitType=form.profitType.data, profitDesc=form.profitDesc.data, status=form.status.data,organization=form.organization.data,investType=form.investType.data,investArea=form.investArea.data,total=form.total.data,detailDesc=form.detailDesc.data,riskControl=form.riskControl.data)
	db.session.add(p)
	db.session.commit()
	flash('Add product successfully!')
	return redirect(url_for('create_product'))

@app.route('/product/<id>')
def product(id):
	product=Product.query.filter_by(id=id).first()
	#if product == None:
    #	flash('Product ' + id + ' not found.')
    #    return redirect(url_for('index'))
	if 'json'!=request.args.get('format'):
		return render_template('product.html', product=product)
	else:
		return json.dumps(product, default=Product.product2dict, ensure_ascii=False).encode('utf8')
