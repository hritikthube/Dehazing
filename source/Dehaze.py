

import DarkChannel
import ALight
import Transmission
import RefineG
import Rad
import numpy


def dehaze(imgar, a=None, t=None, rt=None, tmin=0.1, ps=15, w=0.95, px=1e-3, r=40, eps=1e-3, m=False):
    
	
 

    jdark = DarkChannel.estimate(imgar, ps)
    
    if a == None:
        a = ALight.estimate(imgar, jdark)
        if(m == True):
            print ('ALight estimated.')
    
    
    if rt == None and t == None:
        rt =Transmission.estimate(imgar, a, w)
        rt=numpy.maximum(rt, tmin)
    if(m == True):
            print ('Trans estimated.')
    
    if t == None:
        t = RefineG.guided_filter(imgar, rt)
        if(m == True):
           print ('Trans refined.')
    
    dehazed = Rad.recover(imgar, a, t, tmin)
    if(m == True):        
       print ('Rad recovered.')
    
    return dehazed
