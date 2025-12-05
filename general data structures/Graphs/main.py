
from graph import *
n1 = Node("o")
assert n1.get_value() == "o"
assert n1.get_edges() == []
n1.set_value("c")
assert n1.get_value() == "c"
assert n1.get_edges() == []
n2 = Node("o")
n3 = Node("m")
n4 = Node("p")
print("Node class works as intended.")

g = Graph()
assert g.get_nodes() == []
g.add_node(n1)
assert g.get_nodes() == [n1]
g.add_node(n2)
g.add_node(n3)
assert n1 in g.get_nodes()
assert n2 in g.get_nodes()
assert n3 in g.get_nodes()
g.add_edge(n1, n2)
g.add_edge(n1, n3)
assert n2 in n1.get_edges()
assert n3 in n1.get_edges()
assert n1 in n2.get_edges()
assert n1 in n3.get_edges()
assert n1 not in n1.get_edges()
assert n2 not in n2.get_edges()
assert n3 not in n3.get_edges()
assert n2 not in n3.get_edges()
assert n3 not in n2.get_edges()
print("add_node, get_nodes, and add_edge work as intended.")


assert g.edge_exists(n1, n2)
assert g.edge_exists(n1, n3)
assert not g.edge_exists(n2, n3)
print("edge_exists works as intended.")

g.add_edge(n2, n3)
edge_error_raised = False
try:
    g.add_edge(n2, n3)
except:
    edge_error_raised = True
assert edge_error_raised
g.add_node(n4)
node_error_raised = False
try:
    g.add_node(n1)
except:
    node_error_raised = True
assert node_error_raised
print("Error raising works as intended.")
