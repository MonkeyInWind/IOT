import dht;
import machine;
import urequests;
import ujson

def getHT():
    d = dht.DHT11(machine.Pin(2));
    d.measure();
    t = str(d.temperature());
    h = str(d.humidity());
    data = {
        "temp": t,
        "humi": h
    };
    urequests.post("http://192.168.31.222:6080/api/HT/update", headers = {'content-type': 'application/json'}, data = ujson.dumps(data));
    return data;
