import socket
import struct
import re


def ip_num_to_str(ip_num):

    if not isinstance(ip_num, int):
        return 'lei xing' 
    elif ip_num>>32 > 0:
        return 'yue jie'
    elif ip_num < 0:
        return 'yue jie'

    # convert to xxx.xxx.xxx.xxx
    return socket.inet_ntoa(struct.pack('I', socket.htonl(ip_num)))
    
def ip_str_to_num(ip_str):

    if not isinstance(ip_str, basestring):
        return 'lei xing'
    elif re.match(r'\d+\.\d+\.\d+\.\d+', ip_str) is None:
        return 'mo shi '

    ip_list = ip_str.split('.')
    for v in ip_list:
        if int(v) > 255:
            return 'yuejie'
        elif int(v) < 0:
            return 'yuejie'

    return socket.ntohl(struct.unpack('I', socket.inet_aton(ip_str))[0])

if __name__ == '__main__':
    while True:
        print 'Enter q to quit\n'
        
        ip_str = raw_input('please input ip(str):')
        if 'q' == ip_str:
            break
        
        ip_num = ip_str_to_num(ip_str)
        
        print ip_num
        '''
        ip_num = raw_input('please input ip(num):')
        if 'q' == ip_num:
            break

        ip_num = int(ip_num)
        ip_str = ip_num_to_str(ip_num)
        
        print ip_str
        '''
