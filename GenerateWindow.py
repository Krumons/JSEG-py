from env import *
import numpy as np


def GenerateWindow(scale):
    window = np.ones((65,65))
    lu = np.ones((32,32))

    j=0
    i = 24

    while i>=10:
         lu[j,0:i] = 0;
         lu[0:i,j] = 0;
         j += 1;
         i -= 2

    lb = np.rot90(lu)
    rb = np.rot90(lb)
    ru = np.rot90(rb)

    window[0:32, 0:32] = lu
    window[0:32, 33:65] = ru
    window[33:65, 0:32] = lb
    window[33:65, 33:65] = rb

    w4 = window;
    w3 = w4[0::2, 0::2]
    w2 = w3[0::2, 0::2]
    w1 = w2[0::2, 0::2]

    if scale==4:
        W = w4
    elif scale==3:
        W = w3
    elif scale==2:
        W = w2
    else:
        W=w1

    return W
