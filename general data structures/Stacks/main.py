from stack import *
s = Stack()
w = "computers"
for c in w:
    s.push(c)
assert s.pop() == "s"
assert s.pop() == "r"
s.push("r")
print("push() and pop() seem to be working as intended.")

assert not s.empty()
assert Stack().empty()
assert s.top() == w[-2]
assert s.top() == w[-2] # If this fails, top() doesn’t restore stack before returning
print("empty() and top() seem to be working as intended.")

assert s.size() == 8
assert s.contains("o")
assert not s.contains("x")
print("size() and contains() seem to be working as intended.")
