from machine import Timer;
from thermometer import getHT;
from clock import initMachineTime, getCurrentTime;
from screen import addText, displayClear, show;
import uasyncio;

HT = {
    "temp": "0",
    "humi": ""
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
    refreshDisplay();

def refreshDisplay():
    displayClear();
    addText(currentTime["date"], 2, 2);
    addText(currentTime["time"], 2, 17);
    addText("Temp:" + HT["temp"], 2, 32);
    addText("Humi:" + HT["humi"], 2, 47);
    show();

def main():
    addText("waiting...", 5, 5);
    show();
    refreshHT(0);
    htTimer.init(period = 1000 * 60 * 5, mode = Timer.PERIODIC, callback = refreshHT);
    clockTimer.init(period = 1000, mode = Timer.PERIODIC, callback = updateTime);

if __name__ == "__main__":
    main();