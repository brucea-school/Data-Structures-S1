list_of_stuff = []
for i in range(0,5):
    b = input("Name:").split()
    list_of_stuff.append(b[len(b)-1])

list_of_stuff.sort()
print(list_of_stuff)