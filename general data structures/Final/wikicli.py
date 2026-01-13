import sys
import requests
import colors
import textwrap
import os
import json
from bs4 import BeautifulSoup
import pyfiglet
import shutil



session = requests.session()
VERSION = "v0.0.0 BETA"
session.headers.update({
    'User-Agent': 'wiki map 1.0 (brucea28@gfacademy.org)'
})

def get_width():
    try:
        # Get the terminal size
        size = shutil.get_terminal_size()
        return size.columns
    except OSError:
        # Provide a default width if running in an environment without a terminal
        return 80

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

    for bold in soup.find_all("b"):
        bold.replace_with(colors.BOLD+bold.text+colors.RESET)

    if page is not None:
        for text in soup.find_all("p"):
            print(text.text+"\n")

    return soup.getText(strip=True)


if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        print("WIKI CLI "+VERSION)
        print("a wikipedia in the command line")
        print()
        print("usage:")
        print("wikicli <page>       quick summary of a page")
        print("wikicli -l <page>    trys to replicate the page to the terminal")
    else:
        long = False
        if (sys.argv[1] == "-l"):
            if (len(sys.argv)>2):
                want = getSummary(sys.argv[2])
                long = True
            else:
                print(colors.textToRGBText("for what page???",255,0,0))
                sys.exit(0)

        else:
            want = getSummary(sys.argv[1])

        if want.status_code == 200:
            content = want.json()
            result = pyfiglet.figlet_format(content["title"])
            print(colors.BOLD+result)
            print("-"*get_width())
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


