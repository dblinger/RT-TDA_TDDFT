#!/usr/bin/python
from __future__ import division
import sys
import numpy as np
from scipy.fftpack import fft, fftfreq

#timedip input file should have time (in AU) in first column, then x, y, and z dipole components

def spec(time,dip):
   
    # subtract the average to prevent zero peak 
    dip = dip - np.mean(dip)

    # do the discrete fourier transform 
    fw = fft(dip)

    # determine frequency range
    n = len(fw)      
    timestep = time[1] - time[0]              # assumes constant time step
    w = fftfreq(n,d=timestep)*2.0*np.pi # frequency list
   
    fw_abs = abs(fw)                    # absolute value of frequencies
    fw_im  = np.imag(fw) 
    w = (w*27.2114)    # give frequencies in eV
    return w,fw_im

if __name__ == '__main__':

    Filename   = 'timedip'
    rt = np.genfromtxt(Filename)
    t      = rt[:,0]
    x      = rt[:,1]
    y      = rt[:,2]
    z      = rt[:,3]
    w, Fx      = spec(t,x) 
    w, Fy      = spec(t,y)
    w, Fz      = spec(t,z)

    np.savetxt('spectrum_ev.txt', np.transpose([w,Fx+Fx+Fz]))  
    
