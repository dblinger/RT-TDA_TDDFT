# RT-TDA_TDDFT
# RT-TDA_TDDFT


First, run NWchem with coords.inp file setup with the structure:

(int) number of points
(floats) x y z of point 1
(floats) x y z of point 2
...

Then, run pickled_mask.py.  This will chug on the Xmat.dat to generate a list of lists of all significant Xmat elements.

Then, run run_formham.sh, which will use the pickled mask to generate hamiltonians for each coord from coords.inp.  Just change the loop to be consistent with numenr of points in coords.inp.

Now that you have loads of number.dat files, run RTTD.py.  It will pick these hamiltonians up as it need and do the propagation of a point charge with positive velocity along z, starting from 0,0,-100.
