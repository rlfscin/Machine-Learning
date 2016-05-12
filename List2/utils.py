import numpy as np
from math import *

def lqv1(x, p, t):
    p += (x - p)*t

def knn(data, p, k):
    dataSort = sorted([(distance(d,p),d) for d in data], key=lambda a: a[0])
    return np.array(dataSort[:k], dtype=tuple)

def separeteData(data, classPos):
    return np.array([(a[classPos], np.delete(a,classPos)) for a in data], dtype=tuple)

def distance(d, p):
    return np.vectorize(euclidian)(d[1],p).sum()
    
def euclidian(a, b):
    return (a-b)**2


classPos = 4
num_prot = 2
tax = 0.1
    
with open('data_banknote_authentication.data') as f:
    data = np.array([map(float, line.split(',')) for line in f.read().splitlines()])

data = separeteData(data, classPos)

print 'base'
print data

classes = np.unique(data[:,0])
print 'classes'
print classes
dataPerclass = []
for c in classes:
    idx = data[:,0] == c 
    dataPerclass.append(data[idx, :])
    
dataPerclass = np.array(dataPerclass)
print 'dataPerClass'
print dataPerclass

p = np.empty([0,data.shape[1]])
for d in dataPerclass:
    mask = np.random.randint(d.shape[0],size=num_prot)
    p = np.concatenate((p, d[mask, :]))
print 'prototipos'
print p

print 'knn'

for i in range(100):
    randNumber = np.random.randint(d.shape[0])
    d = data[randNumber]
    prot = knn(p, d[1], 1)[0]
    print 'escolhido'
    print prot
    lqv1(d[1], prot[1][1], tax)
    print p
    

#print knn(data, data[0][1], 20)


