def convert2bin(val, length):
    a = bin(val)
    a = a[2:]
    l = len(a)
    a = str(a)
    s = ""
    if (length-l>0):
        for i in range(0, (length-l)):
            s = s + "0"
        return (s+a)
    else:
        return a

def sendFunction(data_stream):
    print "The data stream is : " + data_stream
    #Add the functions in this file so that the data stream can be sent back from where we first recieved the data from the receiver.py file

print convert2bin(12, 8)