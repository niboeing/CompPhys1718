from ising import *
import time,math

from ROOT import TGraph,TCanvas

#exercise nr (4 or 6)
ex=6

#lattice size
L1 = 10
L2 = 10

#sample size
N = 10000

if ex==4:
	#estimate magnetisation using random configs
	sum1 = 0.
	sum2 = 0.
	c1 = TCanvas('c1','Dependence of Mag on sample size',200,10,700,500)
	graph = TGraph()
	graph.Set(N/1000)
	j=0
	for i in range(N):
		spinconfig = InitRandomSpins(L1,L2)
		mag = Magnetization(spinconfig)
		factor = math.exp(-CalcH(spinconfig)/(g_kB*g_T))
		sum1 += factor*mag
		sum2 += factor
		if i/1000==0:
			total = sum1/sum2
			graph.SetPoint(j,i,total)
			j+=1
	
	graph.Draw()
	c1.SaveAs('3.6_L='+str(L1)+'.png')
	time.sleep(5000)

if ex==6:
	#simple estimate with metropolis algorit
	magSum = 0.
	spinConfig = InitRandomSpins()
	#		c1 = TCanvas('c1','Mag using Metropolis',200,10,700,500)
	#		graph = TGraph()
	#		graph.Set(N/10)
	for i in range(N):
		if i%10==0:
			magSum+=Magnetization(spinConfig)
			print '|m|='+str(magSum/(i/10+1))
		spinConfig=Metropolis(spinConfig)
	#			if i%10==0:
	#				graph.SetPoint((i+1)/10,i,magSum/(i+1))
	print 'Magnetization estimate for L=' + str(L1) + ' and N=' + str(N) + ' is |m|=' + str(magSum/N)
#	graph.Draw()
#	time.sleep(5000)
		

	
