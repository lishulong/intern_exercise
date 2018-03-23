import refheap
import random

if __name__ == '__main__':
    
    A = []
    for i in range(1, 100, 1):
        A.append(random.uniform(1, 10000))

    # create an instance  
    rf = refheap.RefHeap(A)

    # return the minimal object,but doesn't remove it
    print rf.get()

    # remove 100 
    # print rf.remove(100)

    # return the minimal object,and remove it
    print rf.pop()
    print rf.get()

    # push an object into a heap
    rf.push(1)

    print rf.get()

    # push all item and return them in a list
    B = rf.pop_all()
    print B
