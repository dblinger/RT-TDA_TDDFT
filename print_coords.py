#!/bin/python
#
#   Script to print the coordinates in the plane.  
#   Note that the fastest running index should be made
#   consistent with the ordering of the cube file format
#
from __future__ import division
import sys

for z in range(100):
  for x in range(40):
    print '0.0 '+str(x/10.0*1.89)+' '+str(z/10.0*1.89) 
