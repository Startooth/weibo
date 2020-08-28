import datetime
import math

from flask import Blueprint
from flask import render_template, redirect, request
from flask import session

from libs.orm import db
from libs.utils import checkout
from blog.models import Blog, Comment, Thumb
from user.models import User


blog_bp = Blueprint('blog', __name__, url_prefix='/blog')
blog_bp.template_folder = './templates'


@blog_bp.route('/index')
@checkout
def idnex():
    '''查看主页'''
    page = int(request.args.get('page', 1))
    per_page = 30
    offset = per_page * (page - 1)
    data = Blog.query.order_by(Blog.lasttime.desc()).limit(per_page).offset(offset)
    # 显示分页
    max_page = math.ceil(Blog.query.count() / per_page)
    if page <= 3:
        start, end = 1, min(7, max_page)
    elif page>= (max_page - 2):
        start, end = (max_page - 6), max_page
    else:
        start, end = (page - 3), (page + 3)
    pages = range(start, end + 1)
    # 获取当前页码
    index = int(request.args.get('page'))
    return render_template('home.html',data=data,pages=pages,max=max_page,index=index)


@blog_bp.route('/post',methods=('POST','GET'))
@checkout
def post():
    '''发表微博'''
    if request.method == 'POST':
        content = request.form.get('content')
        time = datetime.datetime.now()
        lasttime = datetime.datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
        username = session['username']
        blog = Blog(content=content,lasttime=lasttime,username=username)
        db.session.add(blog)
        db.session.commit()
        return redirect('/user/info')
    else:
        return render_template('post.html')


@blog_bp.route('/modify',methods=('POST','GET'))
@checkout
def modify():
    '''修改微博'''
    # 检查是否是自己修改操作
    wid = int(request.form.get('wid', 0)) or int(request.args.get('wid', 0))
    blog = Blog.query.get(wid)
    if blog.username != session['username']:
        return render_template('response', msg='请先登录！')

    if request.method == 'POST':
        content = request.form.get('content','').strip()
        now = datetime.datetime.now()
        time = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        # 微博不能为空
        if not content:
            return render_template('post.html',msg='微博内容不能为空',blog=blog)
        # 修改原微博
        Blog.query.filter_by(wid=wid).update(
            {'wid': wid, 'content': content, 'lasttime': time})
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

@blog_bp.route('/comment',methods=('POST',))
def comment():
    '''发表评论/回复评论'''
    content = request.form.get('content')
    wid = int(request.form.get('wid'))
    cid = int(request.form.get('cid',0))
    page = request.form.get('page')
    time = datetime.datetime.now()

    comment = Comment(uid=session['uid'], wid=wid, cid=cid, content=content, time=time)
    db.session.add(comment)
    db.session.commit()

    return redirect(f'/user/show?wid={wid}&page={page}')


@blog_bp.route('/drop')
def drop():
    '''删除评论'''
    cid = int(request.args.get('cid'))
    cmt = Comment.query.get(cid)
    # 检查是否是在删除别人的评论
    if cmt.uid != session['uid']:
        return render_template('response.html',msg='拒绝访问')
    # 修改数据
    cmt.content = '当前评论已被删除'
    db.session.commit()
    return redirect('/blog/index')


@blog_bp.route('/follow')
def follow():
    '''关注'''
    pass


@blog_bp.route('/thumb')
def thumb():
    '''微博点赞/取消赞'''
    uid = int(request.args.get('uid'))
    wid = int(request.args.get('wid'))
    thumb_n = int(request.args.get('thumb'))
    page = request.args.get('page')
    before = Blog.query.get(wid)

    if thumb_n == 1:
        thumb = Thumb(uid=uid,wid=wid)
        Blog.query.filter_by(wid=wid).update({'thumb':(before.thumb + 1)})
        db.session.add(thumb)
    else:
        Thumb.query.filter_by(wid=wid).filter_by(uid=uid).delete()
        Blog.query.filter_by(wid=wid).update({'thumb':(before.thumb - 1)})
    db.session.commit()
    return redirect(f'/user/show?page={page}&wid={wid}')

@blog_bp.route('/hot')
def hot():
    '''查看热门微博'''
    pass
