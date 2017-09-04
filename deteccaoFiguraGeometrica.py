import numpy as np
import cv2

imagem = cv2.imread('bola.jpg')
cinza = cv2.imread('bola.jpg',0)

ret,thresh = cv2.threshold(cinza,127,255,1)

contornos,h = cv2.findContours(thresh,1,2)

for cnt in contornos:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==5:
        print ("Pentagono")
        cv2.drawContours(imagem,[cnt],0,255,-1)
    elif len(approx)==3:
        print ("Triangulo")
        cv2.drawContours(imagem,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print ("Quadrado")
        cv2.drawContours(imagem,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print ("MetadeCirculo")
        cv2.drawContours(imagem,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print ("Circulo")
        cv2.drawContours(imagem,[cnt],0,(0,255,255),-1)

cv2.imshow('imagem',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
