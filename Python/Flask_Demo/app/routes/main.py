from flask import Blueprint


bp = Blueprint('', __name__)

@bp.route('/')
def index():
  return '<h1>Application</h1>'

@bp.route('/home')
def home():
  return '<h1>Home</h1>'