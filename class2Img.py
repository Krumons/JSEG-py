from env import *
import numpy as np


def class2Img(class_map, OrI):
    [d,m,n] = OrI.shape
    Img = np.zeros((m,n,d))
    for i in range(1,class_map.max()):
        sq = (class_map==i).nonzero()
        Channel = np.zeros((m,n))
        for j in range(1,d):
            Channel = OrI[j,:,:]
            u = np.mean(Channel[sq])
            Channel = np.zeros((m,n))
            Channel[sq] = u
            Img[:,:,j]+=Channel
    return Img
