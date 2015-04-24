#coding:utf-8
from iInvest import app, db, bcrypt, csrf
from flask import render_template,flash,redirect, request, abort, url_for, session, jsonify, make_response
from forms import LoginForm, RegistrationForm, TrustProductForm
import datetime
from models import TrustProduct, TrustProductPreorder, User
import json
import flask
import os
import random
import datetime


@app.errorhandler(404)
def bad_request(error):
    return render_template('404.html'), 404

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/hello', methods=['POST'])
def hello():
    phone=request.form['phone']
    password=request.form['password']
    print phone, password
    
    if phone=='admin' and password=='admin':
        flash('admin logged in!')
        session['admin_logged']=True
        session['user']='admin'
        session.permanent=False
        return redirect(url_for('get_trust_products'))
    storedPW=User.query.filter_by(phone=phone).first().passwd
    if bcrypt.check_password_hash(storedPW,password+'ta02%&9!(#HHK_dsKYas;'):
        session['user_logged']=True
        session['user']=phone
        session.permanent=False
        return redirect(url_for('get_trust_products'))

@app.route('/logout')
def logout():
    session.pop('admin_logged', None)
    session.pop('user_logged', None)
    session.pop('user', None)
    flash('Logged out!')
    return redirect(url_for('get_trust_products'))

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin']='*'
    return response

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm(request.form)
    if request.method=='POST' and form.validate():
        print form.errors
        password=bcrypt.generate_password_hash(form.password.data+'ta02%&9!(#HHK_dsKYas;')
        user=User(form.phone.data, password)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@csrf.exempt
@app.route('/ckupload', methods=['POST', 'OPTIONS'])
def ckupload():
    print 'hahahahha'
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")
    print callback
    print request.method
    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        print fileobj
        fname, fext = os.path.splitext(fileobj.filename)
        print fname, fext
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(app.static_folder, 'upload', rnd_name)
        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'
        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
    else:
        error = 'post error'
    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)
    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response
