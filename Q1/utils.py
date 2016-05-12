import os.path
from random import randrange



def getDistance(a, b):
    return sum(euclideanDistance(a, b))

def euclideanDistance(a, b):
    return map(diferenceSquare, a, b)

def diferenceSquare(a, b):
    distance = (a - b)
    return distance * distance

def dtw(a,b):
    pass


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
        print len(data)*(1-tax)
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
