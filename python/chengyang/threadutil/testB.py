from pykit import threadutil
from time import sleep, ctime

loops = [1, 3]


def loop(nloop, nsec):
    print 'start is:', nloop, 'time at:', ctime()
    sleep(nsec)
    print 'end is:', nloop, 'time at:', ctime()


if __name__ == '__main__':
    print 'starting at:', ctime()

    nloops = range(len(loops))
    '''
    for i in nloops:
        t = threadutil.start_thread(
            target=loop,
            name=loop.__name__,
            args=(i, loops[i]),
        )
    '''
    '''
    for i in nloops:
        t = threadutil.start_daemon_thread(

            target=loop,
            name=loop.__name__,
            args=(i, loops[i]),
        )
    '''

    print 'ending'
