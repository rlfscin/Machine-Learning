from kNN import k_NN
from utils import *
import os.path
import sys, time

graphic = False
try:
    import matplotlib.pyplot as plt
    graphic = True
except:
    print 'Attention: impossible to plot the graph, verify if you have matplotlib correctly installed.'

def __init__():
    start = time.time()
    database = "data\\fertility_Diagnosis.data"
    tax = 0.8 #taxa de separacao entre o tamanho do treino e teste
    classPos = 9
    ks = [1,2,3,5,7,9,11,13,15]
    if(len(sys.argv) > 1):
        database = sys.argv[1]
    if(os.path.isfile(database)):
        print 'Preparing data from file '+database
        basePath = separateData(database, tax)
        if(os.path.isfile(basePath+'\\Traning.data')):
           knn = None
           with open(basePath+'\\Traning.data') as f:
               knn = k_NN(f.read().splitlines(),classPos)
           with open(basePath+'\\Testing.data') as f:
               data = f.read()
               p = 0.0
               c = 0
               acuracyWith = [0]*len(ks)
               acuracyWithout = [0]*len(ks)
               lines = data.splitlines()
               for a in lines:
                   a = a.split(',')
                   c = knn.getClass(a, ks, True)
                   right = [1 if element == a[classPos] else 0 for element in c] 
                   acuracyWith = map(lambda x, y: x + y,acuracyWith, right)
               acuracyWith = map(lambda x : float(x) / len(lines), acuracyWith)
               for a in lines:
                   a = a.split(',')
                   c = knn.getClass(a, ks, False)
                   right = [1 if element == a[classPos] else 0 for element in c] 
                   acuracyWithout = map(lambda x, y: x + y,acuracyWithout, right)
               acuracyWithout = map(lambda x : float(x) / len(lines), acuracyWithout)
               print 'Time ' + str(time.time() - start)
               if(graphic):
                   plt.title('Acuracy vs K-constant')
                   plt.xticks(range(len(ks)), ks)
                   plt.plot(acuracyWith, label = 'Weight')
                   plt.plot(acuracyWithout, label = 'No Weight')
                   plt.ylabel('Acuracy')
                   plt.xlabel('k-constants')
                   plt.legend(loc='best',shadow=True)
                   plt.show()
               print 'acuracy '+ str(zip(ks, acuracyWith))
               print 'acuracy '+ str(zip(ks, acuracyWithout)) 
        else:
           print 'Traning set doesn\'t found, please remove the folder '+basePath+' and try again'
       
    else:
        print 'File doesn\'t found' 

if __name__ == '__main__':
    normal = False
    if(normal):
        database = "data\data_banknote_authentication.data"
        with open(database) as f:
            data = f.read()
        data = normalize(data,4)
        with open(database,'w') as f:
            f.write('\n'.join(data))
        print 'Database normalized'
    else:
        __init__()
        
    
