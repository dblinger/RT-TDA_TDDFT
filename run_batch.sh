#!/bin/bash
##PBS -S /bin/bash
#PBS -m be
#PBS -q batch
#PBS -N 4_shell_Si_3c_opt
#PBS -A cnms
#PBS -W group_list=cades-cnms
#PBS -l qos=std
#PBS -l nodes=1:ppn=32
#PBS -l walltime=48:00:00

#CD into working dir
cd /lustre/or-hydra/cades-cnms/6dl/Si_3C_defect/triangle/full_opt/NEB_5/bead_19_reopt/tddft/with_couplings/more_gridpoints
 
# assuming 32 cores per node.  Could be more clever here with small effort...
for i in `seq 737 32 860`;
do
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  let i+=1
  python formham_with_pickled_mask.py $i   &        
  wait
done 


