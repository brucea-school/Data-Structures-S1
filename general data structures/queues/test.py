
from queue import *
s = Queue()
w = "computer"
for c in w:
    s.enqueue(c)
assert s.look() == w[0]
new_w = ""
assert not s.empty()
assert s.size() == 8
for i in range(s.size()):
    new_w += s.dequeue()
assert s.empty()
print(w + " is " + new_w)
assert w == new_w
print("Basic queue methods seem to be working as intended.")
for c in w:
    s.enqueue(c)
assert s.contains("t")
assert not s.contains("x")
print("contains() seems to be working as intended.")
print(s)
s2 = Queue()
for c in "science":
    s2.enqueue(c)
s3 = s + s2
print(s3) # should be a queue containing all the letters in “computerscience”
print(repr(s3))