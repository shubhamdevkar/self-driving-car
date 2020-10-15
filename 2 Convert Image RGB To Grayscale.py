import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
cv2.imshow('results', gray)
cv2.waitKey(0)

                            #this code converts RGB image to Grayscale
                            #lets run
                            #F5
