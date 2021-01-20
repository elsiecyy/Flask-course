from flask import Flask, request

app = Flask(__name__)


@app.route('/hello/Allen')  # 此接口名稱自行定義。使用者來訪問的接口
def hello():
    return 'Hello Allen！'


@app.route('/hello/Jen')
def hello2():
    return 'Hello Jen！'


@app.route('/hello/<username>')
def hello_username(username):
    return 'Hello %s！' % (username)


@app.route('/hello/<username>/<age>')  # 把參數給裝飾器。可定義多個參數
def querytest(username, age):
    outStr = 'Hello %s！,You are %s years old.' % (username, age)
    return outStr


# @app.route('/query')
# def query_par():
#     username = request.args.get('username')
#     age = request.args.get('age')
#     outStr='Hello %s! , you are %s years old.'%(username,age)
#     return outStr

@app.route('/query')   #此為用'?'帶參數
def query_par():
    username = request.args.get('username')
    age = request.args.get('age')
    if username == None:
        return 'What is your name?'
    if age == None:
        outStr = '<h1>Hello %s.</h1>' % (username)
        return outStr
    outStr = '<h1>Hello %s!  , you are %s years old.</h1>' % (username, age)
    return outStr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
