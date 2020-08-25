from libs.orm import db


class Blog(db.Model):
    '''初始化微博功能表'''
    __tablename__ = 'blog'
    wid = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    lasttime = db.Column(db.DateTime)
    thumb = db.Column(db.Integer,default=0)
    username = db.Column(db.String(20), nullable=False)
