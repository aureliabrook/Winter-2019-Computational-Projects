#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:11:56 2019

@author: aureliabrook
"""
#NATURAL UNITS: Distance[AU]. Time[Years], Mass[Solar Masses]
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Declaring constants and parameters

NBODIES = 4
pi = np.pi 
G = 4*pi**2

M_EARTH = 1e-6
M_MOON = 1e-8
M_JUP = 3e-5
M_SUN = 1

D_EARTH =  1
D_MOON = 1e-3
D_JUP = 2

V_EARTH = np.sqrt((G*M_SUN)/D_EARTH)#circular orbits
V_MOON = V_EARTH + np.sqrt(G*M_EARTH/D_MOON)
V_JUP = np.sqrt(G*M_SUN/D_JUP)


#Initializing variables

DURATION = 5
NSTEPS = 100000
dt = DURATION/NSTEPS #integration parameters

r = np.zeros([NSTEPS, 3*NBODIES])
v = np.zeros([NSTEPS, 3*NBODIES])
a = np.zeros([NSTEPS, 3*NBODIES])
m = [M_SUN, M_EARTH, M_MOON, M_JUP]

r[0] = [0, 0, 0, D_EARTH, 0, 0, D_EARTH + D_MOON, 0, 0, D_JUP, 0, 0]
v[0] = [0, 0, 0, 0, V_EARTH, 0, 0, V_MOON, 0, 0, V_JUP, 0]


#loop to calculate initial accelerations

for j in range(NBODIES):
    for k in range(NBODIES):
        if j != k:
            dr = r[0, j*3 : j*3 + 3] - r[0, k*3 : k*3 + 3]
            r_mag = np.sqrt(sum(dr*dr))
            a[0, j*3 : j*3 + 3] = a[0, j*3 : j*3+3] + -G*m[k]*dr/r_mag**3
            

#Numerical integration (Euler)
for i in range(1, NSTEPS):
    for j in range(NBODIES):
        r[i, j*3 : j*3 + 3] = r[i-1, j*3 : j*3 + 3] + v[i-1, j*3 : j*3 + 3]*dt
        v[i, j*3 : j*3 + 3] = v[i-1, j*3 : j*3 + 3] + a[i-1, j*3 : j*3 + 3]*dt
    for j in range(NBODIES):
        for k in range(NBODIES):
            if j != k:
                dr = r[i, j*3 : j*3 + 3] - r[i, k*3 : k*3 + 3]
                r_mag = np.sqrt(sum(dr*dr))
                a[i, j*3 : j*3 + 3] = a[i, j*3 : j*3+3] + -G*m[k]*dr/r_mag**3
                

#3D Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot(r[:, 0], r[:, 1], r[:, 2])
ax.plot(r[:, 3], r[:, 4], r[:, 5])
ax.plot(r[:, 6], r[:, 7], r[:, 8])
ax.plot(r[:, 9], r[:, 10], r[:, 11])
plt.axis('equal')
plt.show()

''' 2D PLOTTING
fig, ax = plt.subplots()

ax.plot(r[:, 0], r[:, 1])
ax.plot(r[:, 3], r[:, 4])
ax.plot(r[:, 6], r[:, 7])
ax.plot(r[:, 9], r[:, 10])
plt.axis('equal')
plt.show()
'''

            
            
            
            
            
            