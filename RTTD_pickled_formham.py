from __future__ import division
from __future__ import print_function
from scipy.linalg import expm
from scipy.io import FortranFile
import numpy as np
import sys
import itertools

# DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL
#
#
#     A  TDCIS routine that recovers matrix elements of a point charge perturbation operator
#     beteen TDA eigenstates and does real-time TDCIS propagation 
#
# DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL DBL

sol = 137.035999139 # speed of aight in bohr/AU
sol = sol*0.52917721067 # now its in angstrom/AU
vel = 0.5*sol 
dt = 0.0001
nsteps = 100000
#
# get mat elements for first two grid point
#
Ee = FortranFile('evals.dat', 'r')
E = Ee.read_reals(dtype=np.float)
print(E)
nst=np.size(E)
V1 = FortranFile('1.dat', 'r')
V2 = FortranFile('2.dat', 'r')
grid1 = V1.read_reals(dtype=np.float)
Ham1 = V1.read_reals(dtype=np.float).reshape((nst,nst))
grid2 = V2.read_reals(dtype=np.float)
Ham2 = V2.read_reals(dtype=np.float).reshape((nst,nst))
H0CIS = np.diag(E)
Psiold = np.zeros(nst,dtype=np.complex128)
Psiold[0]=1.0
count=3
for istep in range(nsteps):
    time = istep*dt
    zposition = -100.0+vel*time
    if (zposition>=grid2[2]):
      VN = FortranFile(str(count)+'.dat', 'r')
      Ham1 = Ham2
      grid2 = VN.read_reals(dtype=np.float)
      Ham2 = VN.read_reals(dtype=np.float).reshape((nst,nst))
      count += 1
    griddif = grid2[2]-grid1[2]
    progress = zposition-grid1[2]/griddif
    UCISV = expm(-1.0j*dt*(H0CIS+(progress*Ham2+(1.0-progress)*Ham1)))
    Psinew = np.dot(UCISV,Psiold)
    Psiold = Psinew
#
# form the density matrix
#
    Psioldc= np.conjugate(Psiold)
    dmat = np.einsum('i,j->ij',Psioldc,Psiold)
#    print(dmat)
#
# energy expectaton values
#
    print(istep)
    print("En "+str(np.dot(abs(Psiold)**2,E))+"\n")
    print(zposition)
    print(abs(Psinew)**2)
