import base64
import sys


def RGBText(R:int,G:int,B:int) -> str:
    return "\033[38;2;"+str(R)+";"+str(G)+";"+str(B)+"m"

def RGBBackGround(R:int,G:int,B:int) -> str:
    return "\033[48;2;"+str(R)+";"+str(G)+";"+str(B)+"m"

def textToRGBText(text:str,R:int,G:int,B:int,bold=False,italic=False,underline=False,crossout=False) -> str:
    header = RESET
    if bold:
        header += BOLD
    if italic:
        header += ITALIC
    if underline:
        header += UNDERLINE
    if crossout:
        header += CROSSOUT

    return header + RGBText(R,G,B) + text + RESET


def textToRGBBackGround(text: str, R: int, G: int, B: int, bold=False, italic=False, underline=False, crossout=False) -> str:
    header = RESET
    if bold:
        header += BOLD
    if italic:
        header += ITALIC
    if underline:
        header += UNDERLINE
    if crossout:
        header += CROSSOUT

    return header + RGBBackGround(R, G, B) + text + RESET


RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
CROSSOUT = "\033[9m"

def ct():
    for r in range(0,64):
        for g in range(0,64):
            for b in range(0,64):
                print(RGBText((63-r)*4,(63-g)*4,(63-b)*4), end="")
                print(RGBBackGround(r * 4, g * 4, b * 4) + "◼︎" + RESET, end="")

            print(RESET+CROSSOUT+"crossout"+RESET+BOLD+" bold "+RESET+ITALIC+"italic "+RESET+UNDERLINE+"unerline"+RESET)


