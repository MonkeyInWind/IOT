from machine import Pin, I2C;
from ssd1306 import SSD1306_I2C;

i2c = I2C(scl=Pin(14), sda=Pin(0));
oled = SSD1306_I2C(128, 64, i2c);

def display(text, x, y):
    oled.text(text, x, y);
    oled.show();

def displayClear():
    oled.fill(0);