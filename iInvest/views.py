#coding:utf-8
from iInvest import app, db, bcrypt
from flask import render_template,flash,redirect, request, abort, url_for, session, jsonify, make_response
from forms import LoginForm, RegistrationForm, ProductForm, TrustProductForm
import datetime
from models import Product, Preorder, TrustProduct, TrustProductPreorder, User
import json
import flask


@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error':'Bad request'}), 400)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/hello', methods=['POST'])
def hello():
	phone=request.form['phone']
	password=request.form['password']
	print phone, password
	
	if phone=='admin' and password=='admin':
		flash('admin logged in!')
		session['admin_logged']=True
		session['user']='admin'
		return redirect(url_for('get_trust_products'))
	storedPW=User.query.filter_by(phone=phone).first().passwd
	if bcrypt.check_password_hash(storedPW,password+'ta02%&9!(#HHK_dsKYas;'):
		session['user_logged']=True
		session['user']=phone
		return redirect(url_for('get_trust_products'))

@app.route('/logout')
def logout():
	session.pop('admin_logged', None)
	session.pop('user_logged', None)
	session.pop('user', None)
	flash('Logged out!')
	return redirect(url_for('get_trust_products'))

@app.after_request
def add_header(response):
	response.headers['Access-Control-Allow-Origin']='*'
	return response

@app.route('/register', methods=['GET','POST'])
def register():
	form=RegistrationForm(request.form)
	if request.method=='POST' and form.validate():
		print form.errors
		password=bcrypt.generate_password_hash(form.password.data+'ta02%&9!(#HHK_dsKYas;')
		user=User(form.phone.data, password)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/products', methods=['GET'])
def get_products():
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

@app.route('/preorders/', methods=['GET'])
def get_preorders():
	preorders=Preorder.query.all()
	return render_template('preorders.html', preorders=preorders)

@app.route('/preorders/', methods=['POST'])
def create_preorders():
	if not request.form or not 'product_id' in request.form or not 'customer_name' in request.form or not 'customer_phone' in request.form:
		abort(400)
	preorder=Preorder(request.form['customer_name'],request.form['customer_phone'],request.form['product_id'])
	db.session.add(preorder)
	db.session.commit()
	flash('Add preorder successfully!')
	return redirect(url_for('create_preorders'))
#@csrt.exempt
@app.route('/preorders/json', methods=['POST'])
def json_create_preorders():
	#print request
	print 'test'
	#print request.json
	print request.mimetype
	print request.json
	print 'aaa',request.get_json(force=True)
	print request.json['product_id']
	if not request.json or not 'product_id' in request.json or not 'customer_name' in request.json or not 'customer_phone' in request.json:
		abort(400)
	preorder=Preorder(request.json['customer_name'],request.json['customer_phone'],request.json['product_id'])
	db.session.add(preorder)
	db.session.commit()
	return jsonify({'status':'success'}), 201

