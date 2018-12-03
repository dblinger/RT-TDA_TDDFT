# RT-TDA_TDDFT
# RT-TDA_TDDFT


First, run my modified NWchem with coords.inp file setup with the structure:

(int) number of points
(floats) x y z of point 1
(floats) x y z of point 2
...

Then, run pickled_mask.py.  This will chug on the Xmat.dat to generate lists of all significant Xmat elements.  We then iterate only over elements of that list instead of all nocc*nvirt many X elements when calculating excited-excited couplings.

Then, run run_formham.sh, which will run formham_with_pickled_mask.py using the pickled mask to generate full hamiltonians for each coord from coords.inp.  Just be sure to  change the loop to be consistent with numenr of points in coords.inp.

Now that you have loads of number.dat files, run RTTD.py.  It will pick these hamiltonians up as it need and do the propagation of a point charge with positive velocity along z, starting from 0,0,-100.
