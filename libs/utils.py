import os
from flask import session, redirect
from hashlib import md5, sha256
import random


def make_password(password):
    '''产生一个安全密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')
    hash_value = sha256(password).hexdigest()
    salt = os.urandom(16).hex()
    safe_password = salt + hash_value
    return safe_password


def check_password(password, safe_password):
    '''用MD5检查密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')
    hash_value = sha256(password).hexdigest()
    return hash_value == safe_password[32:]


def save_avatar(avatar_file):
    '''保存头像文件'''
    file_bin_data = avatar_file.stream.read()
    avatar_file.stream.seek(0)
    filename = md5(file_bin_data).hexdigest()
    base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    filepath = os.path.join(base_dir, 'static', 'avatar', filename)
    avatar_file.save(filepath)
    # avatar_url = os.path.join('static','avatar',filename)
    avatar_url = f'/static/avatar/{filename}'
    return avatar_url


def checkout(func):
    '''检查用户是否登陆'''
    def check_session(*args, **kwargs):
        username = session.get('username')
        if not username:
            return redirect('/')
        else:
            return func(*args, **kwargs)
    check_session.__name__ = func.__name__
    return check_session


def random_word(length):
    '''随机生成汉字'''
    words = [chr(random.randint(25000, 30000)) for i in range(length)]
    return ''.join(words)
