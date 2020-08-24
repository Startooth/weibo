from libs.orm import db


class User(db.Model):
    '''初始化微博功能表'''
    __tablename__ = 'blog'
    wid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)
    thumb = db.Column(db.Boolean(16))
