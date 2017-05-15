from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage
from scipy.ndimage.morphology import binary_fill_holes
from build_heap import build_heap


def ValleyG2(JI, Region):
    [ m , n ] = JI.shape
    SegI = np.zeros((m,n))

    BRegion = ndimage.binary_dilation(Region, [[0,1,0],[1,1,1],[0,1,0]])
    Boundary = logical_and(BRegion, not Region)
    sq = Boundary.nonzero()
    JValue = JI[sq]

    [hp, hpid] = build_heap(JValue, sq)
    x_direction = [-1, 0, 1, 0]
    y_direction = [0, 1, 0, -1]

    while len(hp)
     #Continue here!


    return SegI
