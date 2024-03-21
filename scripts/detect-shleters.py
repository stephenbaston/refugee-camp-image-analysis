	
import cv2

# read image
img_zaatari1 = cv2.imread('./input/zaatari1.png', cv2.IMREAD_COLOR)

# do stuff

# write image
cv2.imwrite('./output/zaatari1.png', img_zaatari1)

# show result
cv2.imshow('Result', img_zaatari1)
cv2.waitKey(0)