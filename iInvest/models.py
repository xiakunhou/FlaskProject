from iInvest import db

class Product(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(20))
	threshold=db.Column(db.Integer)
	dueTime=db.Column(db.String(20))
	shortDesc=db.Column(db.String(128))
	profitRate=db.Column(db.Float)
	profitType=db.Column(db.String(45))
	profitDesc=db.Column(db.String(255))
	status=db.Column(db.SmallInteger)
	organization=db.Column(db.String(45))
	investType=db.Column(db.String(45))
	investArea=db.Column(db.String(45))
	total=db.Column(db.Integer)
	detailDesc=db.Column(db.String(256))
	riskControl=db.Column(db.String(256))
	
	def __init__(self, name, threshold, dueTime, shortDesc, profitRate, profitType, profitDesc, status,organization,investType,investArea,total,detailDesc,riskControl):
		self.name=name
		self.threshold=threshold
		self.dueTime=dueTime
		self.shortDesc=shortDesc
		self.profitRate=profitRate
		self.profitType=profitType
		self.profitDesc=profitDesc
		self.status=status
		self.organization=organization
		self.investType=investType
		self.investArea=investArea
		self.total=total
		self.detailDesc=detailDesc
		self.riskControl=riskControl
	
	def __repr__(self):
		return 'Product is %r' %(self.name)

	def product2dict(prod):
		return {
			'id': prod.id,
			'name': prod.name,
			'threshold': prod.threshold,
			'dueTime': prod.dueTime,
			'shortDesc': prod.shortDesc,
			'profitRate': prod.profitRate,
			'profitType': prod.profitType,
			'profitDesc': prod.profitDesc,
			'status': prod.status,
			'organization': prod.organization,
			'investType': prod.investType,
			'investArea': prod.investArea,
			'sotal': prod.total,
			'detailDesc': prod.detailDesc,
			'siskControl': prod.riskControl
		}