

def yes_or_no() -> bool:
    intake = input().lower()
    if intake == "yes":
        return True
    elif intake == "no":
        return False
    else:
        print("Please enter yes or no.")
        return yes_or_no()
class Node:
    def __init__(self, val = None, s = None):
        self.left_child = None
        self.right_child = None
        if s == None:
            self.value = val
        else:
            interior = s[1:-1]
            if "{" not in interior:
                self.value = interior
            else:
                b = interior.index("{")
                child = interior[b:]
                if interior[b - 8:b] == ", Left: ":
                    self.value = interior[:b - 8]
                    num_brackets = 0
                    for i in range(len(child)):
                        if child[i] == "{":
                            num_brackets += 1
                        elif child[i] == "}":
                            num_brackets -= 1
                            if num_brackets == 0:
                                break
                    self.left_child = Node(s = child[:i + 1])
                    interior = child[i + 1:]
                    if interior == "":
                        return
                    else:
                        self.right_child = Node(s = interior[9:])
                else:
                    self.value = interior[:b - 9]
                    self.right_child = Node(s = interior[b:])


    def set_left(self, n):
        self.left_child = n

    def set_right(self, n):
        self.right_child = n

    def set_value(self, val):
        self.value = val

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_value(self):
        return self.value

    def is_leaf(self):
        return (self.left_child is None) and (self.right_child is None)

    def __str__(self):
        s = "{" + str(self.get_value())
        if self.get_left() != None:
            s = s + ", Left: " +  str(self.get_left())
        if self.get_right() != None:
            s = s + ", Right: " +  str(self.get_right())
        s = s + "}"
        return s

class BinaryTree:
    def __init__(self, n = None, s = None):
        if s is None:
            self.root = n
        else:
            self.root = Node(s=s[6:])

    def get_root(self) -> Node:
        return self.root

    def play_game(self,tgt=None):
        if tgt is None:
            return self.play_game(tgt=self.get_root())
        else:

            if tgt.is_leaf():
                print("I know! its a: "+tgt.get_value())

                print("am I right?")
                if not yes_or_no():
                    print("aww... What were you thinking of?")
                    anwser = input()
                    print("What question could I have asked before guessing to help me tell the difference?")
                    question = input()
                    print("Would you have answered yes or no to that question?")
                    if yes_or_no():
                        tgt.set_right(Node(tgt.get_value()))
                        tgt.set_value(question)
                        tgt.set_left(Node(anwser))
                    else:
                        tgt.set_left(Node(tgt.get_value()))
                        tgt.set_value(question)
                        tgt.set_right(Node(anwser))

                print("play again?")
                if yes_or_no():
                    return self.play_game()
                else:
                    print("bye bye")
                    print("do you want to save your tree?")
                    if yes_or_no():
                        fw = open("saved_tree.txt", "w")
                        fw.write(str(self))
                        fw.close()

                        return
                    else:
                        return

            print(tgt.get_value())
            if yes_or_no():
                return self.play_game(tgt=tgt.get_left())
            else:
                return self.play_game(tgt=tgt.get_right())



    def __str__(self):
        return "Tree: " + str(self.get_root())



