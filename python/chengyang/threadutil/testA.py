from threading import Thread
from pykit import threadutil
from time import ctime, sleep

loops = [5, 3]


class MyThread(Thread):

    def __init__(self, func, args, name):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print 'start loop ', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop ', nloop, 'done at:', ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
