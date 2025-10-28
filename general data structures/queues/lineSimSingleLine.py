from queue import *
import time

the_big_que1 = Queue()
the_big_que2 = Queue()
the_big_que3 = Queue()
tick = 0
desierd_custom = int(input("how many customers"))
people_added_and_that_cool_stuff = 0

desierd_custom -= 1
people_added_and_that_cool_stuff += 1
the_big_que1.enqueue("customer "+str(people_added_and_that_cool_stuff))

while desierd_custom > 0 or (not the_big_que2.empty()) or (not the_big_que3.empty()) or (not the_big_que1.empty()):
    time.sleep(0)
    tick += 1
    if tick%5 == 0:
        if desierd_custom > 0:
            if the_big_que1.size() <= the_big_que2.size() and the_big_que1.size() <= the_big_que3.size():
                desierd_custom -= 1
                people_added_and_that_cool_stuff += 1
                the_big_que1.enqueue("customer "+str(people_added_and_that_cool_stuff))
            elif the_big_que2.size() <= the_big_que1.size() and the_big_que2.size() <= the_big_que3.size():
                desierd_custom -= 1
                people_added_and_that_cool_stuff += 1
                the_big_que2.enqueue("customer "+str(people_added_and_that_cool_stuff))
            else:
                desierd_custom -= 1
                people_added_and_that_cool_stuff += 1
                the_big_que3.enqueue("customer " + str(people_added_and_that_cool_stuff))

    if tick%12 == 0:
        if not the_big_que1.empty():
            print("Cashier 1 served "+the_big_que1.dequeue())

    if tick%19 == 0:
        if not the_big_que2.empty():
            print("Cashier 2 served "+the_big_que2.dequeue())

    if tick%25 == 0:
        if not the_big_que3.empty():
            print("Cashier 3 served "+the_big_que3.dequeue())

print("it took "+str(tick)+" ticks to serve all people")