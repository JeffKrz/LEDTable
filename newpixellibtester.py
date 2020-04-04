from rpi_ws281x import *
from time import sleep
strip = Adafruit_NeoPixel(328, 18, 800000, 5, False, 255)
strip.begin()
for i in range(0,100):
    for i in range(0,327):
     strip.setPixelColorRGB(i, 255, 255, 255)
    strip.show()
    sleep(0.005)
    for i in range(0,327):
      strip.setPixelColorRGB(i, 0,0,0)
    strip.show()
    sleep(0.005)
