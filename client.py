import socket
import thread
import re
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(True):
        print("Enter ip address of remote machine : ")
        ip=raw_input()
        x=re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",ip)
        if(x):
            break
server_address1 = (ip, 10000)
server_address2 = (ip, 10001)
def receiver(a,b):
    sent = sock1.sendto("hello", server_address2)
    while(True):
        data, address = sock1.recvfrom(4096)
        print(address[0]+":"+str(address[1])+" : "+data)
        print("Enter Message here : ")

def sender():
    while(True):
        print("Enter Message here : ")
        message = raw_input()
        sent = sock2.sendto(message, server_address1)

try:
   thread.start_new_thread(receiver, ( ) )
   thread.start_new_thread(sender, ( ) )
except Exception,ex:
   print "Exception : "+str(ex)

while 1:
   pass
