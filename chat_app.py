import socket
import thread
import netifaces as ni

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ni.ifaddresses('wlp2s0')
ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
server_address1 = (ip, 10000)
sock1.bind(server_address1)

def receiver():
    while(True):
        data, address = sock1.recvfrom(4096)
        print(address[0]+":"+str(address[1])+" : "+data)
        print("Enter Message here : ")

def sender():
    print("Enter ip : ")
    ip=raw_input()
    while(True):
        print("Enter Message here : ")
        message = raw_input()
        sent = sock1.sendto(message, (ip,10000))

try:
   thread.start_new_thread(receiver, ( ) )
   thread.start_new_thread(sender, ( ) )
except Exception,ex:
   print "Exception : "+str(ex)

while 1:
   pass
