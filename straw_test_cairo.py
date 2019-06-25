import cairo
import math
import numpy

WIDTH, HEIGHT = 800, 600
COLOR_BACKGROUND = (255, 255, 255) # background white

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.set_source_rgb(*COLOR_BACKGROUND) #fill the background with white
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(.21, .1)
# Curve(x1, y1, x2, y2, x3, y3)
ctx.curve_to(.3, .08, .24, .21, .2, .2) #draw right side of strawberry
ctx.move_to(.19, .1)
ctx.curve_to(.08, .08, .17, .21, .2, .2) #draw left side of strawberry

ctx.set_source_rgb(255, 0, 0)  # line color red
ctx.set_line_width(0.004) # line width
ctx.stroke()

#draw leaves of strawberry
ctx.move_to(.19, .1)
ctx.line_to(.15, .08)
ctx.line_to(.19, .09)
ctx.line_to(.16, .07)
ctx.line_to(.2, .08)
ctx.line_to(.24, .07)
ctx.line_to(.21, .09)
ctx.line_to(.25, .08)
ctx.line_to(.21, .1)

ctx.set_source_rgb(0, 128, 0)  # line color green
ctx.set_line_width(0.002) # line width
ctx.stroke()

"""
#draw a seed manually
ctx.move_to(.17, .17)
ctx.curve_to(.172, .18, .175, .170, .170, .170)

ctx.set_source_rgb(0, 0, 0)  # line color black
ctx.set_line_width(0.0005) # line width
ctx.stroke()
"""

#generate some seeds on the strawberry
for i in numpy.arange(.15, .25, .01): # numpy.arange allows range using floats
	for j in numpy.arange(.12, .18, .02):
		a = i
		b = j
		c = a + 0.002
		d = b + 0.01
		e = a + 0.005
		f = b

		ctx.move_to(a, b)
		ctx.curve_to(a, b, c, d, e, f)
		ctx.set_source_rgb(0, 0, 0)  # line color black
		ctx.set_line_width(0.0005) # line width
		ctx.stroke()



surface.write_to_png("straw_test_cairo.png")  # Output to PNG
