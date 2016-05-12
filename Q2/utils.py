import os.path
from random import randrange
from sets import Set
from math import sqrt

vdm = []

def getDistance(a, b):
    return vdmDistance(a, b)

def euclideanDistance(a, b):
    return map(diferenceSquare, a, b)

def diferenceSquare(a, b):
    distance = (a - b)
    return distance * distance

def vdmDistance(a,b):
    return sqrt(sum(map(vdmSquare, a, b, vdm)))

def vdmSquare(a, b, dic):
    return sum([diferenceSquare(calcP(dic,clas,a), calcP(dic,clas,b)) for clas in dic.keys()])

def calcP(dic, clas, a):
    return dic[clas][a] if a in dic[clas] else 0
        

def createVdm(dataAll):
    data = [x[1] for x in dataAll]
    classes = list(Set([d[0] for d in dataAll]))
    for i in range(len(data[0])):
        ss = [d[i] for d in data]
        m = list(Set(ss))
        dicClass = {}
        for c in classes:
            ssFilter = [d[1][i] for d in dataAll if d[0] == c]
            dic = {}
            for s in m:
                dic[s] = float(ssFilter.count(s))/len(ssFilter)
            dicClass[c] = dic
        vdm.append(dicClass)


def normalize(data, classPoss):
    data = data.splitlines()
    data = [x.split(',') for x in data]
    f = []
    ma = []
    mi = []
    for i in range(len(data[0])):
        
        if(i != classPoss):
            m = [float(d[i]) for d in data]
            ma.append(max(m))
            mi.append(min(m))
        else:
            ma.append(1)
            mi.append(2)
    for i in range(len(data)):
        r = []
        for j in range(len(data[i])):
            if(j != classPoss):
                r.append((float(data[i][j]) - mi[j])/(ma[j]-mi[j]))
            else:
                r.append(data[i][j])
        data[i] = str(r).replace('[','').replace(']','').replace("'",'').replace(' ','')
    return data





def separateData(database, tax):
    dirName = database[:database.index('.')]
    if(not os.path.isdir(dirName)): 
        data = []
        with open(database) as f:
            data = f.read().splitlines()
        print 'Database size '+str(len(data))
        print 'Separating '+str(int(len(data)*tax))+' cases for traning set'
        print 'Separating '+str(int(len(data)*(1-tax)))+' cases for test set'
        testSize = int(len(data)*(1-tax))
        test = []
        os.mkdir(dirName)
        while(testSize > 0):
            testSize -= 1
            test.append(data.pop(randrange(len(data))))
        with open(dirName+'\\Traning.data','w') as traningf:
            traningf.write('\n'.join(data))
            traningf.close()
        print dirName+'\\Traning.data Created'
        with open(dirName+'\\Testing.data','w') as testf:
            testf.write('\n'.join(test))
            testf.close()
        print dirName+'\\Testing.data Created'
        return dirName
    else:
        print 'Database already separated'
        return dirName
