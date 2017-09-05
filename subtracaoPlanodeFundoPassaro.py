#Importa as bibliotecas que serao utilizadas no programa
import cv2
import numpy as np

#Pega a imagem q sera processada
imagem = cv2.imread('bird.jpg',0);
#Faz a limiarizacao da imagem
threshold = cv2.adaptiveThreshold(imagem,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,5)
#Atribui o thresholding para uma nova imagem
novaImagem = threshold
#Bloqueia uma imagem usando o filtro mediano
novaImagem = cv2.medianBlur(novaImagem,5)
#Manda a imagem para a saida
cv2.imshow("Imagem final:", novaImagem)
cv2.waitKey(0)
