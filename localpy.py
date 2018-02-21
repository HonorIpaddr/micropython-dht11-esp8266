import socket
import struct

addr=("",5683)
udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(addr)

while True:
  data,addr=udpServer.recvfrom(1024)
  print()
udpServer.close()

