#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# get image
img = cv2.imread("gaussian Noise.png", 0)

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel) #source, desirable depth, kernel

# both printing together
# result = np.hstack((img,dst))

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()


# In[9]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# load image
img = cv2.imread("gaussian Noise.png", 0)

# define the kernel size
kernel = (3,3)

# use cv2.blur
blur_image = cv2.blur(img, kernel)

# use cv2.boxFilter
blurred_image = cv2.boxFilter(img, -1, kernel)

# plot the outputs
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(blur_image,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB))
plt.show()


# In[17]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# get image
img1 = cv2.imread("saltandpepper1.png", 0)
img2 = cv2.imread("gaussian Noise.png", 0)

# define the kernel size
kernel = 3

# use cv2.Median
median = cv2.medianBlur(img1,kernel)

# Use gaussian blur
blur = cv2.GaussianBlur(img2,(11,11),0)

# plotting outputs
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(blur,cv2.COLOR_BGR2RGB))
plt.show()


# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# get image
img_hubble = cv2.imread("hubble.png", 0)

# define the kernel size
kernel = np.ones((15,15), np.float32)/225
dst = cv2.filter2D(img_hubble, -1, kernel)

# use cv2.Median
median = cv2.medianBlur(img1,kernel)

# Use gaussian blur
blur = cv2.GaussianBlur(img2,(11,11),0)

# plotting outputs
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.show()

