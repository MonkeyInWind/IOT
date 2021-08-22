from thermometer import getHT;
from clock import getCurrentTime;
from screen import display;

def showHT():
    ht = getHT();
    t = str(ht['t']);
    h = str(ht['h']);
    display('Tem:' + t, 2, 32);
    display('Hum:' + h, 2, 47);

def showTime():
    # display('loading', 0, 0);
    currentTime = getCurrentTime();
    d = currentTime['date'];
    t = currentTime['time'];
    display(d, 2, 2);
    display(t, 2, 17);

def init():
    showHT();
    showTime();

if __name__ == '__main__':
    init();