import cv2
import numpy as np
rasm=cv2.imread('img.png')
burchak=-120
h, w = rasm.shape[:2]
markaz=(h//2, w//2)
matritsa=cv2.getRotationMatrix2D(markaz,burchak,1)
burish=cv2.warpAffine(rasm,matritsa,(w,h))
cv2.imshow("dastabk holatdagi rasm", rasm)
cv2.imshow("Burilgan rasm",burish)
cv2.waitKey(0)
cv2.destroyAllWindows()