from env import *
import numpy as np
from sqdist import sqdist

def JCalculation(class_map, M, St):
    [m,n] = class_map.shape
    N = m*n
    Sw = np.float64(0.0)

    for l in range(1,max(class_map.flatten(1))):
        [x,y] = (class_map==1).nonzero()
        if x.size == 0:
            continue
        m_l = [np.mean(x), np.mean(y)]
        m1 = np.kron(np.ones([x.size, 1]),m_l)
        xy = np.array([x, y])
        Dist1 = np.sum(np.diag(sqdist(xy, m1.transpose())))
        Sw+= Dist1
    J = np.float64(St-Sw)/Sw
    return 0 if J==float('Inf') else J
