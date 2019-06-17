import svgwrite

svg = svgwrite.Drawing(filename = "strawberry.svg",
                                size = ("800px", "600px"))

#draw the right side of the strawberry
svg.add(svg.path(
	d="M210,100 C 300,80 240,210 200,200", stroke_width="3",
	style="stroke: #ff0000; fill:none;",
	))

#draw the left side of the strawberry
svg.add(svg.path(
	d="M190,100 C 80,80 170,210 200,200", stroke_width="3",
	style="stroke: #ff0000; fill:none;",
	))

#draw the leaves on the strawberry
svg.add(svg.line(
	start=(190,100), end=(150,80), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(150,80), end=(190,90), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(190,90), end=(160,70), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(160,70), end=(200,80), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(200,80), end=(240,70), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(240,70), end=(210,90), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(210,90), end=(250,80), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

svg.add(svg.line(
	start=(250,80), end=(210,100), stroke_width="3",
	style="stroke: #20C319; fill:none;",
	))

#draw a seed manually
#svg.add(svg.path(
#	d="M170,170 Q 172,180 175,170", stroke_width="1",
#	style="stroke: #7F1824; fill:none;",
#	))

#generate some seeds on the strawberry
for i in xrange(150,250,10):
	for j in xrange(120,180,20):

		a = i
		b = j
		c = a + 2
		d = b + 10
		e = a + 5
		f = b

		svg.add(svg.path(d="M {},{} Q {},{} {},{}".format(a,b,c,d,e,f), stroke_width="1", 
		stroke='#7F1824', fill='none'
		))

svg.add(svg.text("a strawberry",
                                   insert = (220, 220)))

print(svg.tostring())

svg.save()