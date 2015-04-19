#coding:utf-8
from iInvest import app, db
from flask import render_template
from models import Article

@app.route('/articles', methods=['GET','POST'])
def create_article():
	if request.method=='POST':
		request.form['']
		return render_template('articles.html')
	return render_template('articles.html')