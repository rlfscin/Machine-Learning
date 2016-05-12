from utils import *
import time

class k_NN():

    def __init__(self):
        self.data = None        

    def __init__(self, data, classPos):
        self.registerTraningData(data,classPos)
    
    def registerTraningData(self, data, classPos):
        data = [a.split(',') for a in data]
        self.data = [(a.pop(classPos),map(float,a)) for a in data]
        self.classPos = classPos
        
    def getClass(self, pattern, ks,useWeight):
        start1 = time.time()
        p = pattern[:]
        p.pop(self.classPos)
        p = map(float,p)    
        if(self.data is not None):
            distance = []           
            for d in self.data:
                ret = getDistance(p, d[1])
                distance.append((d[0],1.0/(1+ret)))                
            kElements = sorted(distance, key = lambda a: a[1], reverse = True)[:ks[-1]]
            kClass = []
            for k in ks:
                kElement = kElements[:k]
                classes = {}
                for e in kElement:
                    if(useWeight):
                        classes[e[0]] = classes.get(e[0],0) + e[1]
                    else:
                        classes[e[0]] = classes.get(e[0],0) + 1
                kClass.append(max(classes.items(),key = lambda a: a[1])[0])
            return kClass
        else:
            print("Error: There is no database")
            return None


