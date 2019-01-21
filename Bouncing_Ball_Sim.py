#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:02:49 2019

@author: aureliabrook
"""

import matplotlib.pyplot as plt
import numpy as np

#variables
g = -9.8 #m/s**2
h0 = 3 #meters
x0 = 0 #meters
vy0 = 0 #m/s
vx0 = 0 #m/s

#integration parameters
duration = 30 #seconds
nsteps = 3000 #steps
dt = duration/nsteps #seconds

#initial conditions
position = np.zeros([nsteps, 2])
velocity = np.zeros([nsteps, 2])
position[0] = [x0, h0]
velocity[0] = [vx0, vy0]

#integration loop
for i in range(1, nsteps):
    position[i, 0] = position[i-1, 0] + velocity[i-1, 0]*dt
    position[i, 1] = position[i-1, 1] + velocity[i-1, 1]*dt

    velocity[i, 0] = velocity[i-1, 0]
    velocity[i, 1] = velocity[i-1, 1] + g*dt
    
    if position[i, 1] <= 0:
        velocity[i, 1] = -velocity[i, 1]
        

for i in range(0, nsteps):
    plt.cla()
    plt.scatter(position[i, 0], position[i, 1])
    plt.axis((-1, 1, -0.1, 3.5))
    plt.pause(1e-15)
plt.show()

