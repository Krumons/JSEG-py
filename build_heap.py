from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage


def build_heap(x, sq):
    l = len(x)-1
    hp = np.asarray(x)
    print sq.shape
    hpind = np.asarray(sq)
    for i in range(1,l):
        curnode = i
        while curnode > 1:
            parnode = int(np.fix(curnode/2))
            if hp[parnode] > hp[curnode]:
                tmp = hp[parnode]
                hp[parnode] = hp[curnode]
                hp[curnode] = tmp

                tmp = hpind[parnode]
                hpind[parnode] = hpind[curnode]
                hpind[curnode] = tmp
                curnode = parnode
            else:
                break
    return [hp, hpind]
