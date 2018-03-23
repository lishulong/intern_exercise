from pykit import humannum


if __name__ == '__main__':
    num = 1024 ** 3 * 100
    print humannum.humannum(num)
    print humannum.humannum(num, humannum.K)
    string = humannum.humannum(num, humannum.T)
    print string
    print humannum.parsenum(string)
    print

    num1 = 1024 ** 2 * 2
    num1 = str(num1)
    print humannum.humannum(num1)
    print

    num2 = [1024214, 1515161, 616171]
    string = humannum.humannum(num2)
    print string
    # can't analysis list
    # print humannum.parseint(string)
    print

    num3 = {'1': 1024 ** 3 * 10, '2': 1024 ** 2, '3': 1024 ** 4}
    print humannum.humannum(num3,exclude=['1'])
    print humannum.humannum(num3, include=['1','2'])
    print

    num4 = '14%'
    print humannum.parsenum(num4)
