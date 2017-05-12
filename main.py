from env import *
import numpy as np
import scipy.io as sio
from scipy.cluster.vq import kmeans2,whiten
from GenerateWindow import GenerateWindow
from JImage import JImage
from class2Img import class2Img
from ValleyD import ValleyD

image = open_tiff('seg.jpg').ReadAsArray()

[d,m,n] = image.shape
X = image.reshape(d, n*m).transpose()
[M,P] = kmeans2(X,16)
map = P.reshape(m,n)

JImages = []

# for w in range(1, 5):
#      W = GenerateWindow(w)
#      JI = JImage(map,W)
#      JImages.append(JI)

W = GenerateWindow(1)
JI = JImage(map,W)
JImages.append(JI)

#JImages.append(sio.loadmat('2.mat'))
np.savetxt("foo.csv", JI, delimiter=",")



ImQ = class2Img(map, image)
Region = np.zeros((m,n))

#Scale1

u = np.mean(JImages[0])
s = JImages[0].std(axis=0)
Region = ValleyD(JImages[0], 4, u, s)
