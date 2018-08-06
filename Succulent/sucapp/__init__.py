from django.apps import AppConfig
import os

default_app_config = 'sucapp.SucConfig'

VERBOSE_APP_NAME = u"多肉数据"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class SucConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME