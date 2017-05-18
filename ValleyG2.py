from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage
from scipy.ndimage.morphology import binary_fill_holes
from build_heap import build_heap
from heap_pop import heap_pop
from heap_add import heap_add


def ValleyG2(JI, Region):
    [ m , n ] = JI.shape
    SegI = np.zeros((m,n))
    BRegion = ndimage.binary_dilation(Region, [[0,1,0],[1,1,1],[0,1,0]])
    Boundary = np.logical_and(BRegion, np.logical_not(Region))
    sq = np.asarray(Boundary.ravel().nonzero())
    JValue = JI.flatten('F')[sq]
    [hp, hpid] = build_heap(JValue, sq)
    x_direction = [-1, 0, 1, 0]
    y_direction = [0, 1, 0, -1]

    while len(hp):
        try:
            [hp,hpid,minval, pos] = heap_pop(hp, hpid)
        except TypeError as e:
            if "object is not iterable" in str(e):
                break
        posy = int(np.fix((pos)/m))
        posx = int(pos - m * (posy))
        if not Region[posx, posy]:
            curval = BRegion[posx, posy]
            Region[posx, posy] = curval
            for k in range(0,4):
                x = posx + x_direction[k] - 1
                y = posy + y_direction[k] - 1
                if x > 0 and x <=m and y > 0 and y <= n:
                    if BRegion[x,y] == 0:
                        P = x + m * (y-1)
                        J = JI[x,y]
                        [hp,hpid] = heap_add(hp, hpid, J, P)
                        BRegion[x,y] = curval
    SegI = Region
    return Region.astype(int)
