import sys

numz = 21

data = np.loadtxt(str(sys.argv[1]))
coups = data[:,2]
for i in range(coups.shape[0]):
  print coups[i],
  if (i+1)%6==0: print
  if (i+1)%numz==0 and (i+1)%6!=0: print


