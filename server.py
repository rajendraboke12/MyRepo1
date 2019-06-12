import socket
import thread
import re
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address1 = ('172.16.10.65', 10000)
server_address2 = ('172.16.10.65', 10001)
sock1.bind(server_address1)
sock2.bind(server_address2)
def receiver():
    while(True):
        data, address = sock1.recvfrom(4096)
        print(address[0]+":"+str(address[1])+" : "+data)
        print("Enter Message here : ")

def sender():
    data, address = sock2.recvfrom(4096)
    while(True):
        print("Enter Message here : ")
        message = raw_input()
        sent = sock2.sendto(message, address)

try:
   thread.start_new_thread(receiver, ( ) )
   thread.start_new_thread(sender, ( ) )
except Exception,ex:
   print "Exception : "+str(ex)

while 1:
   pass
