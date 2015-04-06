#coding:utf-8
from iInvest import app, db
from flask import render_template,flash,redirect, request
from forms import LoginForm, RegistrationForm
from models import Product
import json
    	
@app.route('/')
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

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
	return render_template('login.html',title = 'Sign In',form = form)

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)


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

@app.route('/products')
def products():
	p=Product(name='sadfasdf', threshold=12100, dueTime='asdasd', shortDesc='123123', profitRate='123123', profitType='1231231', profitDesc='123123', status='123123',organization='123132',investType='123123',investArea='123123',total=2300,detailDesc='asd',riskControl=1)
	db.session.add(p)
	db.session.commit()
	products=Product.query.all()
	if 'json'!=request.args.get('format'):
		return render_template('products.html',products=products)
	else:
		productsList=[]
		for product in products:
			productsList.append(json.dumps(product, default=Product.product2dict))
		return json.dumps(productsList)


@app.route('/product/<id>')
def product(id):
	product=Product.query.filter_by(id=id).first()
	#if product == None:
    #	flash('Product ' + id + ' not found.')
    #    return redirect(url_for('index'))
	if 'json'!=request.args.get('format'):
		return render_template('product.html', product=product)
	else:
		return json.dumps(product, default=Product.product2dict)
