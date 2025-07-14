import sys
import logging

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)