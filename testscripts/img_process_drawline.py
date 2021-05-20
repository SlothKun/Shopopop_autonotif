#!/usr/bin/env python

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

im = Image.open('testcases/phonescreen.png')
rgb_im = im.convert('RGB')

draw = ImageDraw.Draw(im)
draw.line((540, 1110) + (540, 2220), width=1, fill="green")

im.save("testcases/phonescreen_draw.png")
