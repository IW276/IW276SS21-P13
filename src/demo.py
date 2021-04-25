import cv2
import gamma_correction
import numpy as np

imageNames = ['210425-141321-ka-markplatz-nord.jpg', '210425-153000-markt-dunkel.jpeg']
resultImage = None
axis = 0
for i, name in enumerate(imageNames):
    img = cv2.imread('../datasets/' + name, 0)
    img_gamma_corrected = gamma_correction.adjust_gamma(img)
    resultImage = np.concatenate((img, img_gamma_corrected), axis=1)
    cv2.imshow('name', resultImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
