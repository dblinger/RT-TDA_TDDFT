from __future__ import division
from scipy.linalg import expm
from scipy.io import FortranFile
import numpy as np
import sys
import itertools
Filename   = 'out.log'
data = np.genfromtxt(Filename)
hops=data[:,1]
print str(hops)
numhops=len(hops)
totalsteps=1000000
pops=np.zeros(7980)

for i in range(numhops):
  hopstep=int(hops[i])
  pops[hopstep]=pops[hopstep]+1.0
pops[0]=1000000
for i in range(1,7980):
  pops[i]=pops[i-1]-pops[i]
np.savetxt('num_hops_per_step.txt', np.transpose([pops]))  
