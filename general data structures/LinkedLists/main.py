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

l4 = LinkedList()
assert len(l4) == 0
l4.insert_at_start("a")
assert len(l4) == 1
l4.insert_at_end("b")
assert len(l4) == 2
l4.delete_at_start()
assert len(l4) == 1
print("__len__() works as intended.")
c = LinkedList()

c.insert_at_end("c")
c.insert_at_end("o")
c.insert_at_end("m")
c.insert_at_end("p")
c.insert_at_end("u")
c.insert_at_end("t")
c.insert_at_end("e")
c.insert_at_end("r")
assert c[0] == "c"
assert c[7] == "r"
put = ""
for i in range(3, 6):
    put += c[i]
print("put is " + put)
assert put == "put"
print("__getitem__() works as intended.")
b = LinkedList()
b.insert(0, "m")
b.insert(0, "o")
b.insert(2, "u")
b.insert(3, "r")
b.insert(0, "c")
b.insert(4, "e")
b.insert(3, "p")
b.insert(5, "t")
assert not b.empty()
assert len(b) == 8

computer = ""
for i in range(8):
    computer += b[i]
print("computer is " + computer)

print("insert() works as intended.")

b.insert(8, "s")
b.delete_at_end()
computer = ""
for i in range(8):
    computer += b[i]
assert computer == "computer"
a = LinkedList()
a.insert(0, "q")
a.insert(1, "u")
a.delete_at_end()
assert a.head == a.tail
a.delete_at_end()
assert a.head == None
assert a.tail == None

print("delete_at_end() works as intended.")

b.delete(6)
b.delete(6)
b.delete(0)
b.delete(1)
b.delete(1)
assert len(b) == 3

out = ""
for i in range(3):
    out += b[i]
print("out is " + out)
assert out == "out"
print("delete() works as intended.")



