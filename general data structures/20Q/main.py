from binarytree import *

fa = open("saved_tree.txt", "a") # This creates the file if it
fa.close() 				 # doesn’t exist yet
fr = open("saved_tree.txt", "r")
old_tree = fr.read() # This is the string representing the old tree
fr.close()

print("would you like to paly with the old tree?")
if yes_or_no():
    game_tree = BinaryTree(Node("dose it have 4 legs"))
    game_tree.get_root().set_left(Node("dose it have pointy ears?"))
    game_tree.get_root().get_left().set_left(Node("cat"))
    game_tree.get_root().get_left().set_right(Node("dog"))

    game_tree.get_root().set_right(Node("can it swim?"))
    game_tree.get_root().get_right().set_left(Node("fish"))
    game_tree.get_root().get_right().set_right(Node("parrot"))
else:
    game_tree = BinaryTree(old_tree)


game_tree.play_game()
