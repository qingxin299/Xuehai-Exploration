from flask import *
app = Flask(__name__)

@app.route("/check.xh")
def check():
    return "xh"

app.run(host='192.168.16.102',port=80)