import numpy as np
import sys

numx = 21
numy = 21
numz = 6

#note this only works because there are exactly 6 z points
data = np.loadtxt(str(sys.argv[1]))
coups = data[:,2]
for i in range(coups.shape[0]):
  print coups[i],
  if (i+1)%5==0: print


