import numpy as np
import sys

numz = 81

#account for the index starting at zero...
data = np.loadtxt(str(sys.argv[1]))
coups = data[:,2]
count=1
for i in range(1,coups.shape[0]+1):
  print coups[i-1],
  if (count%6==0):
    count=1
    print
    continue
  else:
    count += 1
  if (i%numz==0):
    print
    count=1

