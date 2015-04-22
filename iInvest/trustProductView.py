#coding:utf-8
from iInvest import app, db, bcrypt, csrf
from flask_wtf.csrf import generate_csrf
from flask import render_template,flash,redirect, request, abort, url_for, session, jsonify, make_response
from forms import LoginForm, RegistrationForm, ProductForm, TrustProductForm
import datetime
from models import Product, Preorder, TrustProduct, TrustProductPreorder, User
import json
import flask

###############信托产品#########################


@app.route('/token')
def token():
	token=generate_csrf(time_limit=10)
	return jsonify({'token':token}), 201

@app.route('/')
@app.route('/index')
@app.route('/trustProducts', methods=['GET'])
def get_trust_products():
	product_list=TrustProduct.query.with_entities(TrustProduct.id, TrustProduct.name, TrustProduct.reason, \
		TrustProduct.threshold,TrustProduct.dueTime,TrustProduct.profitRate).all()
	productsList=[]
	for product in product_list:
		productsList.append({'id':product[0],'name':product[1],'reason':product[2],'threshold':product[3],'dueTime':product[4],'profitRate':product[5]})
	return render_template('trustProducts.html',products=productsList)

@app.route('/trustProducts', methods=['POST'])
def create_trust_product():
	form=TrustProductForm(request.form)
	print request.form['csrf_token']
	if not form.validate():
		return make_response(jsonify({'error': form.errors}), 400)
	p=TrustProduct(name=form.name.data, reason=form.reason.data, threshold=form.threshold.data, dueTime=form.dueTime.data, \
		shortDesc=form.shortDesc.data, profitRate=form.profitRate.data, profitType=form.profitType.data, profitClose=form.profitClose.data, \
		profitDesc=form.profitDesc.data, status=form.status.data,organization=form.organization.data,investType=form.investType.data,\
		investArea=form.investArea.data,total=form.total.data, detailDesc=form.detailDesc.data,riskControl=form.riskControl.data)
	db.session.add(p)
	db.session.commit()
	flash('Add trust product successfully!')
	return redirect(url_for('create_trust_product'))

@app.route('/trustProduct/<id>', methods=['GET'])
def trust_product(id):
	product=TrustProduct.query.filter_by(id=id).first()
	return render_template('trustProduct.html', product=product)


@app.route('/trustProduct/<id>', methods=['DELETE'])
def delete_trust_product(id):
	TrustProduct.query.filter_by(id=id).delete()
	db.session.commit()
	flash('Delete trust product successfully!')
	return '201'

@app.route('/trustPreorders/', methods=['GET'])
def get_trust_preorders():
	preorders=TrustProductPreorder.query.all()
	return render_template('trustPreorders.html', preorders=preorders)

@app.route('/trustPreorders/', methods=['POST'])
def create_trust_preorders():
	if not request.form or not 'product_id' in request.form or not 'customer_name' in request.form or not 'customer_phone' in request.form:
		abort(400)
	preorder=TrustProductPreorder(request.form['customer_name'],request.form['customer_phone'],request.form['product_id'])
	db.session.add(preorder)
	db.session.commit()
	flash('Add preorder successfully!')
	return redirect(url_for('create_trust_preorders'))

##JSON API#######################################################
@app.route('/trustProducts/json', methods=['GET'])
def json_get_trust_products():
	product_list=TrustProduct.query.with_entities(TrustProduct.id, TrustProduct.name, TrustProduct.reason, \
		TrustProduct.threshold,TrustProduct.dueTime,TrustProduct.profitRate).all()
	productsList=[]
	for product in product_list:
		productsList.append({'id':product[0],'name':product[1],'reason':product[2],'threshold':product[3],'dueTime':product[4],'profitRate':product[5]})
	return json.dumps(productsList, ensure_ascii=False).encode('utf8')

@app.route('/trustProduct/<id>/json', methods=['GET'])
def json_trust_product(id):
	product=TrustProduct.query.filter_by(id=id).first()
	return json.dumps(product, default=TrustProduct.product2dict, ensure_ascii=False).encode('utf8')

#@csrf.exempt
@app.route('/trustPreorders/json', methods=['POST'])
def json_create_trust_preorders():
	if not request.json or not 'product_id' in request.json or not 'customer_name' in request.json or not 'customer_phone' in request.json:
		abort(400)
	preorder=TrustProductPreorder(request.json['customer_name'],request.json['customer_phone'],request.json['product_id'])
	db.session.add(preorder)
	db.session.commit()
	return jsonify({'status':'success'}), 201

@app.route('/trustPreorders/json', methods=['GET'])
def json_get_trust_preorders():
	preOrder_list=TrustProductPreorder.query.with_entities(TrustProductPreorder.id, TrustProductPreorder.name, TrustProductPreorder.phone, \
		TrustProductPreorder.product_id,TrustProductPreorder.createTime,TrustProductPreorder.updateTime).all()
	ordersList=[]
	for preorder in preOrder_list:
		ordersList.append({'id':preorder[0],'nick_name':preorder[1],'customer_phone':preorder[2],'trust_id':preorder[3],\
			'createTime':preorder[4].strftime('%Y/%m/%d-%H:%M:%S')})
	return json.dumps(ordersList, ensure_ascii=False).encode('utf8')
