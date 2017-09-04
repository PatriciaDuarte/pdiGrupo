from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_doh
from skimage.color import rgb2gray
from skimage import color

import cv2
import numpy as np
import glob
import os


def load_images_from_folder(folder):
 images = []
 filenames = []
 for filename in os.listdir(folder):
  img = cv2.imread(os.path.join(folder,filename),0)
  if img is not None:
   filenames.append(filename)
   images.append(img)
 return images,filenames


imagens,nomes = load_images_from_folder("imagens");
for (src,nome) in zip(imagens,nomes):
 th2 = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,5)#subtracao de plano de fundo
 newImage = th2
 newImage = cv2.medianBlur(newImage,5)

 image = newImage
 blobs_doh = blob_doh(image,min_sigma=10, max_sigma=25, threshold=.0125,overlap=0.33)

 blobs = [blobs_doh]
 colors = ['black']
 titles = ['Rotulacao de Passaros']
 sequence = zip(blobs, colors, titles)

 for blobs, color, title in sequence:
  fig, ax = plt.subplots(1, 1)
  ax.set_title(title)
  ax.imshow(image, interpolation='nearest')
  for blob in blobs:
   y, x, r = blob
   c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
   ax.add_patch(c)
 print("Foram detectados " + str(len(blobs)) + " em " + "\"" + nome + "\"")
 plt.show()

