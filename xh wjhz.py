from flask import *
app = Flask(__name__)

@app.route("/box/file")
def box():
    return send_file("ppt.7z")


app.run(host='192.168.16.102',port=8080)