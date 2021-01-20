from flask import Flask
from feature_test import feature_test

app = Flask(__name__)
app.register_blueprint(feature_test, url_prefix='/feature')

if __name__ == '__main__':
    app.run()
