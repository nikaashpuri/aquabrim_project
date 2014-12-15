import traceback

__author__ = 'nikaashpuri'
import socket
import sys
import os
from time import gmtime, strftime
import file_locations_and_constants

sys.path.append(file_locations_and_constants.SYSTEM_PATH_TO_APPEND)

from views import collect_data_from_device_using_tcp
from views import TCP_SERVER_IP, TCP_SERVER_PORT

filename = file_locations_and_constants.LOG_FILE_LOCATION
f = open(filename, 'a+')
f.close()

# dict to store all connections
dict_device_id_to_connection = {}

def write_to_file(text):
    print_to_stderr(text)
    f = open(filename, 'a+')
    bounding_string = '-----------------------------------------------------'
    f.write(bounding_string + '\n' +
            text + " " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) +'\n' + bounding_string)
    f.close()


def print_to_stderr(text):
    print >>sys.stderr, text


num_attempts = 0
while num_attempts < file_locations_and_constants.NUMBER_OF_SERVER_START_ATTEMPTS:

    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_address)

        text = 'starting up on %s port %s' % server_address
        write_to_file(text)
        break

    except:
        num_attempts += 1
        write_to_file("port is already taken, retry number " + str(num_attempts))


# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    write_to_file('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        write_to_file('connection from ' + repr(client_address))

        received_string = connection.recv(1024)
        # Receive the data in small chunks and retransmit it


        # now either this string has come from the website or from a device
        if received_string.split(" ")[0] == 'send':
            # we have to send this to the device
            # for now we just send this to 123456
            # print dict_device_id_to_connection
            string_to_send = received_string.split(" ")[1]
            # print string_to_send
            write_to_file('*********** SENT DATA: ' + string_to_send[:24] + '--' + string_to_send[24:32] + '--' + string_to_send[32:40] + '--' + string_to_send[40:] + '*****************')
            connection = dict_device_id_to_connection[string_to_send[:24]]
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
            # write_to_file('stored the connection for future use... ' + repr(received_string))
            write_to_file('*********** RECEIVED DATA: ' + repr(received_string) + '*****************')

            # print >>sys.stderr, dict_device_id_to_connection

            # connection.close()
            # now send this command to Django
            collect_data_from_device_using_tcp(received_string)

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        result = ''.join('!! ' + line for line in lines)  # Log it or whatever here
        write_to_file("Exception in tcp ip server: " + '\n' + result)
        continue
        # write_to_file("Exception: " + repr(e))


