import cv2
import numpy as np


imagem = cv2.imread('bird.jpg',0);
threshold = cv2.adaptiveThreshold(imagem,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,5)
novaImagem = threshold
novaImagem = cv2.medianBlur(novaImagem,5)
cv2.imshow("Imagem final:", novaImagem)
cv2.waitKey(0)
