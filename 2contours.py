import numpy as np 
import cv2


# opening image
img = cv2.imread("taskpic1.jpg", 1)

# converting image to grayscale
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# using automatic thresholding to convert to binary image for contour detection
# since our image has different shapes with different colours and brightness, 
# we will do thresholding using difference from background colour

bg_color = np.array([0, 215, 84]) 
diff = cv2.absdiff(img, np.full_like(img, bg_color))
diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(diff_gray, 30, 255, cv2.THRESH_BINARY)

cv2.imshow('binary_output.png', thresh)


# contour detection 
# RETR_EXTERNAL gives only outer contours 
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# displaying the contours found 
print("TOTAL NUMBER OF CONTOURS = {} ".format(len(contours)))


# drawing contours on a copy of original image 
output = img.copy()
cv2.drawContours(output, contours, -1, (0, 0, 255), 3)
# cv2.drawContours(source, contours, contour index - negative so all contours are drawn, colour, thickness)


#saving and displaying the image
cv2.imwrite('binary_image.png', thresh)
cv2.imwrite('contours.png', output)

# looping over the contours to get the image moments of each contour
print("contour coordinates are :")
for contour in contours:
    M = cv2.moments(contour)
    #calculating centroid (centre) of each contour and displaying 
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print("({},{})".format(cx, cy)) 
    # finding perimeter and vertices to differentiate contours
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    num_vertices = len(approx)
    casualty = ""

    if num_vertices == 0:
        casualty == "child"
    elif num_vertices == 5:
        casualty == "adult"
    elif num_vertices == 4:
         x, y, w, h = cv2.boundingRect(approx)
         aspect_ratio = w / float(h)
         casualty == "senior citizen" if 0.95 <= aspect_ratio <= 1.05 else "non-traversable area"
    print("the casualty is {}".format(num_vertices))


cv2.imshow('threshold image', thresh)
cv2.imshow('contours', output)
cv2.waitKey(0)
cv2.destroyAllWindows()




