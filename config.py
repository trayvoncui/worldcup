# -*-coding:utf-8 -*-
import os

# from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
basedir = os.path.abspath(os.path.dirname(__file__))


# 配置类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # 密钥
    MAIL_SERVER = 'smtp.qq.com'  # 邮箱服务器
    MAIL_PORT = '465'  # 邮箱端口
    # MAIL_USE_TLS = True
    MAIL_USE_SSL = True  # 安全套接岑协议
    MAIL_USERNAME = '1130831892@qq.com'  # 用户名
    MAIL_PASSWORD = 'qugkudslltgffhbh'  # 密码
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 主题前缀
    FLASKY_MAIL_SENDER = '1130831892@qq.com'  # 发送方
    FLASKY_ADMIN = '1130831892@qq.com'  # 管理员邮箱
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束后自动提交数据库中的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它。
    FLASKY_POSTS_PER_PAGE = 20  # 每页条目
    FLASKY_FOLLOWERS_PER_PAGE = 50  # 关注者数目
    FLASKY_COMMENTS_PER_PAGE = 30  # 评论条目
    UPLOAD_FOLDER = r'D:\python\myflask2\app\static\img\postImg'  # 文件上传路径

    @staticmethod
    def init_app(app):  # 可以执行对当前环境的配置初始化
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
