import hashlib
import threading

def hash(message):
    message_bytes = message.encode('utf-8')
    h = hashlib.sha512()
    h.update(message_bytes)
    return h.hexdigest()

tgt = "92938b5423a1793d836333694cf0e55d92b42fb0c14ffcfe8349b51e86bceedcf9631398c31e1afdf114936502ca95577fa9014c26d718e77a235eb889ed56f3"
thrds = []
ROOF = 20

def check(intake):
    if hash(intake) == tgt:
        print("VALID-"+intake)
        exit(0)
    else:
        print("invalid")
def scan(add:str,dep:int,start=False):

    if dep == 0:
        for i in range(33, 126):
            check(add+chr(i))
    else:
        rt = []
        for i in range(33, 126):
            thr = threading.Thread(target=scan, args=(add+chr(i),dep-1))
            rt.append(thr)
        for t in rt:
            t.start()

    if start:
        if dep == ROOF:
            return
        else:
            scan("",dep+1,start=True)

def test():
    for i in range(33, 126):
        print(chr(i))

scan("",0,start=True)