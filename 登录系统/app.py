import requests
from lxml import etree
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return "主页"

app.run(debug=True)
