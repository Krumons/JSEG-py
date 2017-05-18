from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage
from scipy.ndimage.morphology import binary_fill_holes

def ValleyG1(JI, ValleyI):
    [ m , n ] = ValleyI.shape
    ValleyI = binary_fill_holes(ValleyI)
    SegI = ValleyI

    sq_remain = (ValleyI == 0)
    JHigh = JI[sq_remain]
    u = np.mean(JHigh)
    sq_medth = sq_remain[(JHigh < u)-1]

    se1 = ndimage.generate_binary_structure(2, 1)
    bw_ValleyI = ndimage.binary_dilation(ValleyI, se1)
    GArea = np.zeros((m,n), dtype=bool)
    GArea[sq_medth-1] = 1
    bw_GArea = np.asarray(sp.ndimage.label(GArea))[0]

    for t in range(1, bw_GArea.max()):
        sq = (bw_GArea == t)
        Areaval = bw_ValleyI[sq]
        tmp = np.unique(Areaval)
        numnnz = np.count_nonzero(tmp)
        if numnnz == 1:
            tmp = tmp[tmp>0]
            SegI[sq] = tmp
    return SegI.astype(int)
