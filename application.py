from flask import Flask
from flask import request, url_for

app = Flask (__name__, static_url_path='/static')

@app.route('/')
def index():
    return '<h3>Hello Masha!</h3>'

def parseop(input_string):
  formula = input_string [1:]
  oper, remainder = formula.split (':', 1)
  lh, rh = remainder.split (',', 1)
  return (oper, float (lh), float (rh))

def execop (oper, lh, rh):
    if oper == 'add':
        return lh + rh
    elif oper == 'sub':
        return lh - rh
    elif oper == 'mult':
        return lh * rh
    elif oper == 'div':
        return lh / rh
    else:
        return math.nan

@app.route('/calc')
def calc():
    op = request.args.get('op')
    lh = float (request.args.get('lh')) 
    rh = float (request.args.get('rh'))
    res = execop (op, lh, rh)
    return '<h3>Calculator</h3>%s %s %s = %s' % (lh, op, rh, res)

@app.route('/bye')
def bye():
    return '<a href="/">Bye Masha!</a><img src="%s">' % url_for('static', filename='MariaParfenova.jpg')
