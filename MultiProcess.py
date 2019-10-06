from multiprocessing import Process ,Manager
import datetime 
import time
import random
import sys

def detect(QA):
  while True:
    sys.stdout.flush()
    QA.append(random.randrange(2,10,1))
    #sys.stdout.write("New detect = ",QA[-1])
    print("New detect = ",QA[-1])
    sys.stdout.flush()
    time.sleep(1)
    #print(QA)

def teakQA(QA):
  while True:
    if(len(QA) > 0):  
      sys.stdout.flush()
      now=datetime.datetime.now()
      print(QA[0],"Start @",'%02d:%02d.%d'%(now.minute,now.second,now.microsecond))
      sys.stdout.flush()

      time.sleep(QA[0])
      now=datetime.datetime.now()
      print("Done @",'%02d:%02d.%d'%(now.minute,now.second,now.microsecond))
      sys.stdout.flush()
      
      del(QA[0])
      #print(QA)

if __name__ == "__main__":
    QA = Manager().list()
    proc1 = Process(target=detect ,args=(QA,),)
    proc2 = Process(target=teakQA,args=(QA,),)
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()

    

