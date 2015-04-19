#coding:utf-8
from iInvest import app, db
from flask import render_template, request, redirect, url_for
from models import Article

@app.route('/articles', methods=['GET', 'POST'])
def articles():
	print request.method
	if request.method=='POST':
		content=request.form['article'].replace('\r\n', '')
		article=Article(content, category=1)
		db.session.add(article)
		db.session.commit()
		return redirect(url_for('articles'))
	articles=Article.query.all()
	return render_template('articles.html', articles=articles)
	