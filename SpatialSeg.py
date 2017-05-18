from env import *
import numpy as np
from sqdist import sqdist
from ValleyD import ValleyD
from ValleyG1 import ValleyG1

def SpatialSeg(JI, RS, wi):
    [m,n] = JI.shape
    ImgSeg = np.zeros((m,n))
    Sno = 0
    for r in range(1,max(RS.flatten(1)) + 1):
        Region = np.zeros((m,n))
        Region[Region == 0] = np.nan
        temp = []
        xy = RS == r
        Region[xy] = JI[xy]
        temp = JI[xy]
        u = sum(temp)/len(xy)
        s = temp.std(axis=0)

        Region = ValleyD(Region, wi, u, s)
        sq = Region.nonzero()
        Region[sq] = Region[sq] + Sno
        ImgSeg = ImgSeg + Region
        Sno = max(ImgSeg.flatten(1))
        ImgSeg = ValleyG1(JI, ImgSeg)
    return ImgSeg
