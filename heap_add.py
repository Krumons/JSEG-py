from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage


def heap_add(hp, hpind, addval, addind):
    l = len(hp) - 1
    hp[l] = addval
    hpind[l] = addind
    curnode = l
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
