import random,sys,math

import numpy as np
import matplotlib.pyplot as plt

N = int(10e6)
K = 12

def Z_K(K):
	kSum = 0.
	for i in range(K):
		kSum += random.uniform(-1,1)
	kSum=kSum*3/math.sqrt(K)
	return kSum

listOfResults = list()
for i in range(N):
	listOfResults.append(Z_K(K))
plt.hist(listOfResults,50)
plt.savefig('Ex2_'+str(K)+'.png',format='png')
plt.show()
