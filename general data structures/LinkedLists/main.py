from linkedlist import *
n1 = Node("c")
n2 = Node("o")
n3 = Node("m")
n4 = Node("p")
assert n1.get_value() == "c"
n1.set_next(n2)
n2.set_next(n4)
n3.set_next(n4)
n2.set_next(n3)
assert n1.get_next().get_value() == "o"
assert n1.get_next().get_next().get_value() == "m"
assert n1.get_next().get_next().get_next().get_next() == None
n = n1
comp = ""
for i in range(4):
    comp += n.get_value()
    n = n.get_next()
print("comp is " + comp)
assert comp == "comp"

l1 = LinkedList()
l1.insert_at_start("a")
assert l1.head.get_value() == "a"
assert l1.tail.get_value() == "a"
l1.insert_at_start("b")
assert l1.head.get_value() == "b"
assert l1.tail.get_value() == "a"
assert l1.head.get_next().get_value() == "a"
l1.insert_at_start("c")
assert l1.head.get_value() == "c"
assert l1.tail.get_value() == "a"
assert l1.head.get_next().get_value() == "b"
assert l1.head.get_next().get_next().get_value() == "a"
print("insert_at_start() works as intended.")
l2 = LinkedList()
l2.insert_at_end("a")
assert l2.head.get_value() == "a"
assert l2.tail.get_value() == "a"
l2.insert_at_end("b")
assert l2.head.get_value() == "a"
assert l2.tail.get_value() == "b"
assert l2.head.get_next().get_value() == "b"
l2.insert_at_end("c")
assert l2.head.get_value() == "a"
assert l2.tail.get_value() == "c"
assert l2.head.get_next().get_value() == "b"
assert l2.head.get_next().get_next().get_value() == "c"
print("insert_at_end() works as intended.")

l3 = LinkedList()
l3.insert_at_start("a")
l3.insert_at_start("b")
l3.insert_at_start("c")
assert not l3.empty()
l3.delete_at_start()
assert l3.head.get_value() == "b"
assert l3.tail.get_value() == "a"
l3.delete_at_start()
l3.delete_at_start()
assert not l3.head
assert not l3.tail
assert l3.empty()
print("delete_at_start(), empty() work as intended.")

