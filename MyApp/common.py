import sys
import logging
from .utils import *

logging.basicConfig(stream=sys.stderr, level=getattr(logging, app_config.log_level))
logger = logging.getLogger(__name__)

logging.debug("logging started")

