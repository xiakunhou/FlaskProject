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
	
	def __repr__(self):
		return 'Product %r' %(self.name)

