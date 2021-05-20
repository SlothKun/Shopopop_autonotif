#!/usr/bin/env python

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

im = Image.open('testcases/phonescreen.png')
#rgb_im = im.convert('RGB')
rgb_im = im.load()

print(im.size[0], " - ", im.size[1])

y = int(im.size[1] / 2)
x = int(im.size[0] / 2)
print(x)
print(y)

target = (27, 63, 146, 255)
walking_pixel = rgb_im[x,y]


while target != walking_pixel:
    walking_pixel = rgb_im[x,y]
    y += 1
    print("y : ", y, " walkpix : ", walking_pixel)

if rgb_im[x, y+1] == target and rgb_im[x, y+2] == target:
    print("good !")

print(y)

print(rgb_im[x,y])
print(f"x : {x} - y : {y}")
#print(rgb_im[x-1, y-1])
#im.save("testcases/search_line1.png")
