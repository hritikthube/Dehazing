
import numpy

def estimate(imgar, jdark, px=1e-3):
     
       
    
    imgavec = numpy.resize(imgar, (imgar.shape[0]*imgar.shape[1], imgar.shape[2]))

    jdarkvec = numpy.reshape(jdark, jdark.size)
                                                          

    numofpx = numpy.int(jdark.size * px)
                                                    
    isjd = numpy.argsort(-jdarkvec)
                                                           
    asum = numpy.array([0.0,0.0,0.0])

    for i in range(0, numofpx):

        asum[:] += imgavec[isjd[i], :]
                                                                       
    A = numpy.array([0.0,0.0,0.0])
    A[:] = asum[:]/numofpx


    return A
    