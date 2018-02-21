import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if.active(True)
sta_if.connect('Snow&John', '1wdv5yjH')

import usocket
import struct
# addr=usocket.getaddrinfo()
addr=("",5683)
s=usocket.socket(usocket.AF_INET,usocket.SOCK_DGRAM)
s.bind(addr)

while True:
  data,addr = s.recv(1024)
s.close()
print(struct.unpack(data))
# 