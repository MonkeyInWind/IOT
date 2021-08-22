import dht;
import machine;

def getHT():
    d = dht.DHT11(machine.Pin(2));
    d.measure();
    t = d.temperature();
    h = d.humidity();
    return {
        't': t,
        'h': h
    };
