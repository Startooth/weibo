from flask import Blueprint
from flask import render_template, redirect, request
from flask import session

from user.models import User
from blog.models import Blog, Comment, Thumb
from libs.orm import db
from libs.utils import checkout, save_avatar, make_password, check_password

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/login',methods=('POST','GET'))
def login():
    '''用户登陆'''
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        num = User.query.filter_by(username=username).count()
        if num == 0:
            return render_template('response.html', msg='用户名不存在！')
        user = User.query.filter_by(username=username).one()
        if not check_password(password,user.password):
            return render_template('response.html', msg='用户名密码错误！')
        # session记录username
        user = User.query.filter_by(username=username).one()
        session['username'] = username
        session['uid'] = user.uid
        # return render_template('home.html')
        return redirect('/user/info')
    else:
        return render_template('index.html')

@user_bp.route('/register',methods=('POST','GET'))
def register():
    '''用户注册'''
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password','').strip()
        pwd = request.form.get('pwd','').strip()
        gender = request.form.get('gender')
        phone = request.form.get('phone', '').strip()
        check = User.query.filter_by(username=username).count()
        if password != pwd:
            return render_template('response.html',msg='两次密码输入不一致')
        if check != 0:
            return render_template('response.html',msg='用户名已存在')
        user = User(username=username, password=make_password(password),gender=gender, phone=phone)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('index.html')


@user_bp.route('/info')
@checkout
def info():
    '''用户信息'''
    username = session['username']
    user = User.query.filter_by(username=username).one()
    blog = Blog.query.filter_by(username=username).order_by(Blog.lasttime.desc()).limit(10).all()
    return render_template('info.html',user=user,blogs=blog)


@user_bp.route('/modify',methods=('POST','GET'))
@checkout
def modify():
    '''修改用户信息'''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        phone = request.form.get('phone')
        city = request.form.get('city')
        hobbit = request.form.get('hobbit')
        des = request.form.get('des')

        photo = request.files.get('photo')
        if photo:
            photo = save_avatar(photo)
        old_user = User.query.filter_by(username=username)
        old_user.update({
                'username': username, 'password': make_password(password), 
                'gender': gender, 'phone': phone, 
                'photo': photo, 'city':city, 
                'hobbit': hobbit, 'des': des
                })
        db.session.commit()
        return render_template('response.html',msg='修改成功')
    else:
        username = session['username']
        user = User.query.filter_by(username=username).one()
        return render_template('modify.html',user=user)


@user_bp.route('/show')
@checkout
def show():
    '''显示文章内容'''
    # username = request.args.get('username')
    username = session['username']
    page = request.args.get('page')
    wid = request.args.get('wid')
    op = request.args.get('op',0)
    blog = Blog.query.get(wid)

    # 获取当前文章评论
    comment = Comment.query.filter_by(wid=wid).order_by(Comment.time.desc())

    # 确认当前文章是否被当前用户点赞
    uid = session['uid']
    thumb = int(Thumb.query.filter_by(uid=uid).filter_by(wid=wid).count())
    return render_template('show.html', blog=blog, op=op,page=page,comment=comment,thumb=thumb)


@user_bp.route('/logout')
@checkout
def logout():
    '''用户退出'''
    # session.pop('username')
    session.clear()
    return redirect('/user/login')
