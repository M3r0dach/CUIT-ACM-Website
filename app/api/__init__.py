from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api/v1.0')

from auth import *
from user import *