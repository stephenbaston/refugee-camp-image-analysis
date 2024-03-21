	
import cv2

# read image
img_zaatari1 = cv2.imread('./input/zaatari1.png', cv2.IMREAD_COLOR)

# draw boxes on clicks
click = 0
coords = []
def onClick(event, x, y, flags, params):
    global click
    global coords
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append((x, y))
        print(f'({x},{y})')
        if click > 0:
            cv2.line(img_zaatari1, coords[click - 1], coords[click], (200,0,0), 2)
        if click == 3:
            cv2.line(img_zaatari1, coords[0], coords[click], (200,0,0), 2)
        if click >= 3:
            click = 0
            coords = []
        else:
            click += 1

# write image
# cv2.imwrite('./output/zaatari1.png', img_zaatari1)

# prepare window
cv2.namedWindow('Points Coordinates')
cv2.setMouseCallback('Points Coordinates', onClick)

# show window
while True:
    cv2.imshow('Points Coordinates', img_zaatari1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
      break
cv2.destroyAllWindows()