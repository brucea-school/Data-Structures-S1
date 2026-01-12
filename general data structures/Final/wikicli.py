import sys
import requests
import colors
import textwrap
import json
from bs4 import BeautifulSoup
session = requests.session()
VERSION = "v0.0.0 BETA"
session.headers.update({
    'User-Agent': 'wiki map 1.0 (brucea28@gfacademy.org)'
})

def getSummary(page):
    return session.get("https://en.wikipedia.org/api/rest_v1/page/summary/"+page)

def formatBasicHtml(html:str) -> str:
    c = html
    c = c.replace("<p>","")
    c = c.replace("</p>", colors.RESET)
    c = c.replace("<b>", colors.BOLD)
    c = c.replace("</b>", colors.RESET)
    c = c.replace("<strong>", colors.BOLD)
    c = c.replace("</strong>", colors.RESET)
    c = c.replace("<i>", colors.ITALIC)
    c = c.replace("</i>", colors.RESET)
    c = c.replace("<em>", colors.ITALIC)
    c = c.replace("</em>", colors.RESET)
    c = c.replace("<mark>", colors.RGBText(255,255,0))
    c = c.replace("</mark>", colors.RESET)
    c = c.replace("<small>", "")
    c = c.replace("</small>", "")
    c = c.replace("<del>", colors.CROSSOUT)
    c = c.replace("</del>", colors.RESET)
    c = c.replace("<ins>", colors.UNDERLINE)
    c = c.replace("</ins>", colors.RESET)
    c = c.replace("<sub>", "")
    c = c.replace("</sub>", "")
    c = c.replace("<sup>", "")
    c = c.replace("</sup>", "")
    c = c.replace("<u>", colors.UNDERLINE)
    c = c.replace("</u>", colors.RESET)
    c = c.replace("<code>", colors.RGBText(100,100,100))
    c = c.replace("</code>", colors.RESET)
    c = c.replace("<kbd>", "")
    c = c.replace("</kbd>", "")
    c = c.replace("<span>", "")
    c = c.replace("</span>", "")
    soup = BeautifulSoup(c, "html.parser")
    return soup.getText(strip=True)


if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        print("WIP")
    else:

        want = getSummary(sys.argv[1])
        if want.status_code == 200:
            content = want.json()
            print(colors.BOLD + content["title"]+colors.RESET)
            print("-"*50)
            print(textwrap.fill(formatBasicHtml( content["extract_html"])))
            imgtxt = session.get(content["thumbnail"]["source"])
            print(imgtxt.text)
        else:
            #failed status
            print(colors.RGBText(255,0,0)+"page "+sys.argv[1]+" not found"+colors.RESET)
else:
    print("WIKI CLI "+VERSION)
    print()
    print("\"wikicli -h\" for help")


