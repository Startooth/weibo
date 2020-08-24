import datetime

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session

from libs.orm import db
from blog.models import Blog
from user.models import User

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')
blog_bp.template_folder = './templates'
blog_bp.static_folder = './static'


def checkout():
    '''判断用户是否登陆'''
    count = User.query.filter_by(username=session['username']).count()
    return count


@blog_bp.route('/index')
def idnex():
    '''查看主页'''
    if checkout():
        data = Blog.query.order_by(Blog.date.desc()).all()
        return render_template('home.html',data=data)
    else:
        return redirect('/')

@blog_bp.route('/hot')
def hot():
    '''查看热门微博'''
    pass

@blog_bp.route('/post',methods=('POST','GET'))
def post():
    '''发表微博'''
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        time = datetime.datetime.now()
        date = datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
        blog = Blog(title=title,content=content,date=date)
        db.session.add(blog)
        db.session.commit()
    else:
        return render_template('post.html')

@blog_bp.route('/modify')
def modify():
    '''修改微博'''
    pass

@blog_bp.route('/delete')
def delete():
    '''删除微博'''
    pass

@blog_bp.route('/comment')
def comment():
    '''发表评论'''
    pass

@blog_bp.route('/follow')
def follow():
    '''关注'''
    pass


@blog_bp.route('/thumb')
def thumb():
    '''微博点赞'''
    pass
