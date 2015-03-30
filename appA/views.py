#coding:utf-8
from appA import app
from flask import render_template,flash,redirect
from forms import LoginForm
from models import Product

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

@app.route('/products')
def products():
	products=[
	{
 	 'id':10000000,
	 'name':'优债4号', 
	 'threshold':1000000,
	 'dueTime':'24月',
	 'shortDesc':'AA级国有肚子企业担保',
	 'profitRate':0.102,
	 'status':1 #火热募集中
	},
	{
	 'id':'10000001',
	 'name':'金马210号', 
	 'threshold':500000,
	 'dueTime':'12月',
	 'shortDesc':'AA级国有肚子企业担保',
	 'profitRate':0.120,
	 'status':1 #火热募集中
	}
	]
	products=Product.query.all()
	return render_template('products.html',products=products)

