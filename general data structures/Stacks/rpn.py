from stack import *

class Rpn:
    def __init__(self):
        self.stack = Stack()

    def add(self,num:float):
        self.stack.push(num)

    def calc(self,oper:str) -> str:
        b = 0
        if self.stack.empty():
            return '\033[31m'+"theres NOTHING on the stack"+'\033[0m'
        else:
            b = self.stack.pop()
            if self.stack.empty():
                self.stack.push(b)
                return '\033[31m'+"you need more stuff on the stack"+"\033[0m"


        if oper == "+":
            self.stack.push(self.stack.pop()+b)
            return self.stack.top()
        elif oper == "-":
            self.stack.push(self.stack.pop() - b)
            return self.stack.top()
        elif oper == "*":
            self.stack.push(self.stack.pop() * b)
            return self.stack.top()
        elif oper == "/":
            self.stack.push(self.stack.pop() + b)
            return self.stack.top()
        else:
            self.stack.push(b)
            return '\033[31m'+"no clue what that means"+"\033[0m"



print("type exit to exit")
the_stack = Rpn()

intake = ""
while intake != "exit":
    intake = input(">")
    if intake.isnumeric():
        the_stack.add(float(intake))
    else:
        print(the_stack.calc(intake))
