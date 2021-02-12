from flask import Flask, render_template, request
from random import choice
import json
app = Flask(__name__)


@app.route('/')
def index():
    send = {"status":"error","error":"404"}
	return "hi"
@app.route('/send')
def send():
    info = request.args.get('info')
    f=open("info.txt", "a+")
    f.write(f"{info} -end + begin-")
    f.close()
    return "<link rel=\"stylesheet\" type=\"text/css\" href=\"https://grovegazette.ml/style.css\"><p>You can close this page.</p><title>loading</title><script>window.onload = window.close();</script>"
app.run(host='0.0.0.0', port=8080)