from flask import Blueprint

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/item/<int:id>')
def item(id):
  return f'<h1>Application</h1><h2>Item {id}</h2>'