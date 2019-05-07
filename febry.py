import random as rand
import math
import csv
import statistics as st
datatest=[]
datatrain=[]
realtrain=[]
jdt=275
jm=7
with open('TrainsetTugas4ML.csv') as f:
	tmp=([[[y for y in x.split(",")] for x in a.split("\n")][0] for a in f])
	tmp.pop(0)
	datatrain=([[float(x) for x in a] for a in tmp])
def generatetrain():
	return ([datatrain[rand.randint(0,len(datatrain)-1)] for x in range(jdt)])
def getsdrt(x):
	return st.stdev(x),st.mean(x)
def maketrain():
	return ([generatetrain() for x in range(jm)])
realtrain=maketrain()
with open('TestsetTugas4ML.csv') as f:
	tmp=([[[y for y in x.split(",")] for x in a.split("\n")][0] for a in f])
	tmp.pop(0)
	datatest=([[x for x in a] for a in tmp])
count=1
for a in datatest:
	res=[]
	for i in range(jm):
		no=([x for x in realtrain[i] if x[len(x)-1]==2])
		yes=([x for x in realtrain[i] if x[len(x)-1]==1])
		jyes=len(yes)/len(realtrain[i])
		jno=len(no)/len(realtrain[i])
		for x in range(len(realtrain[i][0])-1):
			stdy,rty=getsdrt([y[x] for y in yes])
			stdn,rtn=getsdrt([y[x] for y in no])
			jyes*=(1/(stdy*math.sqrt(2*math.pi)))*math.exp(-( math.pow(float(a[x])-rty,2)/(2*stdy*stdy)))
			jno*=(1/(stdn*math.sqrt(2*math.pi)))*math.exp(-( math.pow(float(a[x])-rtn,2)/(2*stdn*stdn)))
		res.append(1) if jyes>=jno else res.append(2)
	print(count,'|',a[0],a[1],'|',1,'|') if res.count(1)>=res.count(2) else print(count,'|',a[0],a[1],'|',2,'|')
	count+=1