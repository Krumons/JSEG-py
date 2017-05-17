from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage


def heap_pop(hp, hpind):
    hp = hp.ravel()
    hpind = hpind.ravel()
    if len(hp) - 1 == 0:
        return
    l = len(hp) - 1
    minval = hp[0]
    minind = hpind[0]
    hp[0] = hp[l]
    hpind[0] = hpind[l]
    l = l - 1
    hp = hp[range(0,l+1)]
    hpind = hpind[range(0,l+1)]
    curnode = 0
    halfl = int(np.fix(l/2))
    while curnode <= halfl:
        sonnode1 = curnode * 2
        sonnode2 = sonnode1 + 1
        val1 = hp[curnode]
        val2 = hp[sonnode1]
        if l > sonnode2:
            val3 = hp[sonnode2]
        else:
            val3 = np.inf
        if val1 > val2:
            if val2 > val3:
                stat = 3
            else:
                stat = 2
        else:
            if val1 > val3:
                stat = 3
            else:
                stat = 0

        if stat == 0:
            break
        elif stat == 3:
            hp[sonnode2] = val1
            hp[curnode] = val2
            tmp = hpind[curnode]
            hpind[curnode] = hpind[sonnode1]
            hpind[sonnode1] = tmp
            curnode = sonnode1
    return [hp, hpind, minval, minind]
