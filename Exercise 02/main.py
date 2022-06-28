# file detection program
import os

path = 'C:\\files\\disk'

if os.path.exists(path):
  print('The {0} exists on the disk'.format(path))
  if os.path.isfile(path):
    print('And it is a file.')
  elif os.path.isdir(path):
    print('That is a diretory.')
else:
  print('Location does not exist!')
    
  


