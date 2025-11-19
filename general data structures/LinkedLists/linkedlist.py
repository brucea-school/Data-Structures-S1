
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

    def empty(self) -> bool:
        return self.head is None

    def delete_at_start(self):
        if self.head is self.tail:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next

        self.length -= 1

    def __getitem__(self, ind):
        index = ind
        it = self.head
        while index > 0:
            index -= 1
            it = it.get_next()
        return it.get_value()

    def get_node(self, ind) -> Node:
        index = ind
        it = self.head
        while index > 0:
            index -= 1
            it = it.get_next()
        return it

    def insert(self, ind, value):
        self.length += 1

        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if ind == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return


        index = ind-1
        it:Node = self.head
        while index > 0:
            index -= 1
            it = it.get_next()
            if it is None:
                break


        if it is None:
            self.tail.set_next(new_node)
            self.tail = new_node
            return

        if it.get_next() is None:
            it.set_next(new_node)
            return

        new_node.set_next(it.get_next())
        it.set_next(new_node)


    def delete_at_end(self):
        if self.head is self.tail:
            self.head =None
            self.tail =None
            return

        b = self.get_node(self.__len__()-2)
        b.set_next(None)
        self.tail = b
        self.length -= 1

    def delete(self,ind):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return

        if ind == 0:
            self.head = self.head.get_next()
            return

        if self.get_node(ind) is self.tail:
            self.get_node(ind - 1).set_next(None)
            self.tail = self.get_node(ind-1)
            return
        self.get_node(ind-1).set_next(self.get_node(ind+1))

    def __contains__(self, item):
        i = 0
        while i<self.length:
            if self.__getitem__(i) == item:
                return True
            i += 1

        return False

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
