#p_is_guidedfilter
import numpy

def guided_filter(imgar, p, r=40, eps=1e-3):
    
    H, W, C = imgar.shape 
    S = __boxfilter__(numpy.ones((H, W)), r)
    
    mean_i = numpy.zeros((C, H, W))
    
    for c in range(0, C):
        mean_i[c] = __boxfilter__(imgar[:,:, c], r)/S
    
    mean_p = __boxfilter__(p, r)/S
    
    mean_ip = numpy.zeros((C, H, W))
    for c in range(0, C):
        mean_ip[c] = __boxfilter__(imgar[:,:,c]*p, r)/S
     
    cov_ip = numpy.zeros((C, H, W))
    for c in range(0, C):
        cov_ip[c] = mean_ip[c] - mean_i[c]*mean_p
    
    var_i = numpy.zeros((C, C, H, W))
    
    var_i[0, 0] = __boxfilter__(imgar[:,:,0]*imgar[:,:,0], r)/S - mean_i[0]*mean_i[0]

    var_i[0, 1] = __boxfilter__(imgar[:,:,0]*imgar[:,:,1], r)/S - mean_i[0]*mean_i[1]
    
    var_i[0, 2] = __boxfilter__(imgar[:,:,0]*imgar[:,:,2], r)/S - mean_i[0]*mean_i[2]
    
    var_i[1, 1] = __boxfilter__(imgar[:,:,1]*imgar[:,:,1], r)/S - mean_i[1]*mean_i[1]
    
    var_i[1, 2] = __boxfilter__(imgar[:,:,1]*imgar[:,:,2], r)/S - mean_i[1]*mean_i[2]
    
    var_i[2, 2] = __boxfilter__(imgar[:,:,2]*imgar[:,:,2], r)/S - mean_i[2]*mean_i[2]
    
    a=numpy.zeros((H,W,C))
    
    for i in range(0, H):
        for j in range(0, W):
            sigma = numpy.array([ [var_i[0, 0, i, j], var_i[0, 1, i, j], var_i[0, 2, i, j]], 
                                  [var_i[0, 1, i, j], var_i[1, 1, i, j], var_i[1, 2, i, j]],
                                  [var_i[0, 2, i, j], var_i[1, 2, i, j], var_i[2, 2, i, j]]])
             
        
            cov_ip_ij = numpy.array([ cov_ip[0, i, j], cov_ip[1, i, j], cov_ip[2, i, j]]) 
               
            a[i, j] = numpy.dot(cov_ip_ij, numpy.linalg.inv(sigma + eps*numpy.identity(3))) 
    
    b = mean_p - a[:,:,0]*mean_i[0,:,:] - a[:,:,1]*mean_i[1,:,:] - a[:,:,2]*mean_i[2,:,:] 
    
   
    pp = ( __boxfilter__(a[:,:,0], r)*imgar[:,:,0]
          +__boxfilter__(a[:,:,1], r)*imgar[:,:,1]
          +__boxfilter__(a[:,:,2], r)*imgar[:,:,2]
          +__boxfilter__(b, r) )/S
    
    return pp


def __boxfilter__(m, r):
   
    H, W = m.shape
    mp = numpy.zeros(m.shape) 
    
   
    ysum = numpy.cumsum(m, axis=0) 
    mp[0:r+1, : ] = ysum[r:(2*r)+1, : ]
    
    mp[r+1:H-r, : ] = ysum[(2*r)+1: , : ] - ysum[ :H-(2*r)-1, : ]
    mp[(-r): , : ] = numpy.tile(ysum[-1, : ], (r, 1)) - ysum[H-(2*r)-1:H-r-1, : ]

   
    xsum = numpy.cumsum(mp, axis=1)
    
    mp[ : , 0:r+1] = xsum[ : , r:(2*r)+1]
  
    mp[ : , r+1:W-r] = xsum[ : , (2*r)+1: ] - xsum[ : , :W-(2*r)-1]
    mp[ : , -r: ] = numpy.tile(xsum[ : , -1][:, None], (1, r)) - xsum[ : , W-(2*r)-1:W-r-1]

    return mp