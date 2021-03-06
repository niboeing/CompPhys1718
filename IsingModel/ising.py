#!/usr/bin/env python

import random,math,sys,time

from helpers import *

import numpy as np

g_La = 3 #obsolete
g_Lt = 3 #obsolete
	
# ising model

def GetNearestNeighbours(x,y):
	neighbours = list()
	L = GetSize()
	
	neighbours.append([(x-1)%(L-1),y])
	neighbours.append([x,(y-1)%(L-1)])
	neighbours.append([(x+1)%(L-1),y])
	neighbours.append([x,(y+1)%(L-1)])
	return neighbours

def InitRandomSpins():
	#creates a lattice of size L with randomly aligned spins
	L = GetSize()
#	lattice = np.empty((L,L),dtype=np.int)
	lattice = [[0 for i in range(L)] for j in range(L)]
	for i in range(L):
		for j in range(L):
			if random.randint(0,1)==0:
				lattice[i][j]=-1
			else:
				lattice[i][j]=1
	return lattice

def InitSpinDown():
	#creates a lattice of size L with all spins down
	L = GetSize()
	lattice = [[-1 for i in range(L)] for j in range(L)]
	return lattice

def InitSpinUp():
	#creates a lattice of size L with all spins up
	L = GetSize()
	lattice = [[1 for i in range(L)] for j in range(L)]
	return lattice

def CalcH(lattice):
	xmax = len(lattice)
	ymax = len(lattice[0])

	HSum = 0
	for x in range(xmax):
		for y in range(ymax-1):
			HSum+=lattice[x][y]*lattice[x][y+1]

	for y in range(ymax):
		for x in range(xmax-1):
			HSum+=lattice[x][y]*lattice[x+1][y]
	
	HSum = HSum*-1*GetJ()
	return HSum

def NextConfig(lattice):
	#DEPRECATED
	if lattice[g_La-1][g_Lt-1]==1:
		print 'Last config reached'
		sys.exit()
	for i in range(g_La):
		for j in range(g_Lt):
			if lattice[i][j]==-1:
				lattice[i][j]=1
				return lattice
			else:
				lattice[i][j]=-1

def GetSumOverAllConfigs():
	#DEPRECATED
	Ntot = 0
	lattice = InitZeroSpins()
	T = GetTemp()
	kB = GetKB()
	while(lattice[g_La-1][g_Lt-1]==-1):
		Ntot += math.exp(-CalcH(lattice)/(kB*T))
		lattice = NextConfig(lattice)
	return Ntot

def Magnetization(lattice):
	#calculates the magnetization of the current lattice with M = 
	msum = 0.
	L = len(lattice)
	for i in range(L):
		for j in range(L):
			msum += lattice[i][j]
	
	msum = abs(msum)/(L**2)
	return msum

def Magnetisation(lattice):
	return Magnetization(lattice)

def Metropolis(lattice,J,T):
	L = len(lattice)
	for i in range(L**2):
#		x1 = random.randint(0,L-1)
#		x2 = random.randint(0,L-1)
		x1,x2 = random.randint(0,L-1),random.randint(0,L-1)
		s_x = lattice[x1][x2]
	 	Pacc = min(1,math.exp(-2*J/T*s_x*(lattice[(x1-1)%(L-1)][x2] + lattice[x1][(x2-1)%(L-1)] + lattice[(x1+1)%(L-1)][x2] + lattice[x1][(x2+1)%(L-1)])))
#		delH = -J*(-2*nSum)
#		Pacc = min(1,math.exp(-delH/T))
#		r = random.uniform(0,1)
#		if r<Pacc:
		if random.uniform(0,1)<Pacc:
			lattice[x1][x2]=-s_x
	return lattice

