#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:02:53 2019

@author: aureliabrook
"""

import numpy as np
from PIL import Image

X = float(input("insert x coordinate: "))
Y = float(input("insert y coordinate: "))
ZOOM = float(input("what zoom percentage? "))/100
iter_max = max(500, int(1 + 100*ZOOM))

PIX_W = 800
PIX_H = 600
COLOR = (0, 125, 255) #Cyan

print("\nplz wait, am calculating...")
MSET = Image.new('RGB', (PIX_W, PIX_H))
PIX = MSET.load()
ESC = {}

def mand_set(a, b):
    a_iter = a
    b_iter = b
    tempB = 0.0
    norm = (a**2 + b**2)**0.5
    for it_num in range (1, iter_max):
        tempB = 2*a_iter*b_iter + b
        a_iter = a_iter**2 - b_iter**2 + a
        b_iter = tempB
        norm = (a_iter**2 + b_iter**2)**0.5
        if (norm > 2):
            return it_num
    return -1
        
def pix_to_comp(px, py, max_esc):
    n = ESC[(px, py)]
    if (n != -1):
        rate = np.exp(np.log(n)/np.log(max_esc) - 1)
        PIX[px, py] = (int(rate*0), int(rate*125), int(rate*255))
    else:
        PIX[px, py] = (0,0,0)
    
def create():
    max_esc = -1
    for i in range (PIX_W):
        for j in range(PIX_H):
            x = (4 * i / PIX_W - 2) / ZOOM + X
            y = (2 - 4 *  j / PIX_H) / ZOOM + Y
            esc = mand_set(x, y)
            ESC[(i, j)] = esc
            if esc > max_esc:
                max_esc = esc
    for i in range (PIX_W):
        for j in range(PIX_H):
            pix_to_comp(i, j, max_esc)
    MSET.save('MandelbrotSet, X: ' + str(X) + ', Y: ' + str(Y) + ', Z: ' + str(ZOOM) + '.png')
    MSET.show()
    
create()