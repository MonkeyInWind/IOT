from thermometer import getHT;
from clock import getCurrentTime;

def init():
    print(getHT());
    print(getCurrentTime());

if __name__ == '__main__':
    init();