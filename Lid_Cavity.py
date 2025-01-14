# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 01:55:21 2024

@author: HP
"""

import numpy as np
import math
from time import process_time
import matplotlib.pyplot as plt
W=[[0 for col in range(51)] for row in range(51)]
S=[[0 for col in range(51)] for row in range(51)]
for i in range(0,50):
    S[0][i]=0
    S[i][0]=0
    S[50][i]=0
    S[i][50]=0
iterr=0
while iterr>=0:
    S_=[[0 for col in range(51)] for row in range(51)]
    for i in range(0,51):
        for j in range(0,51):
            S_[i][j]=S[i][j]
    W_=[[0 for col in range(51)] for row in range(51)]
    for i in range(0,51):
        for j in range(0,51):
            W_[i][j]=W[i][j]
    for i in range(1,50):
        
        for j in range(1,50):
            
            S[i][j]=(1/4)*(S[i-1][j]+S[i+1][j]+S[i][j-1]+S[i][j+1]+W[i][j]*(1/2500))
    for i in range(1,50):
        W[i][0]=(-2*2500)*(S[i][1]-S[i][0])
        W[50][i]=(-2*2500)*(S[49][i]-S[50][i])
        W[i][50]=(-2*2500)*(S[i][49]-S[i][50])
        W[0][i]=(-2*2500)*(1*50+S[1][i]-S[0][i])
        W_[i][0]=(-2*2500)*(S[i][1]-S[i][0])
        W_[50][i]=(-2*2500)*(S[49][i]-S[50][i])
        W_[i][50]=(-2*2500)*(S[i][49]-S[i][50])
        W_[0][i]=(-2*2500)*(1*(1/50)+S[1][i]-S[0][i])

    s=0
    for i in range(1,50):
        for j in range(1,50):
            W[i][j]=W_[i][j]+(0.01)*((W_[i-1][j]+W_[i+1][j]+W_[i][j-1]+W_[i][j+1]-4*W_[i][j])*(25)-(-S[i][j+1]+S[i][j-1])*(-W_[i+1][j]+W_[i-1][j])*(625)-(S[i-1][j]-S[i+1][j])*(W_[i][j+1]-W_[i][j-1])*(625))
            s=s+abs(S[i][j]-S_[i][j])
    
    if s<0.01 and iterr>0:
        
        break
    iterr=iterr+1

St=[[0 for col in range(51)] for row in range(51)]
for i in range(0,51):
    for j in range(0,51):
        St[i][j]=S[50-i][j]
vo=[[0 for col in range(51)] for row in range(51)]
for i in range(0,51):
    for j in range(0,51):
        vo[i][j]=W[50-i][j]

z=plt.contour(St,levels=np.arange(-0.12,0.1,0.01))
plt.colorbar(z,label="Streamlines")
plt.show()
c=plt.contour(vo,levels=np.arange(-5,7,1))
plt.colorbar(c,label="Vorticity Contours")
plt.show()

U=[]
V=[]
V.append(0)
for i in range(1,50):
    u=(-S[i+1][25]+S[i-1][25])/(2/50)
    v=-1*(S[25][i+1]-S[25][i-1])/(2/50)
    U.append(u)
    V.append(v)
V.append(0)
plt.plot(V)
plt.xlabel("Distance from left")
plt.ylabel("Vertical Velocity")
plt.show()
U_=[]
U_.append(0)
for i in range(0,49):
    U_.append(U[48-i])
U_.append(1)
plt.plot(U_)
plt.xlabel("Distance from bottom")
plt.ylabel("Horizontal Velocity")
plt.show()
P=[[0 for col in range(51)] for row in range(51)]

r=1
k=0
t1_start=process_time()
cnt=0
while k>=0:
    P_past=[[0 for col in range(51)] for row in range(51)]
    for i in range(0,51):
        for j in range(0,51):
            P_past[i][j]=P[i][j]
    for i in range(1,50):
        P[i][0]=(0.25)*(P[i-1][0]+P[i+1][0]+2*P[i][1])
        P[i][50]=(0.25)*(P[i-1][50]+P[i+1][50]+2*P[i][49])
        P[0][i]=(0.25)*(P[0][i-1]+P[0][i+1]+2*P[1][i])
        P[50][i]=(0.25)*(P[50][i-1]+P[50][i+1]+2*P[49][i])

    

    

    for i in range(1,50):
        for j in range(1,50):
            P[i][j]=(0.25)*(P[i+1][j]+P[i-1][j]+P[i][j+1]+P[i][j-1]-2*(r*2500)*((S[i-1][j]+S[i+1][j]-2*S[i][j])*(S[i][j+1]+S[i][j-1]-2*S[i][j])-((0.25)*(S[i-1][j+1]-S[i+1][j+1]-S[i-1][j-1]+S[i+1][j-1]))**2 ))
    s=0        
    for i in range(0,51):
        for j in range(0,51):
            s=s+abs(P[i][j]-P_past[i][j])
    print(s)
    if s<0.01:
        break

po=[[0 for col in range(51)] for row in range(51)]
for i in range(0,51):
    for j in range(0,51):
        po[i][j]=P[50-i][j]


d=plt.contour(po,levels=np.arange(-0.6,1,0.01))
plt.colorbar(d,label="Pressure Contours")
plt.show()