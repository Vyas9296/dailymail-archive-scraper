#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pprint import pprint

import os
from lxml import html,etree,cssselect
import urllib
import requests

import time

import csv
from datetime import datetime
import requests

from datetime import date, timedelta

def main():
    articles=generate_urls()

def generate_urls():
    main_url="http://www.dailymail.co.uk/home/sitemaparchive/"
    d1 = date(1994,1,1)  # start date
    d2 = date.today()  # end date - Today's date
    delta = d2 - d1         # timedelta
    print str(delta) + " days of news to be collected"
    articles=[]
    for i in range(delta.days + 1):
        day=(d1 + timedelta(i)).strftime('%Y%m%d')
        print(day)
        url=main_url + "day_" + day + ".html"
        r=requests.get(url,timeout=30)
        time.sleep(3)
        html_tree=html.fromstring(r.text)
        article_links = html_tree.xpath('//ul[@class="archive-articles debate link-box"]/*/a/@href')
        for article in article_links:
            d={}
            d['date']=day
            d['url']=article
            articles.append(d)
    return articles


if __name__ == '__main__':
    main()
