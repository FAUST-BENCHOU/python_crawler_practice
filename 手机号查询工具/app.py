import requests
from lxml import etree
from flask import Flask, render_template, request

app = Flask(__name__)


def get_mobile(phone):
    url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    e = etree.HTML(resp.text)
    datas = e.xpath('//*[@class="table"]//tbody/tr/td[2]//a/text()')
    return datas


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_phone')
def search_phone():
    phone = request.args.get('phone')
    data = get_mobile(phone)
    return '<br/>'.join(data)


app.run(debug=True)
