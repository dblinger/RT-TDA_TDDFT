#!/usr/bin/python
from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

def spec(time,dip):
    '''
        (C) Joshua Goings 2016
        
        CQ_RealTime.py: a post-processing script for computing the absorption spectrum of
         Real Time Time Dependent SCF jobs in Chronus Quantum
        Computes the energy range, w (in eV) and dipole strength function S(w) for
         a given real time TD-SCF run. 
        real_time_file   ... type:string ; the RealTime_Dipole.csv file from a ChronusQ run
        dipole_direction ... type:char   ; which dipole moment contribution is computed (e.g. 'x','y', or 'z')
        kick_strength    ... type:float  ; in a.u., what was the applied field strength (e.g. 0.0001 au)
        damp_const       ... type:float  ; in a.u. of time, gives FWHM of 2/damp_const
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
    
