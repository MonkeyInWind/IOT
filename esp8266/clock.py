from machine import SPI, Pin, Timer;
import urequests;
import json;

async def getCurrentTime():
    url = 'http://quan.suning.com/getSysTime.do';
    res = urequests.get(url).text;
    dateJson=json.loads(res);
    t = dateJson['sysTime2'].split();
    currentDate = t[0].replace('-', '/');
    currentTime = t[1];
    return {
        'date': currentDate,
        'time': currentTime
    };