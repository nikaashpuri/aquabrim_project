__author__ = 'nikaashpuri'
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# server_address = ('localhost', 40000)
server_address = ('162.251.84.104', 40000)

print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    # Send data
    message = '11111111' \
              '11111111' \
              '11111111' \
              '00000011' \
              '111111' \
              '1111111111'
    '''
    device id - 255255255
    command id - 3
    sub id - 63
    AF, AL, M, F, E - all 1
    No signal duration - 31
    '''
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    data = sock.recv(1024)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

'''
111111111111111111111111
00000011
11111111
11111111
'''