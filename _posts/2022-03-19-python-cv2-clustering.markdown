---
layout: post
title:  Color clustering with python opencv
date:   2022-03-20 
image:  '/images/posts/opencv_cluster/maboroshi_clean_2.png'
tags:   [python, computer vesion]
---

Sometimes you want to break down a image into a few pieces with unique colors. This is a easy task if the image only has a few colors, however, in many cases the image has noises and may have hundreds of colors that are different from, but very similar to, a few colors. 

To give a more concrete example, this image below (a kanji standing for "illusion") appears to have only two colors: black and white.

<p align="center">
<img align="center" width="300" height="300" src="{{site.baseurl}}/images/posts/opencv_cluster/maboroshi.jpeg">
</p>

However it has more than 100 colors spanning a spectrum from pure black to pure white. How to replace "nearly black" with black and "nearly white" with white? One solution is kmeans-clustering algorithm from a python library `opencv`.

First, install [opencv](https://pypi.org/project/opencv-python/). In most cases you just need to run in terminal:
```bash
pip install opencv-python
```
\
Then, read your image with opencv.
```python
import cv2
import numpy as np # numpy will be used later on, as most transformation that we will do are based on numpy arrays
input_file = "path/to/image" # change the path to your path here
image = cv2.imread(str(input_file))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```
\
this converts an image to an array with shape (height, width, 3), where the third dimension stores the color of each pixel in [rgb](https://en.wikipedia.org/wiki/rgb_color_model) format. aternatively you can read the image with [pillow](https://pillow.readthedocs.io/en/stable/), a popular image-processing library.

then flatten the array to a matrix with 3 rows, where each column represents a pixel. this is a requirement for the input of the kmeans algorithm.
```python
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
```
\
use `cv2.kmeans` to find the centers and labels.
```python
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 2 # number of colors you want in the result
compactness, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# convert back to 8 bit values
centers = np.uint8(centers)
# flatten the labels array
labels = labels.flatten()
```
\
note the labels is a vector of integer labels that indicates which color each pixel has. we need to convert back to rgb colors by translating the labels to rgb colors, then rehsape it to the original shape.
```python
output_image = centers[labels].reshape(image.shape)
# save image to file
output_file = "paht/to/output_image.png"
cv2.imwrite(output_file, output_image)
```
\
Now let's compare the original image (left) and the output image (right). The blurry, grey-ish boundary of the kanji is obviously gone.
<p align="center">
<img width="300" height="300" src="{{site.baseurl}}/images/posts/opencv_cluster/maboroshi.jpeg">
<img width="300" height="300" src="{{site.baseurl}}/images/posts/opencv_cluster/maboroshi_clustered.png">
</p>

Now that we have labelled each pixel, let's have some fun!
Read a second image that is of a mountain, replace the white background of the kanji by the mountain, and replace the kanji by grey.

<p align="center">
<img width="300" height="300" src="{{site.baseurl}}/images/posts/opencv_cluster/maboroshi_transformed.png">
</p>

Full code:
```python
import cv2
import numpy as np 
input_file = "../images/posts/opencv_cluster/maboroshi.jpeg" # change the path to your path here
image = cv2.imread(str(input_file))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 2
compactness, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# convert back to 8 bit values
centers = np.uint8(centers)
# flatten the labels array
labels = labels.flatten()
output_image = centers[labels].reshape(image.shape)
# save image to file
output_file = "../images/posts/opencv_cluster/maboroshi_clustered.png" # change the path to your path here
cv2.imwrite(output_file, output_image)

# background replacement
input_file2 = "../images/posts/opencv_cluster/mountain.jpeg" # change the path to your path here
image2 = cv2.imread(str(input_file2))
image2 = cv2.resize(image2, output_image.shape[:2][::-1])
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
labels = np.array(labels).reshape(output_image.shape[:2])

mask = np.stack([labels == 1] * 3, axis=2) # this mask decide which pixel is background
output_image = np.where(mask, image2, 230)
output_file = "../images/posts/opencv_cluster/maboroshi_transformed.png" # change the path to your path here
cv2.imwrite(output_file, output_image)
```

---

 