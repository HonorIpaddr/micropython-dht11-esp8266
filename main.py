from machine import Timer
from machine import Pin
from chipid import chipid
import dht
import wifi
import register
import usocket
import ujson
from machine import reset


class http:
    def __init__(self, url='', apikey=''):
        self.url=url+"/datapoints?type=3"
        self.apikey=apikey
        self.dht11=dht.DHT11(Pin(2))
        self.pid = 0

    def updata(self,t):
        self.dht11.measure()
        jdata={"temp":self.dht11.temperature(),"humi":self.dht11.humidity()}
        data=ujson.dumps(jdata)
        # print(jdata)
        # print(data)
        _, _, host, path = self.url.split('/', 3)
        # print(self.url)
        # print(host)
        # print(path)
        addr = usocket.getaddrinfo(host, 80)[0][-1]
        s = usocket.socket()
        s.connect(addr)
        s.send(bytes('POST /%s HTTP/1.0\r\napi-key:%s\r\nHost:%s\r\nContent-Length:%d\r\n\r\n%s' % (path, self.apikey,host,len(data),data), 'utf8'))
        # print('POST /%s HTTP/1.0\r\napi-key:%s\r\nHost:%s\r\nContent-Length:%d\r\n\r\n%s' % (path, self.apikey,host,len(data),data))
        while True:
            data = s.recv(100)
            if data:
                print(str(data, 'utf8'), end='')
            else:
                break
        s.close()
    def timerdata(self):
        tim = Timer(-1)
        tim.init(period=30000, mode=Timer.PERIODIC, callback=self.updata) 


def checkWifi(t):
    wifi.do_connect(False)


def main():
    wifi.do_connect(True)
    netTim = Timer(1)
    netTim.init(period=60000, mode=Timer.PERIODIC, callback=checkWifi)
    apikey="=your apikey="
    #替换成你自己的key和id
    apiUrl = 'http://api.heclouds.com/devices/=youerdeviceid='
    hr=http(url=apiUrl,apikey=apikey)
    hr.timerdata()

main()
