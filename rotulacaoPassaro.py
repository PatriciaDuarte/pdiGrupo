from skimage import measure
import cv2
import numpy as np

img = cv2.imread('bird.jpg',0)
#aplica a rotulação da imagem
label = measure.label(img)

# Escreve o nome do filtro na imagem correspondente
font = cv2.FONT_HERSHEY_SIMPLEX
finalImage = cv2.putText(label,'Rotulação de imagem',(45,320), font, 1, (0,0,255), 2, cv2.LINE_AA)

# Salva a imagem
cv2.imwrite("bird1.png", finalImage)
# Mostra a imagem final concatenada
cv2.imshow("Final Image", finalImage)
# Aguarda tecla para finalizar
cv2.waitKey(0)
