import cv2
import numpy as np

# %% read in the image
img = cv2.imread('cave.jpg')

img1 = []
img2 = []
for i, row in enumerate(img):
    if i % 2 == 1:
        img1.append(list(row[::2]))
        img2.append(list(row[1::2]))
    else:
        img1.append(list(row[1::2]))
        img2.append(list(row[0::2]))

np.array(img1).shape
cv2.imwrite('img1.png', np.array(img1))
cv2.imwrite('img2.png', np.array(img2))
#evil
