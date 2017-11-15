from ising import *

import time,random,math

from ROOT import TGraph,TCanvas

#timing
timeStart = time.clock()

#sheet 1
#lattice = InitRandomSpins()
#H = CalcH(lattice)

#sheet 2
#7b
#lattice = InitZeroSpins()

#N = 1/(GetSumOverAllConfigs()*g_La*g_Lt)
#magSum = 0.
#while(lattice[g_La-1][g_Lt-1]==-1):
#   magSum += math.exp(-CalcH(lattice)/(g_kB*g_T))*N*abs(GetSumOverSpins(lattice))
#   lattice = NextConfig(lattice)


#print 'Sum is ' + str(magSum)

#7c
listOfPoints = list()
lattice = InitZeroSpins()
counter = 1
magSum = 0.
normSum = 0.
c1 = TCanvas('c1','Magnetization',200,10,700,500)
graph = TGraph()
graph.Set(20)
while(True):
    if counter>4000:
        break
    if (counter%200==0):
        graph.SetPoint(counter/200,counter,magSum/(normSum*100))
        print str(magSum/(normSum*100))
    counter+=1
    magSum += math.exp(-CalcH(lattice)/(g_kB*g_T))*abs(GetSumOverSpins(lattice))
    normSum += math.exp(-CalcH(lattice)/(g_kB*g_T))
    lattice = NextConfig(lattice)

graph.Draw()
time.sleep(5000)
#print lattice
#print H

timeEnd = time.clock()
timeDelta = timeEnd - timeStart

print 'Time taken: ' + str(timeDelta) + ' seconds'
