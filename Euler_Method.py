#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pylab as plt
import math
t = 0.00
dt= 0.001
x = 1.00
y = 0.00
v_x = 0.00
v_y =  2.0*math.pi
lis_x = []
lis_y = []

def test():
    t = 0
    dt=0.01
    x = 1
    y = 0
    v_x = 0
    v_y = 2*math.pi
    r = 1
    print (t,dt,x,y,v_x,v_y,r)
    
def v_xi():
    return v_x - (4*(math.pi**2)*x/(r**3))*dt

def x_i():
    return x + v_xi(dt)*dt

def v_yi():
    return v_y - (4*(math.pi**2)*y/(r**3))*dt

def y_i():
    return y + v_yi(dt)*dt

fig,ax = plt.subplots(1,1)
while t < 5: 
    r = math.sqrt(x**2+y**2)
    vxold = v_x
    v_x = v_xi()
    x = x + vxold*dt
    lis_x.append(x)
    vyold = v_y
    v_y = v_yi()
    y = y + vyold*dt
    lis_y.append(y)
    t = t + dt
    
    
ax.set_aspect('equal')
plt.plot(lis_x,lis_y)
plt.show()