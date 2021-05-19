#!/usr/bin/env python

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

im = Image.open('testcases/found.jpg')
#rgb_im = im.convert('RGB')
rgb_im = im.load()

y = int(im.size[1] / 2)
x = int(im.size[0] / 2)
print(x)
print(y)

target = (27, 63, 147)
walking_pixel = rgb_im[x,y]


while target != walking_pixel:
    walking_pixel = rgb_im[x,y]
    y += 1

if rgb_im[x, y+1] == target and rgb_im[x, y+2] == target:
    print("good !")

print(y)

print(rgb_im[x,y])
print(f"x : {x} - y : {y}")
#print(rgb_im[x-1, y-1])
#im.save("testcases/search_line1.jpg")
