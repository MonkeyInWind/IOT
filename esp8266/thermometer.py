import dht;
import machine;
from service import uploadHT;

def getHT():
    d = dht.DHT11(machine.Pin(2));
    d.measure();
    t = str(d.temperature());
    h = str(d.humidity());
    data = {
        "temp": t,
        "humi": h
    };
    uploadHT(data);
    return data;
