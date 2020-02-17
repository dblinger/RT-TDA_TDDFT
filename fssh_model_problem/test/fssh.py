from __future__ import division
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

dt = 4.134 
nst=2
#
# get mat elements
#
Filename   = 'fssh.dat'
data = np.genfromtxt(Filename)
E1      = data[:,0]
E2      = data[:,1]
tau1      = data[:,2]
tau2      = data[:,3]
nsteps=len(tau1)
print str(nsteps)
E1half=np.zeros(nsteps)
E2half=np.zeros(nsteps)
tauhalf=np.zeros(nsteps)

for i in range(nsteps-1):
  E1half[i] = (E1[i]+E1[i+1])/2/27.211385
  E2half[i] = (E2[i]+E2[i+1])/2/27.211385
  tauhalf[i] = (tau1[i]+tau2[i])/2/dt  # dt is actually the full timestep, and we need 1/2 delta t since we use
#   the central final difference 
#
# interpolate E's to get the half-step values
#

hopprob=np.zeros(nsteps)
Psiold = np.zeros(nst,dtype=np.complex128)
Psiold[1]=1.0
for istep in range(nsteps-1):
    time_fs = istep*dt*0.02418884254
    Hamhalf = np.zeros((2,2),dtype=np.complex128)
    Hamhalf[0,0] = E1half[istep]
    Hamhalf[1,1] = E2half[istep]
    Hamhalf[0,1] = -1.0*1j*tauhalf[istep]
    Hamhalf[1,0] = 1.0*1j*tauhalf[istep]
    U = expm(-1.0j*dt*Hamhalf)
    Psinew = np.dot(U,Psiold)
    Psiold = Psinew
#
# form the density matrix
#
    Psioldc= np.conjugate(Psiold)
    dmat = np.einsum('i,j->ij',Psioldc,Psiold)
#
# form the hop probs, -4*Real(dmat_01*tau_01)*dt/dmat_11
#
    hopprob[istep]= -4.0*dt*np.real(dmat[0,1])*((tauhalf[istep]+tauhalf[istep+1])/2)/dmat[1,1] 
#
# energy expectaton values
#
    print "time_fs  "+str(time_fs)
    print "hopprob "+str(hopprob[istep])
    print str(Psiold)

#ntraj=1000000
ntraj=100000

for traj in range(ntraj):
  for istep in range(nsteps):
    if (hopprob[istep]>np.random.random_sample()):
#      print "time: "+str(istep*dt*0.02418884254)
      print "step: "+str(istep)
      continue
