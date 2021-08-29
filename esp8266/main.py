from machine import Timer;
from thermometer import getHT;
from clock import initMachineTime, getCurrentTime;
from screen import refreshDisplay;
import time;

HT = {
    "temp": "0",
    "humi": "0"
}

currentTime = {
    "date": "-/-/-",
    "time": "-:-:-"
}

currentHour = "";

htTimer = Timer(0);
clockTimer = Timer(1);

def refreshHT(t):
    global HT;
    HT = getHT();

def initTime():
    global currentTime, currentHour;
    initMachineTime();
    currentTime = getCurrentTime();
    print("initTime: ", currentTime);
    currentHour = currentTime["h"];

def updateTime(t):
    global currentTime;
    currentTime = getCurrentTime();
    h = currentTime["h"];
    if h != currentHour:
        initTime();
    refreshDisplay([
        [currentTime["date"], 2, 2],
        [currentTime["time"], 2, 17],
        ["Temp:" + HT["temp"], 2, 32],
        ["Humi:" + HT["humi"], 2, 47]
    ]);

def main():
    refreshDisplay([["waiting...", 5, 5]]);
    time.sleep(2);
    refreshHT(0);
    htTimer.init(period = 1000 * 60 * 10, mode = Timer.PERIODIC, callback = refreshHT);
    clockTimer.init(period = 1000, mode = Timer.PERIODIC, callback = updateTime);

if __name__ == "__main__":
    main();