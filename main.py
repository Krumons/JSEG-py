from env import *
import numpy as np
from scipy.cluster.vq import kmeans2,whiten
from GenerateWindow import GenerateWindow
from JImage import JImage

image = open_tiff('seg.jpg').ReadAsArray()

[d,m,n] = image.shape
print d
print m
print n
X = image.reshape(d, n*m).transpose()
[M,P] = kmeans2(X,16)
map = P.reshape(m,n)

#for w in range(1, 5):
W = GenerateWindow(1)
JI = JImage(map,W)
