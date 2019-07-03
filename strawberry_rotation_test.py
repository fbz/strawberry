# strawberry generating code using pycairo
# written by fbz

import cairo
import numpy
import random

WIDTH, HEIGHT = 800, 800 # dimensions of canvas

surface = cairo.SVGSurface('strawberry_rotation_test.svg', WIDTH, HEIGHT) # for output to svg
cx = cairo.Context(surface)


cx.scale(WIDTH, HEIGHT)  # normalize canvas
strawberry_center = WIDTH/6

def strawberry():
	
	cx.translate(-0.1, 0.0)
	translate_x = 0.2
	translate_y = 0.1

	for k in range(0, 4, 1):
		
		right_curve_x3 = random.uniform(.18, .22)
		right_curve_y1 = random.uniform(.005, 0.14)

		cx.move_to(.21, .1)
		cx.curve_to(.3, right_curve_y1, .24, .21, right_curve_x3, .2) #draw right side of strawberry
		cx.move_to(.19, .1)
		cx.curve_to(.08, right_curve_y1, .17, .21, right_curve_x3, .2) #draw left side of strawberry

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

		cx.translate(translate_x, 0.05) # translate the whole shebang

		cx.translate(translate_x, translate_y)
		cx.rotate(1.5)
		negative_translate_x = -(translate_x)
		negative_translate_y = -(translate_y)
		cx.translate(negative_translate_x, negative_translate_y)
		translate_x = translate_x + 0.01
		translate_y = translate_y - 0.2




strawberry()

surface.finish() # output to svg, finish