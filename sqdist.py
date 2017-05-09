from env import *
import numpy as np


def sqdist(a,b):
    aa = sum(a*a, 0)
    bb = sum(b*b, 0)
    print a
    print b
    ab = a*b
    print ab
    d = abs(np.kron(np.ones([0, np.size(b, axis=1)]),aa.transpose()) + np.kron(np.ones([np.size(aa, axis=1), 0]),bb) - 2*ab)
    return d

# Kapec matlab ab matricai ir 25x1 izmers python 25*2 use np.dot(a,b) or smth????
