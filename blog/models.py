from libs.orm import db


class Blog(db.Model):
    '''初始化微博功能表'''
    __tablename__ = 'blog'
    wid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)
    thumb = db.Column(db.Integer,default=0)
    username = db.Column(db.String(20), nullable=False)


class Blog_User(db.Model):
    '''用户和微博点赞关系表'''
    __tablename__ = 'blog_user'
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer)
    wid = db.Column(db.Integer)
