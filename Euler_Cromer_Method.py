#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Use of Euler-Cromer method to plot planetary orbits

import matplotlib.pylab as plt
import math
t = 0.00
dt= 0.001
x = 1.00
y = 0.00
v_x = 0.00
v_y = 4
lis_x = []
lis_y = []
    
def v_xi():
    return v_x - (4*(math.pi**2)*x/(r**3))*dt

def x_i():
    return x + v_xi(dt)*dt

def v_yi():
    return v_y - (4*(math.pi**2)*y/(r**3))*dt

def y_i():
    return y + v_yi(dt)*dt

while t < 10: 
    r = math.sqrt(x**2+y**2)
    v_x = v_xi()
    x = x + v_x*dt
    lis_x.append(x)
    v_y = v_yi()
    y = y + v_y*dt
    lis_y.append(y)
    t = t + dt

fig,ax = plt.subplots(1,1)
ax.set_aspect('equal')
plt.plot(lis_x,lis_y, 'b')
plt.xlabel('x position (AU)')
plt.ylabel('y position (AU)')
#plt.savefig('Eurler-cromer dt = 0.01 v = 2.png' )
plt.show()