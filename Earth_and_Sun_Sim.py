#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:58:15 2019

@author: aureliabrook
"""

#assuming mass of the planet is much less than the mass of a star
#and that the center of mass of the star is just the center of the star

import numpy as np
import matplotlib.pyplot as plt

#NATURAL UNITS: Distance[AU]. Time[Years], Mass[SM]

#constants :)
pi = np.pi
G = 4*pi**2
M_SUN = float(input("How big is your star in solar masses? "))
D_EARTH = 1
V_EARTH = 2*pi*D_EARTH/1

#integration parameters
DURATION = 5 #T = 4 * (pi**2) * (D_EARTH**3/2)
NSTEPS = 2000
dt = DURATION/NSTEPS 

#initialize variables
r = np.empty([NSTEPS, 3]) #position[x, y, z]
v = np.empty([NSTEPS, 3]) #velocity[x, y, z]
a = np.empty([NSTEPS, 3]) #acceleration[x, y, z]

#initial conditions
r[0] = [D_EARTH, 0, 0]
v[0] = [0, V_EARTH, 0]
R_MAG = np.sqrt(sum(r[0]*r[0]))
a[0] = -G * M_SUN * r[0] / R_MAG**3

#euler integration to move the planet
for i in range(1, NSTEPS):
    r[i] = r[i-1] + v[i-1] * dt
    v[i] = v[i-1] + a[i-1] * dt
    R_MAG = np.sqrt(sum(r[i]*r[i]))
    a[i] = -G * M_SUN * r[i] / R_MAG**3
    
fig, (ax1, ax2) = plt.subplots(1, 2, sharey = True)
ax1.plot(r[:, 0], r[:, 1])
ax1.plot(0, 0, 'r*')
ax1.axis('equal')


#movie 
for i in range(0, NSTEPS):
    plt.cla()
    plt.scatter(r[i, 0], r[i, 1], color='g')
    plt.plot(0, 0, 'r*')
    plt.axis((-1.5, 1.5, -1.5, 1.5))
    plt.pause(1e-20)
plt.show()