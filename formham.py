from __future__ import division
from scipy.linalg import expm
from scipy.io import FortranFile
import numpy as np
import sys


PCname=str(sys.argv[1])
print PCname
npts=127
noc=280#number doubly occ orbs
nst=1000#just excited states	
nbf=468
nvir=nbf-noc
nov=noc*nvir
H = FortranFile('dblmat.dat', 'w')
Vfile = FortranFile(PCname, 'r')
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
# now we have listlist which is a list of lists of nonzero ia elements of X 
# iterate over these in the loops instead of all ia / ijab
# Load in the first gridpoint's PC matrix
#
# Create np array for Hamiltonian in the adiabatic basis
#
for i in range(npts):
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
  H.write_record(grid,dtype=np.float)
  H.write_record(ham,dtype=np.float)
H.close
