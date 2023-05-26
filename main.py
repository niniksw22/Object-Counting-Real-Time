import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear    
stream = CamGear(source='https://www.youtube.com/watch?v=B0YjuKbVZ5w', stream_mode = True, logging=True).start() # YouTube Video URL as input
#https://www.youtube.com/watch?v=En_3pkxIJRM
count=0
while True:
    frame = stream.read()
    count += 1
    if count % 6 != 0:
        continue
 
    frame=cv2.resize(frame,(1020,600))
    bbox,label,conf=cv.detect_common_objects(frame)
    frame=draw_bbox(frame,bbox,label,conf)
    c=label.count('car')
    P=label.count('PERSON')
    cv2.putText(frame,str(c),(50,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    cv2.putText(frame,str(P),(90,85),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
stream.release()
cv2.destroyAllWindows()
