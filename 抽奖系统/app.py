from flask import Flask, render_template
from random import randint
import requests
from lxml import etree

app = Flask(__name__)


url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
resp = requests.get(url, headers=headers)
e = etree.HTML(resp.text)

hero = e.xpath('//table[@class="players_table"]//tr//td[2]//a//text()')

@app.route('/index')
def index():
    return render_template('index.html', hero=hero)


@app.route('/choujiang')
def choujiang():
    num = randint(0, len(hero) - 1)
    return render_template('index.html', hero=hero, h=hero[num])


app.run(debug=True)
