from app import app


@app.route('/')
def index():
  return '<h1>Application</h1>'

@app.route('/home')
def home():
  return '<h1>Home</h1>'