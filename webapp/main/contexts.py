import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from api.config import *
from api.instance.config import * #인스턴스로 덮어쓰기