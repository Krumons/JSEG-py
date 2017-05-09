from env import *
import numpy as np


def sqdist(a,b):
    if a.shape[0]==1:
        print "STUFFF"
        d = np.kron(np.ones((1, b.size)),a) - np.kron(np.ones((a.size, 1)),b)
        d = d**2
    else:
        aa = sum(a*a, 0)
        bb = sum(b*b, 0)
        ab = np.dot(a.transpose(),b)
        bbdim = 1 if bb.ndim==0 else bb.ndim
        d = abs((np.kron(np.ones((1, bbdim)),aa.transpose()) + np.kron(np.ones((aa.ndim, 1)),bb)) - 2*ab)
    return d
