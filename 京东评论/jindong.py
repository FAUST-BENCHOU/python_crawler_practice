import openpyxl
import pandas as pd
import os
import time
import json
import random
import csv
import re
import jieba
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 评论数据保存文件
COMMENT_FILE_PATH = 'jd_comment.txt'
# 词云字体
WC_FONT_PATH = 'C:\Windows\Fonts\FZSTK.TTF'

def batch_spider_comment():
    """
        批量爬取某东评价
        """
    for i in range(1,200):
        header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105'}
        url=f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1701175611119&loginType=3&uuid=122270672.1701166171208912969799.1701166171.1701166171.1701175526.2&productId=100009464799&score=0&sortType=5&page={i}&pageSize=10&isShadowSku=0&fold=1&bbtf=1&shield='
        response= requests.get(url=url,headers=header)
        json=response.json()
        data=json['comments']
        for t in data:
            content =t['content']
            with open(COMMENT_FILE_PATH, 'a+', encoding='utf-8') as file:
                file.write(content + '\n')

def cut_word():
    """
    对数据分词
    :return: 分词后的数据
    """
    with open(COMMENT_FILE_PATH, encoding="utf8") as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=False)#精确模式
        wl = " ".join(wordlist)
        return wl

def create_word_cloud():
    """44144127306
    生成词云
    :return:
    """

    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=2000, scale=4,
                   max_font_size=50, random_state=42, font_path=WC_FONT_PATH)
    # 生成词云
    wc.generate(cut_word())
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    wc.to_file("jd_ciyun.jpg")


def txt_change_to_csv():
    with open('jd_comment.csv', 'w+', encoding="utf8", newline='')as c:
        writer_csv = csv.writer(c, dialect="excel")
        with open("jd_comment.txt", 'r', encoding='utf8')as f:
            # print(f.readlines())
            for line in f.readlines():
                # 去掉str左右端的空格并以空格分割成list
                line_list = line.strip('\n').split(',')
                writer_csv.writerow(line_list)

if __name__ == '__main__':
    # 爬取数据
    batch_spider_comment()

    #转换数据
    txt_change_to_csv()

    # 生成词云
    create_word_cloud()