

import numpy
import DarkChannel


def estimate(imgar, A, w=0.95):

    normalizedimg = numpy.zeros(imgar.shape)
    

    for c in range(0, imgar.shape[2]):
        normalizedimg[:,:,c] = imgar[:,:,c]/A[c]
    
    
    normalizedjdark = DarkChannel.estimate(normalizedimg)
    
    t = 1-w*normalizedjdark+0.25
    
    
    return t
