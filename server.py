from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import render_template

from libs.orm import db
from user.views import user_bp
from blog.views import blog_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zysqwxfx0714@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = r'dsaf^%*EfdfggfghdnydbrdsdasdadjhGH9-ua'


db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


app.register_blueprint(user_bp)
app.register_blueprint(blog_bp)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    manager.run()
