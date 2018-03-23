from pykit import rangeset


if __name__ == '__main__':

    r1 = rangeset.Range(1, 10)
    r2 = rangeset.Range(10, 100)
    r3 = rangeset.Range(-10, -5)
    r4 = rangeset.Range(100, 200)
    ir1 = rangeset.IntIncRange(1,10)
    print r1
    print r2
    print r3
    print r4
    print

    print r1.cmp(r2)
    print r1.cmp(r3)
    print r1.cmp(r4)
    print
    
    print ir1.has(10)
    print r1.has(10)
    print r1.has(100)
    print r1.has(-4)
    print r1.has(5.3)
    print r1.has('wo')
    print r1.has([1, 2, 4 ,5])
    print 

    print r1.is_adjacent(r2)
    print r2.is_adjacent(r1)
    print r1.is_adjacent(r3)
    print r1.is_adjacent(r4)
    print

    print r1.length()
    print r2.length()
    print 

    # r1 = rangeset.RangeSet([[1, 5], [4, 6], [10, 20]])
    r1 = rangeset.RangeSet([[1, 5], [6, 10], [15,20]])
    print r1
    print
    
    print r1.has(10)
    print 

    r1.add([5, 6])
    print r1
    print

    print r1.has(10)
    print 

    r1 = rangeset.IntIncRange(1, 5)
    r2 = rangeset.IntIncRange(7, 10)
    r3 = rangeset.IntIncRange(15, 20)
    
    r4 = rangeset.IntIncRangeSet([r1, r2, r3])
    print r4
    print 
   
    print 'r4 has 10?'
    print r4.has(10)
    print

    r4.add([5, 7])
    print r4
    print 

    print 'r4 has 10?'
    print r4.has(10)
    print 

    r1 = rangeset.Range(None, None)
    print r1

    print len(r4)
    print
    
    r1 = rangeset.Range(7, 10)
    r2 = rangeset.Range(10, 10)
    r3 = rangeset.Range(1, 10)

    print r1.cmp(r2)
    print r3.cmp(r2)

    print rangeset.intersect(
        rangeset.RangeSet([[0, 1], [5, 10], [15, 20]]),
        rangeset.RangeSet([[0, 10]]),
    )
