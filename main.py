from env import *
import numpy as np
import scipy.io as sio
from scipy.cluster.vq import kmeans2,whiten
from GenerateWindow import GenerateWindow
from JImage import JImage
from class2Img import class2Img
from ValleyD import ValleyD
from ValleyG1 import ValleyG1
from ValleyG2 import ValleyG2
import pickle

image = open_tiff('seg.jpg').ReadAsArray()

[d,m,n] = image.shape
X = image.reshape(d, n*m).transpose()
[M,P] = kmeans2(X,16)
map = P.reshape(m,n)

JImages = []

# for w in range(1, 5):
#     W = GenerateWindow(w)
#     JI = JImage(map,W)
#     JImages.append(JI)

ImQ = class2Img(map, image)
Region = np.zeros((m,n))

# with open('objs.pickle', 'w') as f:
#     pickle.dump(JImages, f)

with open('objs.pickle') as f:  # Python 3: open(..., 'rb')
    JImages = pickle.load(f)
#Scale4

u = np.mean(JImages[0])
s = JImages[0].std(axis=0)
Region = ValleyD(JImages[3], 4, u, s)
Region = ValleyG1(JImages[3], Region)
Region = ValleyG1(JImages[2], Region)
Region = ValleyG2(JImages[0], Region)
Region4 = Region
