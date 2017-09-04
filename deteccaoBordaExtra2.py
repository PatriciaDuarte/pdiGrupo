import numpy as np
import cv2

imagem = cv2.imread('alanturing.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(imagem, (7, 7), 0)
canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 200)
resultado = np.vstack([np.hstack([imagem,    suave ]),np.hstack([canny1, canny2])]) 
cv2.imshow("Detector de Bordas Canny", resultado)
cv2.waitKey(0)
