import socket
import struct


def ip_str_to_num(ip_str):
    return socket.ntohl(struct.unpack('I', socket.inet_aton(ip_str))[0])
   
def ip_num_to_str(ip_num):
    if not isinstance(ip_num, int):
        raise ValueError('input must be in')
    if ip_num < 0 or ip_num >>32 > 0:
        raise ValueError('num muset >= 0 and < 2 ** 32')

    return socket.inet_ntoa(struct.pack('I',socket.htonl(ip_num)))
