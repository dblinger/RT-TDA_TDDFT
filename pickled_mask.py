from __future__ import division
from scipy.linalg import expm
from scipy.io import FortranFile
import numpy as np
import pickle
import sys


noc=5 # number doubly occ orbs
nst=100 # just excited states	
nbf=25 # number basis functions
nvir=nbf-noc
nov=noc*nvir
Xfile = FortranFile('Xmat.dat', 'r')
# Xmat.dat holds the transition density for nst many states
X = np.transpose(Xfile.read_reals(dtype=np.float).reshape((nst,nov)))
listlist=[]
for j in range(nst):
  print j
  NZ=[]
  for ia in range(nov):
    if np.abs(X[ia,j])>1.e-2:
      NZ.append(ia)
  print len(NZ)
  listlist.append(NZ) 

with open('mask.pkl', 'wb') as f:
  pickle.dump(listlist, f)
 
