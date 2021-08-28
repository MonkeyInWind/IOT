from machine import Pin, I2C;
from ssd1306 import SSD1306_I2C;

i2c = I2C(scl=Pin(14), sda=Pin(0));
oled = SSD1306_I2C(128, 64, i2c);

def refreshDisplay(data):
    oled.fill(0);
    for i in range(len(data)):
        item = data[i];
        oled.text(item[0], item[1], item[2]);
    oled.show();
