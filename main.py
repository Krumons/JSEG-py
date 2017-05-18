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
from SpatialSeg import SpatialSeg
import pickle

image = open_tiff('seg.jpg').ReadAsArray()

[d,m,n] = image.shape
X = image.reshape(d, n*m).transpose()
[M,P] = kmeans2(X,16, 100, 1e-01)
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

with open('objs.pickle') as f:
    JImages = pickle.load(f)

#Scale4
u = np.mean(JImages[3])
s = JImages[3].std(axis=0)
Region = ValleyD(JImages[3], 4, u, s)
Region = ValleyG1(JImages[3], Region)
Region = ValleyG1(JImages[2], Region)

Region = ValleyG2(JImages[0], Region)
Region4 = Region

#Scale3
w = 3
Region = SpatialSeg(JImages[2], Region, w)
Region = ValleyG1(JImages[1], Region)
Region = ValleyG2(JImages[0], Region)
Region3 = Region

#Scale2
w=2
Region = SpatialSeg(JImages[1], Region, w)
Region = ValleyG1(JImages[0], Region)
Region = ValleyG2(JImages[0], Region)
Region2 = Region

#scale1
w = 1
Region = SpatialSeg(JImages[0], Region, w)
Region = ValleyG2(JImages[0], Region)
Region1 = Region

import scipy.misc
scipy.misc.imsave('region.jpg', Region1)
