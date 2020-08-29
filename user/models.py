from libs.orm import db
import random

class User(db.Model):
    '''初始化用户表'''
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Enum('男', '女', '保密'), default='保密')
    phone = db.Column(db.String(16), unique=True, nullable=False)
    city = db.Column(db.String(16), nullable=False, default='暂无')
    photo = db.Column(db.String(128), default='/static/img/default')
    hobbit = db.Column(db.String(20), nullable=False, default='暂无')
    des = db.Column(db.Text,nullable=False, default='暂无')
    follow = db.Column(db.Integer,nullable=False,default=0)
    fans = db.Column(db.Integer, nullable=False, default=0)

    @classmethod
    def fake_users(cls, num):
        users = []
        phone = 13555879797
        for i in range(num):
            username = '测试用户' + str(random.randint(100,999))
            password = '123'
            phone = phone + 1
            gender = random.choice(['男', '女', '保密'])
            user = cls(username=username, password=password, gender=gender, phone=phone)
            users.append(user)
        db.session.add_all(users)
        db.session.commit()
        return users


class Follow(db.Model):
    __tablename__ = 'follow'

    uid = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer, primary_key=True)
