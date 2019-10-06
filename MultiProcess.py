from multiprocessing import Process ,Manager
import datetime 
import time
import random
manager = Manager()
QA = manager.list()

def detect():
  while True:
    QA.append(random.randrange(2,10,1))
    print("New detect = ",QA[-1])
    time.sleep(1)
    #print(QA)

def teakQA():
  while True:
    if(len(QA) > 0):
      now=datetime.datetime.now()
      print(QA[0],"Start @",'%02d:%02d.%d'%(now.minute,now.second,now.microsecond))
      time.sleep(QA[0])
      now=datetime.datetime.now()
      print("Done @",'%02d:%02d.%d'%(now.minute,now.second,now.microsecond))
      del(QA[0])
      #print(QA)
if __name__ == "__main__":
    
    proc1 = Process(target=detect)
    proc2 = Process(target=teakQA)

    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()

