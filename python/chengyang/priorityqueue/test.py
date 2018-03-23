from pykit import priorityqueue 


if __name__ == '__main__':

    pq = priorityqueue.PriorityQueue()

    pq.add_producer(2018, 5, ['11', '12', '13', '14', '15', '16', '17'])
    pq.add_producer(2017, 3, ['21', '22', '23', '24', '25', '26', '27'])

    for _ in range(8):
        print pq.get()
    print 

    while True:
        try:
            print pq.get()
        except priorityqueue.Empty as e:
            break

