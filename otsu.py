import cv2
import numpy as np

#abre a imagem
img = cv2.imread('bird.jpg',0)
#aplica o thresholding metodo de otsu
ret,thresholding = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Escreve o nome do filtro na imagem correspondente
font = cv2.FONT_HERSHEY_SIMPLEX
finalImage = cv2.putText(thresholding,'Limiarizacao usando metodo de otsu',(45,320), font, 1, (0,0,255), 2, cv2.LINE_AA)

# Salva a imagem
cv2.imwrite("bird1.png", finalImage)
# Mostra a imagem final 
cv2.imshow("Final Image", finalImage)
# Aguarda tecla para finalizar
cv2.waitKey(0)
