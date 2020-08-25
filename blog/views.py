import datetime

from flask import Blueprint
from flask import render_template, redirect, request
from flask import session

from libs.orm import db
from libs.utils import checkout
from blog.models import Blog
from user.models import User


blog_bp = Blueprint('blog', __name__, url_prefix='/blog')
blog_bp.template_folder = './templates'
blog_bp.static_folder = './static'


@blog_bp.route('/index')
@checkout
def idnex():
    '''查看主页'''
    data = Blog.query.order_by(Blog.lasttime.desc()).all()
    return render_template('home.html',data=data)

@blog_bp.route('/hot')
def hot():
    '''查看热门微博'''
    pass

@blog_bp.route('/post',methods=('POST','GET'))
@checkout
def post():
    '''发表微博'''
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        time = datetime.datetime.now()
        lasttime = datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
        username = session['username']
        blog = Blog(title=title,content=content,lasttime=lasttime,username=username)
        db.session.add(blog)
        db.session.commit()
        return redirect('/user/info')
    else:
        return render_template('post.html')


@blog_bp.route('/modify',methods=('POST','GET'))
@checkout
def modify():
    '''修改微博'''
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        wid = request.form.get('wid')
        now = datetime.datetime.now()
        time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        old_blog = Blog.query.filter_by(wid=wid).one()
        # 修改原微博
        old_blog.update({'wid':wid, 'title':title, 'content':content, 'lasttime':time})
        db.session.commit()
        return redirect('/user/info')
    else:
        wid = request.args.get('wid')
        blog = Blog.query.filter_by(wid=wid).one()
        return render_template('post.html',op='mine',blog=blog)

@blog_bp.route('/delete')
@checkout
def delete():
    '''删除微博'''
    wid = request.args.get('wid')
    old_blog = Blog.query.filter_by(wid=wid).one()
    db.session.delete(old_blog)
    db.session.commit()
    return redirect('/user/info')

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
