import numpy as np
import cv2 

# opening image
img = cv2.imread("taskpic1.jpg", 1)

# black bars masking
lower_black = np.array([0, 0, 0])
upper_black = np.array([179, 255, 30])
black_mask = cv2.inRange(img, lower_black, upper_black)

# blue ellipse masking
# the bgr value of blue ellipse is (235, 23, 93) 
lower_blue = np.array([200, 0, 60])
upper_blue = np.array([255, 60, 130])
blue_mask = cv2.inRange(img, lower_blue, upper_blue)

# we use bitwise_or as it'll identify if either black or blue mask is present
result = cv2.bitwise_not(cv2.bitwise_or(black_mask, blue_mask))

cv2.imshow('image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

