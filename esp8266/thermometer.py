import dht;
import machine;

def getHT():
    d = dht.DHT11(machine.Pin(2));
    d.measure();
    t = d.temperature();
    h = d.humidity();
    return {
        'temp': str(t),
        'humi': str(h)
    };
