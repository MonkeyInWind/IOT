from thermometer import getHT;
from clock import getCurrentTime;
from screen import display, displayClear;
import uasyncio;

def refresh(data):
    displayClear();
    display(data['d'], 2, 2);
    display(data['t'], 2, 17);
    display('Temp:' + data['temp'], 2, 32);
    display('Humi:' + data['humi'], 2, 47);

async def main():
    display('loading...', 5, 5);
    currentTime = list(await uasyncio.gather(getCurrentTime()))[0];
    HT = getHT();
    refresh({
        'd': currentTime['date'],
        't': currentTime['time'],
        'temp': HT['temp'],
        'humi': HT['humi']
    });

if __name__ == '__main__':
    uasyncio.run(main());