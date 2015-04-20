#coding:utf-8
from iInvest import app, db, bcrypt
from flask import render_template,flash,redirect, request, abort, url_for, session, jsonify, make_response
from forms import LoginForm, RegistrationForm, ProductForm, TrustProductForm, AssetManagementForm
import datetime
from models import Product, Preorder, TrustProduct, TrustProductPreorder, User, AssetManagement , AssetManagementPreorder
import json
import flask

###############资管产品#########################
@app.route('/assetManagements', methods=['GET'])
def get_asset_management():
	product_list=AssetManagement.query.with_entities(AssetManagement.id, AssetManagement.name, AssetManagement.reason, \
		AssetManagement.threshold,AssetManagement.dueTime,AssetManagement.profitRate).all()
	productsList=[]
	for product in product_list:
		productsList.append({'id':product[0],'name':product[1],'reason':product[2],'threshold':product[3],'dueTime':product[4],'profitRate':product[5]})
	return render_template('assetManagements.html',products=productsList)

@app.route('/assetManagements', methods=['POST'])
def create_asset_management():
	form=AssetManagementForm(request.form)
	print request.form['csrf_token']
	if not form.validate():
		return make_response(jsonify({'error': form.errors}), 400)
	p=AssetManagement(name=form.name.data, reason=form.reason.data, threshold=form.threshold.data, dueTime=form.dueTime.data, \
		shortDesc=form.shortDesc.data, profitRate=form.profitRate.data, profitType=form.profitType.data, profitClose=form.profitClose.data, \
		profitDesc=form.profitDesc.data, status=form.status.data,organization=form.organization.data,investType=form.investType.data,\
		investArea=form.investArea.data,total=form.total.data, detailDesc=form.detailDesc.data,riskControl=form.riskControl.data)
	db.session.add(p)
	db.session.commit()
	flash('Add asset management successfully!')
	return redirect(url_for('create_asset_management'))



@app.route('/assetManagement/<id>', methods=['GET'])
def asset_management(id):
	product=AssetManagement.query.filter_by(id=id).first()
	return render_template('assetManagement.html', product=product)


@app.route('/assetManagement/<id>', methods=['DELETE'])
def delete_asset_management(id):
	AssetManagement.query.filter_by(id=id).delete()
	db.session.commit()
	flash('Delete asset management successfully!')
	return '201'

@app.route('/assetPreorders/', methods=['GET'])
def get_asset_preorders():
	preorders=AssetManagementPreorder.query.all()
	return render_template('assetPreorders.html', preorders=preorders)

@app.route('/assetPreorders/', methods=['POST'])
def create_asset_preorders():
	if not request.form or not 'product_id' in request.form or not 'customer_name' in request.form or not 'customer_phone' in request.form:
		abort(400)
	preorder=AssetManagementPreorder(request.form['customer_name'],request.form['customer_phone'],request.form['product_id'])
	db.session.add(preorder)
	db.session.commit()
	flash('Add asset preorder successfully!')
	return redirect(url_for('create_asset_preorders'))

##JSON API#######################################################
@app.route('/assetManagements/json', methods=['GET'])
def json_get_asset_managements():
	product_list=AssetManagement.query.with_entities(AssetManagement.id, AssetManagement.name, AssetManagement.reason, \
		AssetManagement.threshold,AssetManagement.dueTime,AssetManagement.profitRate).all()
	productsList=[]
	for product in product_list:
		productsList.append({'id':product[0],'name':product[1],'reason':product[2],'threshold':product[3],'dueTime':product[4],'profitRate':product[5]})
	return json.dumps(productsList, ensure_ascii=False).encode('utf8')

@app.route('/assetManagement/<id>/json', methods=['GET'])
def json_asset_management(id):
	product=AssetManagement.query.filter_by(id=id).first()
	return json.dumps(product, default=AssetManagement.product2dict, ensure_ascii=False).encode('utf8')

@csrf.exempt
@app.route('/assetPreorders/json', methods=['POST'])
def json_create_asset_preorders():
	if not request.json or not 'product_id' in request.json or not 'customer_name' in request.json or not 'customer_phone' in request.json:
		abort(400)
	preorder=AssetManagementPreorder(request.json['customer_name'],request.json['customer_phone'],request.json['product_id'])
	db.session.add(preorder)
	db.session.commit()
	return jsonify({'status':'success'}), 201

@app.route('/assetPreorders/json', methods=['GET'])
def json_get_asset_preorders():
	preorder_list=AssetManagementPreorder.query.with_entities(AssetManagementPreorder.id, AssetManagementPreorder.name, AssetManagementPreorder.phone, \
		AssetManagementPreorder.product_id,AssetManagementPreorder.createTime,AssetManagementPreorder.updateTime).all()
	ordersList=[]
	for preorder in preorder_list:
		ordersList.append({'id':preorder[0],'nick_name':preorder[1],'customer_phone':preorder[2],'asset_id':preorder[3],'createTime':preorder[4].strftime('%Y/%m/%d-%H:%M:%S')})
	return json.dumps(ordersList, ensure_ascii=False).encode('utf8')

