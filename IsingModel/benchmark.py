import time,timeit
from ising import *
from helpers import *

J = GetJ()
L = GetSize()
T = GetTemp()

if L==4:
	N=100000
elif L==10:
	N=10000
elif L==25:
	N=1000
else:
	N=100

print 'L=' + str(L) + ' N=' + str(N)
lattice = InitRandomSpins()
times = list()
for j in range(5):
	startTime = time.clock()
	for i in range(N):
		lattice = Metropolis(lattice,J,T)
	endTime = time.clock()
	times.append(endTime - startTime)
	print str(endTime - startTime) + ' seconds'

average = sum(times)/5
print 'Average over 5 runs: ' + str(average) + ' seconds'
print 'Interpolation for 1 million configs: ' + str(average*1000000/N) + ' seconds'
