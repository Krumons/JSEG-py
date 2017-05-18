from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy.ndimage import label
import time

def ValleyD(JI, scale, uj, sj):
    [ m , n ] = JI.shape
    a = [-0.6, -0.4, -0.2, 0, 0.2, 0 , 4]
    minsize = [32, 128, 512, 2048]
    scale = minsize[scale-1]
    MaxVSize = 0
    ValleyI = np.zeros((m,n))
    for i in range(0, len(a)):
        TJ = uj + a[i]*sj
        VP = np.zeros((m,n), dtype=np.bool)
        VP = np.less_equal(JI, TJ)
        VP_lab = np.asarray(sp.ndimage.label(VP))[0]
        VPlab_hist = np.digitize(VP_lab, range(0, VP_lab.max()))
        sq = (VPlab_hist >= scale)
        VSize = len(sq)
        if VSize > MaxVSize:
            ValleyI = np.zeros((m,n))
            for k in range(1,VSize):
                ValleyI[(VP_lab==sq[k]).nonzero()] = k
            MaxVSize = VSize

    import scipy.misc
    return ValleyI
