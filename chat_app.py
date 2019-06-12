import socket
import thread

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address1 = ("0.0.0.0", 10000)
sock1.bind(server_address1)

def receiver():
    while(True):
        data, address = sock1.recvfrom(4096)
        print "{}:{} : {}".format(address[0],address[1],data)
        print "Enter Message here : "

def sender():
    print "Enter remote machine ip : "
    ip=raw_input()
    while True:
        print "Enter Message here : "
        message = raw_input()
        sock1.sendto(message, (ip,10000))

try:
   thread.start_new_thread(receiver, ( ) )
   thread.start_new_thread(sender, ( ) )
except Exception,ex:
   print "Exception : {}".format(ex)

while True:
   pass
