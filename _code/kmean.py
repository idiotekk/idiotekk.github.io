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

input_file2 = "../images/posts/opencv_cluster/mountain.jpeg" # change the path to your path here
image2 = cv2.imread(str(input_file2))
image2 = cv2.resize(image2, output_image.shape[:2][::-1])
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
labels = np.array(labels).reshape(output_image.shape[:2])
mask = np.stack([labels == 1] * 3, axis=2)
output_image = np.where(mask, image2, 230)
output_file = "../images/posts/opencv_cluster/maboroshi_transformed.png" # change the path to your path here
cv2.imwrite(output_file, output_image)