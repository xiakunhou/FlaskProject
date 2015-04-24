# -*- coding: utf-8 -*-
from iInvest import db
from datetime import datetime

#信托产品
class TrustProduct(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(20))
	#投资理由
	reason=db.Column(db.String(50))
	#投资起点
	threshold=db.Column(db.Integer)
	#产品期限，单位：月
	dueTime=db.Column(db.Integer)
	shortDesc=db.Column(db.String(200))
	#预期收益
	profitRate=db.Column(db.Float)
	#收益类型
	profitType=db.Column(db.String(50))
	#收益分配
	profitClose=db.Column(db.String(50))
	#收益说明
	profitDesc=db.Column(db.String(300))
	#状态，1:募集中，0，售完
	status=db.Column(db.SmallInteger)
	#管理机构
	organization=db.Column(db.String(50))
	#投资方式
	investType=db.Column(db.String(50))
	#投资领域
	investArea=db.Column(db.String(50))
	#发行规模
	total=db.Column(db.Integer)
	#资金用途
	detailDesc=db.Column(db.String(500))
	#风险控制
	riskControl=db.Column(db.String(500))

	def __repr__(self):
		return 'Trust Product is %r' %(self.name)

	def product2dict(prod):
		return {
			'id': prod.id,
			'name': prod.name,
			'reason':prod.reason,
			'threshold': prod.threshold,
			'dueTime': prod.dueTime,
			'shortDesc': prod.shortDesc,
			'profitRate': prod.profitRate,
			'profitType': prod.profitType,
			'profitDesc': prod.profitDesc,
			'profitClose': prod.profitClose,
			'status': prod.status,
			'organization': prod.organization,
			'investType': prod.investType,
			'investArea': prod.investArea,
			'total': prod.total,
			'detailDesc': prod.detailDesc,
			'riskControl': prod.riskControl
		}
	
''' 
	def __init__(self, name, reason, threshold, dueTime, shortDesc, profitRate, profitType, profitClose, profitDesc, status,organization,investType,investArea,total,detailDesc,riskControl):
		self.name=name
		self.reason=reason
		self.threshold=threshold
		self.dueTime=dueTime
		self.shortDesc=shortDesc
		self.profitRate=profitRate
		self.profitType=profitType
		self.profitDesc=profitDesc
		self.status=status
		self.organization=organization
		self.investType=investType
		self.profitClose=profitClose
		self.investArea=investArea
		self.total=total
		self.detailDesc=detailDesc
		self.riskControl=riskControl
'''
	


#资管产品
class AssetManagement(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(20),nullable=False)
	#投资理由
	reason=db.Column(db.String(50))
	#投资起点
	threshold=db.Column(db.Integer)
	#产品期限，单位：月
	dueTime=db.Column(db.Integer)
	shortDesc=db.Column(db.String(200))
	#预期收益
	profitRate=db.Column(db.Float)
	#收益类型
	profitType=db.Column(db.String(50))
	#收益分配
	profitClose=db.Column(db.String(50))
	#收益说明
	profitDesc=db.Column(db.String(300))
	#状态，1:募集中，0，售完
	status=db.Column(db.SmallInteger)
	#管理机构
	organization=db.Column(db.String(50))
	#投资方式
	investType=db.Column(db.String(50))
	#投资领域
	investArea=db.Column(db.String(50))
	#发行规模
	total=db.Column(db.Integer)
	#资金用途
	detailDesc=db.Column(db.String(500))
	#风险控制
	riskControl=db.Column(db.String(500))
''' 
	def __init__(self, name, reason=None, threshold=None, dueTime=None, shortDesc=None, profitRate=None, profitType=None, \
		profitClose=None, profitDesc=None, status=None,organization=None,investType=None,investArea=None,total=None,\
		self.name=name
		self.reason=reason
		self.threshold=threshold
		self.dueTime=dueTime
		self.shortDesc=shortDesc
		self.profitRate=profitRate
		self.profitType=profitType
		self.profitDesc=profitDesc
		self.status=status
		self.organization=organization
		self.investType=investType
		self.profitClose=profitClose
		self.investArea=investArea
		self.total=total
		self.detailDesc=detailDesc
		self.riskControl=riskControl
'''

	


