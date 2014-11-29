__author__ = 'nikaashpuri'
import socket
import sys
import os
sys.path.append('/public_html/aquabrim_project')
sys.path.append('/Users/nikaashpuri/Documents/alibi_projects/aquabrim_project/')

from views import collect_data_from_device_using_tcp
from aquabrim_project.settings import BASE_DIR
from views import TCP_SERVER_IP, TCP_SERVER_PORT

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

'''
filename = '/logs/django_log'
f = open(filename, 'a+')
f.close()
'''

# dict to store all connections
dict_device_id_to_connection = {}

def write_to_file(text):
    filename = ''
    f = open(filename, 'a+')
    f.write(text + '\n')
    f.close()


def print_to_stderr(text):
    print >>sys.stderr, text


while True:
    # Wait for a connection
    print_to_stderr('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print_to_stderr('connection from ' + repr(client_address))

        received_string = connection.recv(1024)
        # Receive the data in small chunks and retransmit it


        # now either this string has come from the website or from a device
        if received_string.split(" ")[0] == 'send':
            # we have to send this to the device
            # for now we just send this to 123456
            # print dict_device_id_to_connection
            string_to_send = received_string.split(" ")[1]
            connection = dict_device_id_to_connection[string_to_send[:24]]
            '''
            fixed_string_to_send = ''.join(format(ord(i), 'b').zfill(8) for i in string_to_send[:3])
            fixed_string_to_send += string_to_send[3:]
            unicode_string = \
                unicode('-'.join(str(int(fixed_string_to_send[i:i+8], 2))
                                for i in xrange(0, len(fixed_string_to_send), 8)))
            print unicode_string
            '''
            connection.sendall(string_to_send)
        else:
            # we receive this connection
            # Clean up the connection
            # store the connection for future use
            # device_id = received_string.split(" ")[0]
            # first three bytes denote the device id
            device_id = received_string[:24]
            # print received_string
            # print len(received_string)
            dict_device_id_to_connection[device_id] = connection
            print_to_stderr('stored the connection for future use... ' + repr(received_string))
            # print >>sys.stderr, dict_device_id_to_connection

            # connection.close()
            # now send this command to Django
            collect_data_from_device_using_tcp(received_string)

    except TypeError as e:
        print_to_stderr("Exception in tcp ip server: " + repr(e))
        # write_to_file("Exception: " + repr(e))


