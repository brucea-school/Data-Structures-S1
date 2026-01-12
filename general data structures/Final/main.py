import time

from graph import *
from coolerQueue import *
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pyvis.network import Network
session = requests.session()

session.headers.update({
    'User-Agent': 'wiki map 1.0 (brucea28@gfacademy.org)'
})

q = Queue()
found = {}
graph = Graph()
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", filter_menu=True)
MAX_CALLS = 7
class dummy_class:
    def __init__(self):
        self.status_code = 0

def getLocalLinks(link) -> list:
    soup = None
    urls = []
    chosenOnes = []
    url = 'https://en.wikipedia.org/api/rest_v1/page/html/' + link
    reqs = dummy_class()
    while soup == None and not reqs.status_code == 200:
        reqs = session.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        if not  link == None:
            if "./" in link.get('href'):
                if "#" not in link.get('href') and ":" not in link.get('href'):
                    if link.get('href') in found:
                        chosenOnes.append(link.get('href'))
                    else:
                        urls.append(link.get('href'))

    return urls[0:MAX_CALLS] + chosenOnes

def scanLinksAndUpdateTheFoundDictAndTheGraphAsWell(src:str,links:list[str]):
    print(src)
    if src in found:
        node = found[src]
        node.value = {"src":src,"searched":True}
    else:
        node = Node({"src":src,"searched":True})
        found[src] = node
        graph.add_node(node)


    for i in links:
        if i in found:
            otherNode:Node = found[i]
            if not graph.edge_exists(otherNode,node):
                net.add_edge(otherNode.value["src"],src)
                graph.add_edge(otherNode,node)

        else:
            net.add_node(i)
            otherNode = Node({"src":i,"searched":False})
            found[i] = otherNode
            graph.add_node(otherNode)
            net.add_edge(i,src)
            graph.add_edge(otherNode,node)
            q.enqueue(otherNode)


start = "./Wikipedia"
net.add_node(start)
scanLinksAndUpdateTheFoundDictAndTheGraphAsWell(start, getLocalLinks(start))
for i in range(1,1000):
    time.sleep(0.05)
    toGo:Node = q.dequeue()
    try:
        scanLinksAndUpdateTheFoundDictAndTheGraphAsWell(toGo.value["src"], getLocalLinks(toGo.value["src"]))
    except:
        print("oops!")



for i in graph.get_nodes():
    net.add_node(i.value["src"])

for i in graph.get_nodes():
    for j in i.get_edges():
        net.add_edge(i.value["src"],j.value["src"])
net.show_buttons(filter_=['physics','nodes', 'edges'])
net.toggle_physics(True)
net.show("net.html", notebook=False)