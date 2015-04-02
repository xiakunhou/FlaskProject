#coding:utf-8
from iInvest import app
from flask import render_template,flash,redirect, request
from forms import LoginForm
from models import Product

@app.route('/products')
def products():
	products=Product.query.all()
	return render_template('products.html',products=products)

@app.route('/product/<id>')
def product(id):
	product=Product.query.filter_by(id=id).first()
	#if product == None:
    #	flash('Product ' + id + ' not found.')
    #    return redirect(url_for('index'))
    	return render_template('product.html', product=product)
    	
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


