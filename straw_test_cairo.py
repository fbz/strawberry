import cairo
import numpy

WIDTH, HEIGHT = 800, 600 # dimensions of canvas
COLOR_BACKGROUND = (255, 255, 255) # background white

surface = cairo.SVGSurface('straw_test_cairo.svg', WIDTH, HEIGHT) # for output to svg
#surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT) # for output to png, also turn on at end
cx = cairo.Context(surface)

cx.scale(WIDTH, HEIGHT)  # normalize canvas

#fill background with white
#cx.set_source_rgb(*COLOR_BACKGROUND)
#cx.rectangle(0, 0, WIDTH, HEIGHT)
#cx.fill()

#cx.translate(0.1, 0.1)  # translate the whole shebang

cx.move_to(.21, .1)
# curve(x1, y1, x2, y2, x3, y3)
cx.curve_to(.3, .08, .24, .21, .2, .2) #draw right side of strawberry
cx.move_to(.19, .1)
cx.curve_to(.08, .08, .17, .21, .2, .2) #draw left side of strawberry

cx.set_source_rgb(255, 0, 0)  # line color red
cx.set_line_width(0.004) # line width
cx.stroke() # draw

#draw leaves of strawberry
cx.move_to(.19, .1)
cx.line_to(.15, .08)
cx.line_to(.19, .09)
cx.line_to(.16, .07)
cx.line_to(.2, .08)
cx.line_to(.24, .07)
cx.line_to(.21, .09)
cx.line_to(.25, .08)
cx.line_to(.21, .1)

cx.set_source_rgb(0, 128, 0)  # line color green
cx.set_line_width(0.002) # line width
cx.stroke() # draw

"""
#draw a seed manually
cx.move_to(.17, .17)
cx.curve_to(.172, .18, .175, .170, .170, .170)

cx.set_source_rgb(0, 0, 0)  # line color black
cx.set_line_width(0.0005) # line width
cx.stroke()
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

		cx.move_to(a, b)
		cx.curve_to(a, b, c, d, e, f)
		cx.set_source_rgb(0, 0, 0)  # line color black
		cx.set_line_width(0.0005) # line width
		cx.stroke() # draw

surface.finish() # output to svg, finish
#surface.write_to_png("straw_test_cairo.png")  # output to png