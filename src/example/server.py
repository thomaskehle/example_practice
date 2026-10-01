from flask import Flask

app = Flask(__name__)


#import os

#names = [os.environ["FIRST_NAME_IN_LIST"]]

@app.route("/")
def hello_world():
    #for name in names:
    return "<p>Hello, World! Does this auto-deploy? Test1? </p>\n" 
    #return thing
