from socket import *

# create
s = socket(AF_INET,SOCK_DGRAM)

host = gethostname()
port = 1111

while True:
    message = raw_input("Input Message : ")
    s.sendto(message,(host,port))

# close
s.close()