class TrustProductPreorder(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	#user nick name
	name=db.Column(db.String(45))
	phone=db.Column(db.Integer)
	product_id=db.Column(db.Integer, db.ForeignKey('trust_product.id'))
	trust_product=db.relationship('TrustProduct', backref=db.backref('trust_preorders', lazy='dynamic'))
	#associated user, if not registed then a default user 00000000
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
	user=db.relationship('User',backref=db.backref('trust_preorders', lazy='dynamic'))
	status=db.Column(db.SmallInteger)#0, solved, 1 not solve, 2 solving, 3 high interest. 
	createTime=db.Column(db.DateTime)
	updateTime=db.Column(db.DateTime)
'''
	def __init__(self, name, phone, product_id, createTime=None,updateTime=None):
		self.name=name
		self.phone=phone
		self.product_id=product_id
		self.status=1
		if createTime is None:
			createTime=datetime.utcnow()
		self.createTime=createTime
		if updateTime is None:
			updateTime=datetime.utcnow()
		self.updateTime=updateTime
'''
class AssetManagementPreorder(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	#user nick name
	name=db.Column(db.String(45),nullable=False)
	phone=db.Column(db.Integer,nullable=False)
	product_id=db.Column(db.Integer, db.ForeignKey('asset_management.id'))
	asset_management=db.relationship('AssetManagement', backref=db.backref('asset_preorders', lazy='dynamic'))
	#associated user, if not registed then a default user 00000000
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
	user=db.relationship('User',backref=db.backref('asset_preorders', lazy='dynamic'))
	status=db.Column(db.SmallInteger)#0, solved, 1 not solve, 2 solving, 3 high interest. 
	createTime=db.Column(db.DateTime)
	updateTime=db.Column(db.DateTime)

	def __repr__(self):
		return 'AssetManagement is %r' %(self.name)

	def product2dict(prod):
		return {
			'id': prod.id,
			'name': prod.name,
			'reason':prod.reason,
			'threshold': prod.threshold,
			'dueTime': prod.dueTime,
			'shortDesc': prod.shortDesc,
			'profitRate': prod.profitRate,
			'profitType': prod.profitType,
			'profitDesc': prod.profitDesc,
			'profitClose': prod.profitClose,
			'status': prod.status,
			'organization': prod.organization,
			'investType': prod.investType,
			'investArea': prod.investArea,
			'total': prod.total,
			'detailDesc': prod.detailDesc,
			'riskControl': prod.riskControl
		}
'''
	def __init__(self, name, phone, product_id, createTime=None,updateTime=None):
		self.name=name
		self.phone=phone
		self.product_id=product_id
		self.status=1
		if createTime is None:
			createTime=datetime.utcnow()
		self.createTime=createTime
		if updateTime is None:
			updateTime=datetime.utcnow()
		self.updateTime=updateTime
'''

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	phone=db.Column(db.Integer)
	passwd=db.Column(db.String(200),nullable=False)
	email=db.Column(db.String(50))
	name=db.Column(db.String(45),unique=True,nullable=False)
	idNumber=db.Column(db.String(40))
	gender=db.Column(db.SmallInteger)
	birthday=db.Column(db.Date)
	level=db.Column(db.Integer)

	def is_authenticated(self):
		return True
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return True

	def get_id(self):
		return self.id

	def __unicode__(self):
		return self.name
'''
	def __init__(self, phone, passwd, email=None,name=None,idNumber=None, gender=1, birthday=None, level=0):
		self.phone=phone
		self.passwd=passwd
		self.email=email
		self.name=name
		self.idNumber=idNumber
		self.gender=gender
		self.birthday=birthday
		self.level=level
		# Flask-Login integration
'''
	



class Article(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	author=db.Column(db.String(50))
	content=db.Column(db.String(3000))
	createTime=db.Column(db.Date)
	#
	category=db.Column(db.Integer)

	def __init__(self, content, author=None, createTime=None, category=0):
		self.author=author
		self.content=content
		if createTime is None:
			createTime=datetime.utcnow().date()
		self.createTime=createTime
		self.category=category