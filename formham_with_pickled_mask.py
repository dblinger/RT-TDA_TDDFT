from __future__ import division
from scipy.linalg import expm
from scipy.io import FortranFile
import numpy as np
import sys
import pickle

PCname=str(sys.argv[1])
print PCname
noc=5#number doubly occ orbs
nstmax=100# number excited states in the X.dat
nst=100# number of states to compute couplings for 
nbf=25
nvir=nbf-noc
nov=noc*nvir
H = FortranFile(PCname+'.dat', 'w')
Vfile = FortranFile(PCname, 'r')
Xfile = FortranFile('Xmat.dat', 'r')
# Xmat.dat holds the transition density for nstmax many states
X = np.transpose(Xfile.read_reals(dtype=np.float).reshape((nstmax,nov)))
#
#  Recover the mask from pickle
#
with open('mask.pkl', 'rb') as f:
  listlist = pickle.load(f)
#
# Create np array for Hamiltonian in the adiabatic basis
#

ham=np.zeros((nst+1,nst+1))

grid = Vfile.read_reals(dtype=np.float)
gsexp = Vfile.read_reals(dtype=np.float)
PC = Vfile.read_reals(dtype=np.float).reshape((nbf,nbf))
#loops for gses portion of ham
for m in range(nst):
  tmom=0.e0
  for ia in listlist[m]:
#recover i and a from compound index ia
    i = ia//nvir
    a = ia%nvir
    tmom = tmom + X[ia,m]*PC[i,a+noc] 
  ham[0,m+1]=ham[m+1,0]=np.sqrt(2)*tmom
#loops for eses portion of ham
for m in range(nst):
  print m
  for n in range(m+1):  #just the lower unique elements (Its hermitian)
    tmom = 0.e0
    for ia in listlist[m]:
      mpct = 0.e0
      for jb in listlist[n]:
        mpct = mpct + X[jb,n]**2
        i = ia // nvir
        a = ia % nvir
        j = jb // nvir 
        b = jb % nvir
        if i==j:
          if a==b:
            vdet = gsexp - PC[i,i] + PC[a+noc,a+noc]
          else:
            vdet = PC[a+noc, b+noc]
        elif a==b and i!=j:
          vdet = -PC[i,j]
        else:
#          vdet=0.0
          continue 
        tmom = tmom + X[ia,m]*X[jb,n]*vdet  
    print mpct
    ham[m+1,n+1] = ham[n+1,m+1] = tmom    
ham[0,0] = gsexp    
H.write_record(grid)
H.write_record(ham)
H.close
