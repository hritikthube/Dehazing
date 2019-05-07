
import numpy

def estimate(imgar, ps=15):
      
    impad = numpy.pad(imgar, [(int(ps/2),int(ps/2)), (int(ps/2),int(ps/2)) , (0,0)], 'edge')
    
    jdark = numpy.zeros((imgar.shape[0],imgar.shape[1]))
    
    for i in range(int(ps/2), (imgar.shape[0]+int(ps/2))):
        for j in range(int(ps/2), (imgar.shape[1]+int(ps/2))):
     
            patch = impad[i-int(ps/2):i+1+int(ps/2), j-int(ps/2):j+1+int(ps/2)]
           
            jdark[i-int(ps/2), j-int(ps/2)] = patch.min()
    
    return jdark
     
    