from queue import *
import time

the_big_que = Queue()
tick = 0
desierd_custom = int(input("how many customers"))
people_added_and_that_cool_stuff = 0

desierd_custom -= 1
people_added_and_that_cool_stuff += 1
the_big_que.enqueue("customer "+str(people_added_and_that_cool_stuff))

while desierd_custom > 0 or (not the_big_que.empty()):
    time.sleep(0.1)
    tick += 1
    if tick%5 == 0:
        if desierd_custom > 0:
            desierd_custom -= 1
            people_added_and_that_cool_stuff += 1
            the_big_que.enqueue("customer "+str(people_added_and_that_cool_stuff))

    if tick%12 == 0:
        print("Cashier 1 served "+the_big_que.dequeue())

    if tick%19 == 0:
        print("Cashier 2 served "+the_big_que.dequeue())

    if tick%25 == 0:
        print("Cashier 3 served "+the_big_que.dequeue())

print("it took "+str(tick)+" ticks to serve all people")