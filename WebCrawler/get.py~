import requests
from lxml import etree

response = requests.get("http://localhost:8080/oeasyorg/index.html")

s_html = response.content.decode("utf-8")
et_html = etree.HTML(s_html)
et_target = et_html.xpath("/html/body/header/nav/ul/li/a") 

with open("urls.txt","wt") as f:
    for element in et_target:
        print(element.text)
        attributes = element.attrib
        print(attributes["href"])
        f.write("http://oeasy.org" + attributes["href"][1:] + "\n")

print(attributes)
