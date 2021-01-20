from flask import Flask

app = Flask(__name__, static_url_path='/static', static_folder='./static')


@app.route('/test')
def images():
    outStr="""
    <link href="/static/css/mycss.css" rel="stylesheet" type="text/css">

    
    <div class="test">
        this is a book
    </div>
    """
    '<img src="/static/google.png">'

    return outStr

if __name__ == '__main__':
    app.run()
# debug=True, host='127.0.0.1', port=5001
