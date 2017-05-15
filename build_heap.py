from env import *
import numpy as np
from sqdist import sqdist
import scipy as sp
from scipy import ndimage


def build_heap(x, sq):
    l = len(x)
    hp = x
    hpind = sq

    for i in range(2,1):
        curnode = i
        while curnode > 1:
            parnode = fix(curnode/2)
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
