# multiprocessing 

from multiprocessing import Process, cpu_count
import time

def counter(num):
  count  = 0
  
  while count < num:
    count+=1

def main():
  cpu_0 = Process(target=counter, args=(20000000,))
  cpu_0.start()
  cpu_0.join()
  
  print('Fisnished in: ' + str(time.perf_counter())+' seconds')
  
  
if __name__ == '__main__':
  main()