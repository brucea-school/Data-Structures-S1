
class Node:
    def __init__(self,val):
        self.value = val
        self.next = None


    def get_value(self):
        return self.value

    def set_next(self, n):
        self.next = n

    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def insert_at_start(self,val):
        b = Node(val)
        b.set_next(self.head)
        self.head = b
        if self.tail is None:
            self.tail = b
        self.length += 1

    def insert_at_end(self,val):
        b = Node(val)
        if self.tail is None:
            self.tail = b
            self.head = b
        else:
            self.tail.set_next(b)
            self.tail = b

        self.length += 1

    def empty(self):
        return self.head is None

    def delete_at_start(self):
        if self.head is self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next

        self.length -= 1
    def __str__(self):
        s = "["
        n = self.head
        while n != None:
            if type(n.get_value()) == str:
                s += '"' + n.get_value() + '", '
            else:
                s += str(n.get_value()) + ", "
            n = n.get_next()
        if s != "[":
            s = s[:-2]
        s = s + "]"
        return s
