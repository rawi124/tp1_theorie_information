import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Im = Image.open('lena.jpeg')
Imarray = np.asarray(Im)
print(Imarray)
#numpy.asarray()La fonction est
#utilisée lorsque nous voulons convertir une entrée en un tableau

plt.figure()
#La fonction plt.figure crée une nouvelle figure
#(dont le numéro de figure est le nombre passer à la fonction en argument).
plt.imshow(Imarray, cmap='gray')
#La fonction imshow() du module pyplot de la bibliothèque matplotlib
#est utilisée pour afficher les données sous forme d’image

# Calculer et afficher la densité de probabilité de l'image
xe = np.asarray(range(np.amax(Imarray[:])+2))
H1, xe = np.histogram(Imarray.reshape(-1), bins=xe)
P1 = H1/Imarray.size
print(P1)
plt.figure()
plt.plot(P1)
