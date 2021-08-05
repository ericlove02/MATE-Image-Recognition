import numpy as np
import pyautogui
import cv2
from PIL import Image, ImageDraw, ImageFont

pyautogui.screenshot('image.jpg')

font = cv2.FONT_HERSHEY_COMPLEX

tri = 0
rect = 0
line = 0
circ = 0

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.blur(img, (10,10))
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
   approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
   x = approx.ravel()[0]
   y = approx.ravel()[1]
   area = cv2.contourArea(cnt)
   if len(approx) == 3:
       if(100000 > area > 8000):
           tri += 1
   elif len(approx) == 4:
       if (100000 > area > 8000):
           rect += 1
   elif 5 <= len(approx) <= 6:
       if (100000 > area > 8000):
           tri += 1
       elif(len(approx) == 6):
           if (18000 > area > 1300):
               line += 1
   elif 7 < len(approx) < 25:
       if (100000 > area > 8000):
           circ += 1
   else:
       if (18000 > area > 1300):
           line += 1

im = Image.new("RGB", (512,512), (255,255,255))
fnt = ImageFont.truetype('arial.ttf', 40)
d = ImageDraw.Draw(im)

d.polygon((60,10,10,110,110,110),(255,0,0))
d.rectangle((10,120,110,220),(255,0,0))
d.line((60,230,60,330),(255,0,0),20)
d.ellipse((10,340,110,440),(255,0,0))
shapes = [tri, rect, line, circ]
i=0

while i<4:
   d.text((200,i*110+50), str(shapes[i]) , font=fnt, fill=(255,0,0))
   i+=1

im.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
