import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)

U = []

Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###
lenghtOfList=0
average=0
while lenghtOfList<50000: 
    variance=0
    num=np.random.rand()
    U.append(num)
    Xa.append(num**(0.5))
    lenghtOfList+=1
    average=(average)*(lenghtOfList-1)/lenghtOfList+((num**(0.5))/lenghtOfList)
    av_Xa.append(average)
    for i in range(lenghtOfList):
        variance+=(Xa[i]-av_Xa[lenghtOfList-1])**2
    vr_Xa.append(variance/lenghtOfList)


# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
plt.figure()
plt.plot(av_Xa)
plt.figure()
plt.plot(vr_Xa)
plt.show()

# Plot the average and variance values.
### YOUR CODE HERE ###


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
### YOUR CODE HERE ###
lenghtOfList2=0
while lenghtOfList2<50000:
    num2=np.random.rand()
    if num2>2*U[lenghtOfList2]:
        pass
    else:
        Xb.append(U[lenghtOfList2])
        if lenghtOfList2==0:
            av_Xb.append(Xb[lenghtOfList2])
            vr_Xb.append(0)
        else:
            av_Xb.append((Xb[lenghtOfList2-1]*(lenghtOfList2-1)+Xb[lenghtOfList2])/lenghtOfList2)
            vr_Xb.append(np.var(Xb))
        lenghtOfList2+=1
# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
plt.figure()
plt.plot(av_Xb)
plt.figure()
plt.plot(vr_Xb)
plt.show()