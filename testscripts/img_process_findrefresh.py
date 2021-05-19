#!/usr/bin/env python

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

im = Image.open('testcases/search_nc.jpg')
#rgb_im = im.convert('RGB')
rgb_im = im.load()

i = 0
pixelstarter = rgb_im[0,0]
walking_pixel = rgb_im[i,i]



while pixelstarter == walking_pixel:
    walking_pixel = rgb_im[0,i]
    i += 1

print(i)


y = i - int(i/3)
print(y)
x = 0
walking_pixel = rgb_im[0,y]

while pixelstarter == walking_pixel:
    x += 1
    walking_pixel = rgb_im[x, y]

print(rgb_im[x,y])
print(f"x : {x} - y : {y}")
print(rgb_im[x-1, y-1])
#im.save("testcases/search_line1.jpg")
