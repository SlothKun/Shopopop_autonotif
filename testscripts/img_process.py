#!/usr/bin/env python

#import cv2
#image = cv2.imread("testcases/Found.png")
#edges = cv2.Canny(image,50,300)
#cv2.imwrite('testcases/found_edges.png', edges)


import numpy as np
import PIL.Image
import matplotlib.pyplot as plt


def create_sample_set(mask, N=36, shape_color=[0,0,1.,1.]):
    rv = np.ones((N, mask.shape[0], mask.shape[1], 4),dtype=np.float)
    mask = mask.astype(bool)
    for i in range(N):
        for j in range(3):
            current_color_layer = rv[i,:,:,j]
            current_color_layer[:,:] *= np.random.random()
            current_color_layer[mask] = np.ones((mask.sum())) * shape_color[j]
    return rv

# create set of sample image and plot them
image = PIL.Image.open("testcases/Found.png")
image_data = np.asarray(image)
image_data_blue = image_data[:,:,2]
median_blue = np.median(image_data_blue)
sample_images = create_sample_set(image_data_blue>median_blue)
plt.figure(1)
for i in range(36):
    plt.subplot(6,6,i+1)
    plt.imshow(sample_images[i,...])
    plt.axis("off")
plt.subplots_adjust(0,0,1,1,0,0)

# determine per-pixel variablility, std() over all images
variability = sample_images.std(axis=0).sum(axis=2)

# show image of these variabilities
plt.figure(2)
plt.imshow(variability, cmap=plt.cm.gray, interpolation="nearest", origin="lower")

# determine bounding box
mean_variability = variability.mean()
non_empty_columns = np.where(variability.min(axis=0)<mean_variability)[0]
non_empty_rows = np.where(variability.min(axis=1)<mean_variability)[0]
boundingBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

# plot and print boundingBox
bb = boundingBox
plt.plot([bb[2], bb[3], bb[3], bb[2], bb[2]],
         [bb[0], bb[0],bb[1], bb[1], bb[0]],
         "r-")
plt.xlim(0,variability.shape[1])
plt.ylim(variability.shape[0],0)

print(boundingBox)
plt.savefig("testcases/found_matlib.png")
