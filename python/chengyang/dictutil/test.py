from pykit import dictutil
import time
import operator


if __name__ == '__main__':

    print dictutil.attrdict(c=1, y=2)
    x = {'a': 1, 'b': 2, 'c': 3}
 
    b = dictutil.attrdict(x)
    b.a = 10
    print b

    c = dictutil.attrdict_copy(x)
    print c
    print c.b
    print c
    print 

    mydict = {
        'a': {
            'a.a': 'v-a.a',
            'a.b': {'a.b.a': 'v-a.b.a'},
            'a.c': {'a.c.a': {'a.c.a.a': 'v-a.c.a.a'}}
        }
    }
    
    for rst in dictutil.depth_iter(mydict):
        print rst
    print 
    
    for rst in dictutil.depth_iter(mydict, maxdepth=2):
        print rst
    print

    for rst in dictutil.depth_iter(mydict, ks=['mykey1', 'mykey2', 'mykey3']):
        print rst
    print  

    for keys, vals in dictutil.depth_iter(mydict, intermediate=True):
        print keys  
    print 

    set_minute = dictutil.make_setter('time.minute', 
        value=lambda vars: int(time.time()) % 3600 / 60)
    tm = {"time": {"hour": 11, "minute": 20}}
    print set_minute(tm)
    print tm
    print

    a = {"x":{}}
    b = {"x":{"x":{}}}
    print dictutil.contains(a,b)
    print dictutil.contains(b,a)
    print

    a = {
        'k1': 1,
        'k3': {'s2': 'foo'},
    }
    b = {
        'k1': 2,
        'k2': 3,
        'k3': {'s1': 'foo', 's2': 'bar'},
        'k4': {'s1': 'bar'},
    }
    exclude = {
        'k4': True,
        'k3': {'s1': True},
    }
    r = dictutil.combine(a, b, operator.add, exclude=exclude)
    print r
    r = dictutil.combine(a, b, operator.add)
    print r
    r = dictutil.combineto(a, b, operator.add, exclude=exclude)
    print r
    r = dictutil.combineto(a, b, operator.add)
    print r
