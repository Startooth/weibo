from libs.orm import db
from user.models import User
from libs.utils import random_word
import random


class Blog(db.Model):
    '''初始化微博功能表'''
    __tablename__ = 'blog'
    wid = db.Column(db.Integer, primary_key=True, unique=True)
    content = db.Column(db.Text, nullable=False)
    lasttime = db.Column(db.DateTime)
    thumb = db.Column(db.Integer,default=0)
    username = db.Column(db.String(20), nullable=False)

    @property
    def author(self):
        return User.query.filter_by(username=self.username).one()

    @classmethod
    def fake_weibos(cls, username_list, num):
        wb_list = []
        for i in range(num):
            year = random.randint(2010, 2019)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            date = '%04d-%02d-%02d' % (year, month, day)

            username = random.choice(username_list)
            content = random_word(random.randint(70, 140))
            wb = cls(username=username, content=content, lasttime=date)
            wb_list.append(wb)

        db.session.add_all(wb_list)
        db.session.commit()
    
class Comment(db.Model):
    '''初始化评论功能表'''
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False, index=True)
    wid = db.Column(db.Integer, nullable=False, index=True)
    cid = db.Column(db.Integer, nullable=False, index=True, default=0)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime)

    @property
    def author(self):
        return User.query.get(self.uid)
    
    @property
    def upper(self):
        if self.id == 0:
            return None
        else:
            return Comment.query.get(self.cid)

class Thumb(db.Model):
    __tablename__ = 'thumb'
    uid = db.Column(db.Integer, primary_key=True)
    wid = db.Column(db.Integer, primary_key=True)