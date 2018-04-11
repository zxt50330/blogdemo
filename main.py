from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from base import db, ma
from views import blueprint
import json
import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:@localhost/learn1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
ma.init_app(app)
app.register_blueprint(blueprint)
migrate = Migrate(app, db)
# migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# @app.route('/')
# def hello_world():
#     return 'Hello World'
#
#
# @app.route('/api/current_time', methods=['GET'])
# def current_time():
#     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     return json.dumps({"current_time": nowTime})

if __name__ == '__main__':
    manager.run()
