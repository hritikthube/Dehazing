#refining by guided filter

import numpy

def recover(imgar, atm, t, tmin=0.1):
  
    
    j = numpy.zeros(imgar.shape)
    
    
    for c in range(0, imgar.shape[2]):
        j[:,:, c] = ((imgar[:,:,c]-atm[c])/numpy.maximum(t[:,:], tmin))+atm[c]
    
    return j/numpy.amax(j)