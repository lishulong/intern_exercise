from pykit import portlock
import time


a_port_lock = portlock.Portlock('wo shi cheng yang')

'''
pl.acquire()
print pl.has_locked()

pl.release()
print pl.has_locked()
'''

while True:

    with a_port_lock as pl:
        time.sleep(10)
        
    print 'end'
    time.sleep(3)
