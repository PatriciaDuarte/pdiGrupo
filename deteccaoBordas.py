#importa as bibliotecas necessarias
import numpy as np
import cv2

#Pega a imagem que sera processada
imagem = cv2.imread('alanturing.jpg')
#Converte uma imagem de um espaco de cores para outra
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#Faz a desfocagem gaussiana
suave = cv2.GaussianBlur(imagem, (7, 7), 0)
#Faz a deteccao de bordas simples
canny1 = cv2.Canny(suave, 20, 120)
#Faz a deteccao de bordas simples
canny2 = cv2.Canny(suave, 70, 200)
#Atribui para resultado  as duas imagens com bordas simples
resultado = np.vstack([np.hstack([imagem,    suave ]),np.hstack([canny1, canny2])]) 
#imprime na tela as imagens com bordas simples
cv2.imshow("Detector de Bordas Canny", resultado)
cv2.waitKey(0)
