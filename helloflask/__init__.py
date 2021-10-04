from flask import Flask, g, request, Response, make_response
from datetime import date, datetime
from flask.helpers import make_response

app = Flask(__name__)   # 앱 만들기 !
app.debug = True

@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    return make_response(res)

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)

@app.route('/rp')
def rp():
    q = request.args.get('q')
    return "q= %s" % str(q)

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),
                   ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test':'ttt'})
    return make_response(custom_res)

# @app.before_request     # request 요청을 처리하기 전에 너가 한 번 실행해줘 !
# def before_request():
#     print("before_request!!!")
#     g.str = "한글"  # application context 영역 = 다른 사람들도 볼 수 있는 ! (session context 영역 = 나만 볼 수 있는 영역)

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g, 'str', '111')

# URI를 정의하는 놈 = Route
@app.route("/")
def helloworld():
    return "Hello Flask World!"