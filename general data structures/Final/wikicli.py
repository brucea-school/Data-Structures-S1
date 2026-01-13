import sys
import requests
import colors
import textwrap
import os
import json
from bs4 import BeautifulSoup
session = requests.session()
VERSION = "v0.0.0 BETA"
session.headers.update({
    'User-Agent': 'wiki map 1.0 (brucea28@gfacademy.org)'
})

def getSummary(page):
    return session.get("https://en.wikipedia.org/api/rest_v1/page/summary/"+page)

def formatBasicHtml(html:str,page:str=None) -> str:
    c = html

    soup = BeautifulSoup(c, "html.parser")
    for link in soup.find_all("a"):
        if page is not None:
            if "./" in link.get('href'):
                link.replace_with(colors.link("https://en.wikipedia.org/wiki/"+link.get('href'),link.getText(strip=True)))
            elif "#" in link.get('href'):
                link.replace_with(colors.link("https://en.wikipedia.org/wiki/"+page+link.get('href'), link.getText(strip=True)))
            else:
                link.replace_with(colors.link(link.get('href'), link.getText(strip=True)))
        else:
            link.replace_with(colors.link(link.get('href'), link.getText(strip=True)))
    if page is not None:
        for text in soup.find_all("p"):
            print(text.text+"\n")

    return soup.getText(strip=True)


if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        print("WIP")
    else:
        long = False
        if (len(sys.argv)>2 and sys.argv[1] == "-l"):
            want = getSummary(sys.argv[2])
            long = True
        else:
            want = getSummary(sys.argv[1])

        if want.status_code == 200:
            content = want.json()
            print(colors.BOLD  + content["title"])
            print("-"*50)
            print(colors.RESET +textwrap.fill(formatBasicHtml( content["extract_html"])))
            print(colors.link(content["content_urls"]["desktop"]["page"],"see on Wikipedia"))
            if long:
                l = session.get("https://en.wikipedia.org/api/rest_v1/page/html/" + sys.argv[2])
                formatBasicHtml(l.text,content["title"])



        else:
            #failed status
            print(colors.RGBText(255,0,0)+"page "+sys.argv[1]+" not found"+colors.RESET)
else:
    print("WIKI CLI "+VERSION)
    print()
    print("\"wikicli -h\" for help")


