import cairo
import math

WIDTH, HEIGHT = 800, 600
COLOR_BACKGROUND = (255, 255, 255) # background white

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.set_source_rgb(*COLOR_BACKGROUND) #fill the background with white
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(0, 0)
# Arc(cx, cy, radius, start_angle, stop_angle)
#ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
#ctx.line_to(0.5, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)

ctx.set_source_rgb(255, 0, 0)  # Solid color red
ctx.set_line_width(0.01) #line width
ctx.stroke()


surface.write_to_png("straw_test_cairo.png")  # Output to PNG
