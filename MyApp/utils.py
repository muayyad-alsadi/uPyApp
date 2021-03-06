import logging

from collections import OrderedDict

from .base_utils import *
from .config import app_config

logger = logging.getLogger(__name__)

commands=OrderedDict()

def command(func):
    """decorator to make function into cli commands"""
    commands[func.__name__]=func
    def wrapped(*a, **kw):
        return func(*a, **kw)
    return wrapped
