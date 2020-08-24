from flask import Blueprint
from flask import render_template
from flask import redirect

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')
blog_bp.template_folder = './templates'
blog_bp.static_folder = './static'

@blog_bp.route('/post')
def post():
    '''发表微博'''
    pass

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
