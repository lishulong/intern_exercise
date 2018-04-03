from pykit import cachepool


class Element(object):

    def __init__(self, *args, **argkw):

        self.args = args
        self.argkw = argkw

        self.closed = False

    def close(self):

        self.close = True

    def do(self):

        print self.args
        print self.argkw

    def __str__(self):
        print 'this is element'
        print self.args
        print self.argkw
        return ''


def generator(*args, **argkw):

    return Element(args, argkw)


def close_callback(element):

    element.close()


def reuse_decider(errtype, errval, _traceback):

    if errtype in (
                cachepool.CachePoolError,
                cachepool.CachePoolGeneratorError,):
        return True

    return False


pool = cachepool.CachePool(
        generator,
        generator_args=[],
        generator_argkw={},
        close_callback=close_callback,
        pool_size=512,
    )

print pool.get()
print pool.stat

wrapper = cachepool.make_wrapper(
    pool,
    reuse_decider=reuse_decider,
)

with wrapper() as ele:
    ele.do()

print pool.stat
