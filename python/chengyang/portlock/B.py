from pykit import portlock


b_prot_lock = portlock.Portlock('wo shi cheng yang')

b_prot_lock.acquire()

while True:
    pass
