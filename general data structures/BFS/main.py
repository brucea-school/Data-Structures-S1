from graph import *
from queue import *
#im sorry that you had to type all this out
star_systems = ['Aldebaran', 'Alderamin', 'Algol', 'Alioth', 'Aljanah', 'Alkaid', 'Alnair', 'Alnasl', 'Alpha Centauri', 'Altair', 'Ankaa', 'Antares', 'Arcturus', 'Ascella', 'Castor', 'Cor Caroli', 'Deneb', 'Denebola', 'Diphda', 'Fomalhaut', 'Hamal', 'Larawag', 'Markab', 'Menkalinan', 'Menkent', 'Merak', 'Muphrid', 'Musica', 'Nihal', 'Peacock', 'Phecda', 'Pollux', 'Procyon', 'Ran', 'Rasalhague', 'Regulus', 'Sabik', 'Sheratan', 'Sirius', 'Sol', 'Tarazed', 'Tau Ceti', 'Tiaki', 'Vega', 'Zaurak', 'Zosma']

hyperlanes = [['Aldebaran', 'Menkalinan'], ['Aldebaran', 'Pollux'], ['Alderamin', 'Cor Caroli'], ['Alderamin', 'Markab'], ['Alderamin', 'Vega'], ['Algol', 'Menkalinan'], ['Algol', 'Merak'], ['Algol', 'Phecda'], ['Alioth', 'Cor Caroli'], ['Aljanah', 'Markab'], ['Aljanah', 'Tarazed'], ['Alkaid', 'Markab'], ['Alkaid', 'Musica'], ['Alpha Centauri', 'Sol'], ['Alnair', 'Alpha Centauri'], ['Alnair', 'Ankaa'], ['Alnair', 'Muphrid'], ['Alnair', 'Tiaki'], ['Alnasl', 'Sabik'], ['Alnasl', 'Ascella'], ['Altair', 'Arcturus'], ['Altair', 'Fomalhaut'], ['Altair', 'Vega'], ['Ankaa', 'Denebola'], ['Ankaa', 'Sirius'], ['Antares', 'Ascella'], ['Antares', 'Larawag'], ['Arcturus', 'Muphrid'], ['Arcturus', 'Rasalhague'], ['Castor', 'Pollux'], ['Castor', 'Zaurak'], ['Deneb', 'Tarazed'], ['Denebola', 'Zosma'], ['Diphda', 'Fomalhaut'], ['Diphda', 'Hamal'], ['Diphda', 'Tau Ceti'], ['Fomalhaut', 'Sol'], ['Hamal', 'Phecda'], ['Larawag', 'Menkent'], ['Larawag', 'Peacock'], ['Menkent', 'Tiaki'], ['Nihal', 'Regulus'], ["Pollux", "Procyon"], ['Procyon', 'Ran'], ['Ran', 'Sirius'], ['Ran', 'Sol'], ['Ran', 'Tau Ceti'], ['Regulus', 'Zaurak'], ['Regulus', 'Zosma'], ['Sheratan', 'Tau Ceti']]

galaxy = Graph()
for i in star_systems:
    galaxy.add_node(Node(i))

for i in hyperlanes:
    galaxy.add_edge(galaxy.find_node(i[0]),galaxy.find_node(i[1]))

def shortest_path(s1_name, s2_name):
    s1_node = galaxy.find_node(s1_name)
    s2_node = galaxy.find_node(s2_name)
    visited = []
    to_visit = Queue()

    visited.append(s1_node)
    to_visit.enqueue([s1_node])

    while not to_visit.empty():
        scan:list = to_visit.dequeue()
        scan_node:Node = scan[-1]
        print("visiting " + scan_node.get_value())
        for i in scan_node.get_edges():
            if i is s2_node:
                b = scan + [i]
                l = []
                for i in b:
                    l.append(i.get_value())
                return l

            if i not in visited:
                to_visit.enqueue(scan + [i])

        visited.append(scan_node)
def shortest_path_length(s1_name, s2_name):
    return len(shortest_path(s1_name,s2_name))-1

print(shortest_path('Nihal','Deneb'))