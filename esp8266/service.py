import urequests;
import ujson;
import network;
import binascii;

wlan = network.WLAN(network.STA_IF);
b = wlan.config('mac');
mac = binascii.hexlify(b).decode()[2:];

def uploadHT(data):
    b = {
        "macAddress": mac,
        "data": data
    }
    urequests.post("http://192.168.31.222:6080/api/HT/update", headers = {'content-type': 'application/json'}, data = ujson.dumps(b));