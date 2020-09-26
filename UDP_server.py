from socket import *

buf = 2048

# create
s = socket(AF_INET,SOCK_DGRAM)

# bind
host = gethostname()
port =  1111
s.bind((host,port))

print gethostname

# read / write
while True:
    data, addr = s.recvfrom(buf)
    print data

# close
s.close()
