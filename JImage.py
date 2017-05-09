from env import *
import numpy as np
from sqdist import sqdist
from JCalculation import JCalculation


def JImage(I,W):

    [m,n] = I.shape
    ws = W.shape[1]

    if ws == 9:
        d = 1
    elif ws == 17:
        d = 2
    elif ws ==32:
        d=4
    elif ws ==65:
        d=8

    wswidth = np.floor(ws/2)
    JI = np.zeros((m,n))

    for i in range(1, m+1):
        print i
        for j in range(1, n+1):
            x1 = i-wswidth
            x2 = i+wswidth
            y1 = j-wswidth
            y2 = j+wswidth
            if x1 < 1:
                x1 = 1
            if x2 > m:
                x2=m
            if y1 < 1:
                y1 = 1
            if y2 > n:
                y2=n

            wid = x2-x1+1
            hei = y2-y1+1

            if wid == ws and hei == ws:
                St = 1080
                M = [5, 5]
            else:
                reg = np.ones((wid, hei))
                reg = reg[::d, ::d]
                [wid, hei] = reg.shape
                M = np.array([np.mean(range(1,wid+1)), np.mean(range(1,hei+1))])
                [z2, z1] = reg.nonzero()
                z = np.array([z1, z2]).transpose()
                St = sum(sqdist(z.transpose(), M.T))

            block = zeros(ws, ws)
            block = I(range(x1,x2), range(y1,y2))
            JValue = JCalculation(block[::d, ::d], M, St)
            JI[i,j] = JValue

    return JI
