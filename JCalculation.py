from env import *
import numpy as np


def JCalculation(class_map, M, St):
    [m,n] = class_map.shape
    N = m*n
    Sw = 0

    for l in range(1,max(class_map.flatten(1))):
        [x,y] = (class_map==1).nonzero()
        if x.size == 0:
            continue

        m_l = [mean(x), mean(y)]
        m1 = kron(ones(x.size, 1),m_l)
        xy = [x, y]
        Dist1 = sum(diag(sqdist(xy.transpose(), m1.transpose())))
        Sw+= Dist1


    return (St-Sw)/Sw
