import cv2
import numpy as np
 
imagem = cv2.imread('bird.jpg')

# Aplica os respectivos filtros
kernel = np.ones((6,6),np.float32)/25
filter2D = cv2.filter2D(imagem,-1,kernel)
blur = cv2.blur(imagem,(5,5))
gaussianBlur = cv2.GaussianBlur(imagem,(5,5),0)
median = cv2.medianBlur(imagem,5)
bilateralFilter = cv2.bilateralFilter(imagem,9,75,75)

# Escreve o nome de cada filtro na imagem correspondente
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'Imagem original',(5,320), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(filter2D,'Filter 2D',(45,320), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(blur,'Blur',(80,320), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(gaussianBlur,'Gaussian Blur',(10,320), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(median,'Median',(60,320), font, 1, (0,0,255), 2, cv2.LINE_AA)
cv2.putText(bilateralFilter,'Bilateral Filter',(10,320), font, 1, (0,0,255), 2, cv2.LINE_AA)

# Concatena as imagens para gerar a imagem de saida
imagemTemporaria1 = np.concatenate((imagem, median, gaussianBlur), axis=1)
imagemTemporaria2 = np.concatenate((bilateralFilter, blur, filter2D), axis=1)
imagemFinal = np.concatenate((imagemTemporaria1, imagemTemporaria2), axis=0)

cv2.imwrite("bird1.png", imagemFinal)
cv2.imshow("Final Image", imagemFinal)
cv2.waitKey(0)
