import os
import sys
import logging

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
