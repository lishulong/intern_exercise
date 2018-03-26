from pykit import net


if __name__ == '__main__':

    ip1 = '192.168.24.56'
    ip2 = '192.23.4.2.3.5'
    ip3 = 'dada'
    print net.is_ip4(ip1)
    print net.is_ip4(ip2)
    print net.is_ip4(ip3)
