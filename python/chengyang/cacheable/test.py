from pykit import cacheable
import time


if __name__ == '__main__':

    '''
    print time.ctime()
    c = cacheable.LRU(10,20)
    c['key1'] = 'val1'
    
    time.sleep(10)
    c['key2'] = 'val2'
    print time.ctime()

    try:
        val = c['key1']
    except KeyError:
        print 'key 1 KeyError'
    try:
        val = c['key2']
    except KeyError:
        print 'key 2 KeyError'

    time.sleep(15)
    try:
        val = c['key1']
    except KeyError:
        print 'key 1 KeyError'
    try:
        val = c['key2']
    except KeyError:
        print 'key 2 KeyError'
    print time.ctime()
    '''

    ''' 
    c = cacheable.LRU(10, 20)
    for i in range(1, 23):
        str_key = 'key' + str(i)
        c[str_key] = 'val' + str(i)
    
    for i in range(1, 23):
        try:
            str_key = 'key' + str(i)
            val = c[str_key]
        except KeyError:
            print str_key + ' KeyError'
    '''

    need_cache_data = {
        'key1': 'val1',
        'key2': 'val2',
        'key3': 'val3',
    }

    @cacheable.cache('name_')
    def cache_a(param):
        return need_cache_data.get(param, '')

    print cache_a('key1')
    print cache_a('key2')
    print cache_a('key3')
