# -*-coding:utf-8 -*-
# 启动脚本
import sys
reload(sys)
sys.setdefaultencoding('utf8')  #修改PYTHON默认字符编码
import os
from app import create_app, db
from app.models import User, Role, Follow, Comment
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():  # 集成Python shell
    return dict(app=app, db=db, User=User, Role=Role, Follow=Follow, Comment=Comment)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():  # 单元测试
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
    #app.run()