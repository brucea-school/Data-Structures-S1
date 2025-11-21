from binarytree import *
n1 = Node("c")
assert n1.get_value() == "c"
assert n1.get_left() == None
assert n1.get_right() == None

n1.set_left(Node("o"))
assert n1.get_value() == "c"
assert n1.get_left().get_value() == "o"
assert n1.get_right() == None
assert n1.get_left().get_left() == None

n1.get_left().set_left(Node("m"))

n1.get_left().set_right(Node("u"))
assert n1.get_left().get_right().get_value() == "u"
assert n1.get_left().get_left().get_value() == "m"

n1.get_left().get_right().set_value("p")
assert n1.get_left().get_right().get_value() == "p"

n1.set_right(Node("u"))
n1.get_right().set_left(Node("t"))
n1.get_right().set_right(Node("e"))
n1.get_left().get_right().set_left(Node("r"))

assert n1.is_leaf() == False
assert n1.get_right().is_leaf() == False
assert n1.get_left().get_left().is_leaf() == True
assert n1.get_left().get_right().is_leaf() == False
assert n1.get_left().get_right().get_left().is_leaf() == True

print("Node works as intended.")


t1 = BinaryTree(n1)
assert t1.get_root().get_value() == "c"
assert t1.get_root() == n1

computer = ""
computer += t1.get_root().get_value()
computer += t1.get_root().get_left().get_value()
computer += t1.get_root().get_left().get_left().get_value()
computer += t1.get_root().get_left().get_right().get_value()
computer += t1.get_root().get_right().get_value()
computer += t1.get_root().get_right().get_left().get_value()
computer += t1.get_root().get_right().get_right().get_value()
computer += t1.get_root().get_left().get_right().get_left().get_value()

print(computer + " is computer")
assert computer == "computer"

print("BinaryTree basic methods work as intended.")
