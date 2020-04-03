import config
from rpi_ws281x import *

strip = Adafruit_NeoPixel(328, 18, 800000, 5, False, 255)
strip.begin()

#pixels = neopixel.NeoPixel(board.D18, config.NUM_ROWS*config.NUM_COLLS, auto_write=False)

def show():
	strip.show()

def pixel(x, y, color):
	if color == 'red':
		r=255
		g=0
		b=0
	elif color == 'green':
		r=0
		g=255
		b=0
	elif color == 'blue':
		r=0
		g=0
		b=255
	elif color == 'yellow':
		r=255
		g=255
		b=0
	elif color == 'orange':
		r=255
		g=151
		b=28
	elif color == 'magenta':
		r=255
		g=0
		b=255
	elif color == "cyan":
		r=27
		g=161
		b=226
	elif color == "white":
		r=255
		g=255
		b=255
	else:
		r=0
		g=0
		b=0

	strip.setPixelColorRGB(y*config.NUM_COLLS+x, r, g, b)
#	pixels[y*config.NUM_COLLS+x] = (r, g, b)
	

