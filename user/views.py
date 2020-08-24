from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import session
from flask import request

from user.models import User
from libs.orm import db

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'
user_bp.static_folder = './static'


@user_bp.route('/login',methods=('POST','GET'))
def login():
    '''用户登陆'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        num = User.query.filter_by(username=username).count()
        if num == 0:
            return render_template('response.html', msg='用户名不存在！')
        user = User.query.filter_by(username=username).one()
        if user.password != password:
            return render_template('response.html', msg='用户名密码错误！')
        # session记录username
        session['username'] = username
        # return render_template('home.html')
        return redirect('/blog/index')
    else:
        return render_template('login.html')

@user_bp.route('/register',methods=('POST','GET'))
def register():
    '''用户注册'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        check = User.query.filter_by(username=username).count()
        if password != pwd:
            return render_template('response.html',msg='两次密码输入不一致')
        if check != 0:
            return render_template('response.html',msg='用户名已存在')
        user = User(username=username, password=password,gender=gender, phone=phone)
        db.session.add(user)
        db.session.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')

@user_bp.route('/info')
def info():
    '''用户信息'''
    return render_template('info.html')

@user_bp.route('/logout')
def logout():
    '''用户退出'''
    return redirect('/user/login')
