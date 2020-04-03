from rpi_ws281x import *
strip = Adafruit_NeoPixel(328, 18, 800000, 5, False, 255)
strip.begin()
strip.setPixelColorRGB(25, 255, 255, 255)
strip.show()