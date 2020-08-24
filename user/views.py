from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import session
from flask import request

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'
user_bp.static_folder = './static'


@user_bp.route('/login',methods=('POST','GET'))
def login():
    '''用户登陆'''
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

@user_bp.route('/register')
def register():
    '''用户注册'''
    return render_template('register.html')

@user_bp.route('/info')
def info():
    '''用户信息'''
    return render_template('info.html')

@user_bp.route('/logout')
def logout():
    '''用户退出'''
    return redirect('/user/login')
