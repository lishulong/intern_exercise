from pykit import strutil


if __name__ == '__main__':
    green_str = strutil.ColoredString('green string!', 'green')
    red_str = strutil.ColoredString('red string!', 'red')
    color_str = strutil.ColoredString('150 string!', 150)
    print green_str
    print red_str
    print color_str
    print 

    print green_str.join(['wo', 'shi', 'cheng', 'yang'])
    
    str_split = 'If sep is not specified or is None, a diffrent splittin'
    str_split += ' algorithm is applied: runs of consecutive whitespace'
    str_split += ' are regarded as a single separator'
    str_split = strutil.ColoredString(str_split, 'red')
    list_split = str_split.split()
    for v in list_split:
        print v

    for v in strutil.ColoredString('h\rello\npyk\rit').splitlines():
        print v
    
    str_break_line = 'one two three four five six seven eight nine ten'
    print strutil.break_line(str_break_line, 10)
    str_break_line = 'aaaaabbbbbcccccdddddeeeeefffff'
    print strutil.break_line(str_break_line, 10)

    t = strutil.blue("blue-text")
    print t

    for p in xrange(0, 200):
        print strutil.colorize(p, 100),
    print 
    for p in xrange(0, 100):
        print strutil.colorize(p, 10),
    print
    print strutil.colorize(22, 100, '{0:>10}%')
    
    str_linestr = 'adw\nni\nleng\n'
    print strutil.line_pad(str_linestr, 'hehe' * 4)

    print strutil.format_line([["name:", "age:"], ["drdrxp", "18"], "wow"], sep= 
    " | ", aligns="lll")

    lines = 'cheng yang 180'
    lines += 'zhang xixi 150'
    lines += 'liu xiang 170'
    lines += 'yao ming 160'
    print strutil.sharding(lines, size=160, accuracy=30)
    
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    for l in strutil.struct_repr(a):
        print l
    print

    print strutil.tokenize(' a\t b\n c\r ')
    print strutil.tokenize('a bxyc d', sep='xy')

