
class Stack:
    def __init__(self):
        self.items = []

    def push(self,a:any):
        self.items.append(a)

    def pop(self):
        return self.items.pop(len(self.items)-1)

    def empty(self) -> bool:
        return len(self.items) == 0

    def bottem(self):
        otherStack = Stack()

        while not self.empty():
            otherStack.push(self.pop())

        b = otherStack.pop()
        self.push(b)

        while not otherStack.empty():
            self.push(otherStack.pop())

        return b

    def top(self):
        b = self.pop()
        self.push(b)
        return b

    def size(self)->int:
        return len(self.items)

    def contains(self, item) -> bool:
        otherStack = Stack()

        if self.top() == item:
            return True

        while (not self.empty()) and (not self.top() == item):
            otherStack.push(self.pop())


        if (not self.empty()) and self.top() == item:
            while not otherStack.empty():
                self.push(otherStack.pop())
            return True
        else:
            while not otherStack.empty():
                self.push(otherStack.pop())

            return False
