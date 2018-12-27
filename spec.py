#!/usr/bin/python
from __future__ import division
import sys
import numpy as np
from scipy.fftpack import fft, fftfreq

def spec(time,dip):
    '''
timedip input file should have time (in AU) in first column, then x, y, and z dipole components
    '''
   
    # chronusq file is CSV, also skip the header (first row)

    # subtract the average to prevent zero peak 
    dip = dip - np.mean(dip)

    # do the fourier transform 
    fw = fft(dip)

    # determine frequency range
    n = len(fw)                         # number samples, including padding
    timestep = time[1] - time[0]              # spacing between time samples; assumes constant time step
    w = fftfreq(n,d=timestep)*2.0*np.pi # frequency list
   
    fw_re = np.real(fw)                 # the real FFT frequencies
    fw_im = (np.imag(fw))               # the imaginary FFT frequencies
    fw_abs = abs(fw)                    # absolute value of frequencies
    
    w = (w*27.2114)    # give frequencies in eV
    return w,fw_abs 

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
    
