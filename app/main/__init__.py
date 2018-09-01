# -*-coding:utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor  # 模板(templates)上下文处理器，这样做的话，在模板中可以访问Permission
def inject_permissions():
    return dict(Permission=Permission)
