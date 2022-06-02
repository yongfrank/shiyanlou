#! /opt/homebrew/bin/python3

import requests
import lxml
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}


response = requests.get("https://baidu.com", headers = headers)

et_html = etree.HTML(response.content.decode("utf-8"))
# print(response.content)
# print(et_html)

et_target = et_html.xpath("//html/body/div[1]/div[2]/div[2]/a")


for a in et_target:
    print(a.get("href"))


print("hello, world!")



# with open("baidu.txt","wt") as f:
#    #f.write(str(response.content))
#    #print("success")
