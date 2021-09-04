from db import database;

def getHT(start, end):
    devices = database.selectDevices("ESP8266");
    htData = database.selectHT(start, end);
    res = [];
    for device in devices:
        d = {
            "macAddress": device[0],
            "name": device[1],
            "type": device[2],
        }
        deviceHT = [];
        for ht in htData:
            if (ht[1] == device[0]):
                deviceHT.append({
                    "temp": ht[2],
                    "humi": ht[3],
                    "timestamp": ht[4]
                });
        d["ht"] = deviceHT;
        res.append(d);
    return res;

