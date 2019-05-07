
import argparse
import sys
from Imstore import Imstore
from Dehaze import dehaze
import numpy


def __prepareargs__():
    parser = argparse.ArgumentParser(description='Dehazing of Image')
    parser.add_argument('-i', nargs=1, type=str, help='input image path', required=True)
    parser.add_argument('-o', nargs=1, type=str, help='output image path', required=True)
    parser.add_argument('-m', action='store_const', help='test messages ', const=True, default=False, required=False)
    
    return parser

def __getargs__(parser):
    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':

    parser = __prepareargs__()
    args = __getargs__(parser)
    

    input_img_file = args['i'][0]
    output_img_file = args['o'][0]
    

    a = None
    t = None
    rt = None
    tmin=0.1 
    ps=15 
    w=0.95 
    px=1e-3 
    r=40 
    eps=1e-3
    m = args['m']
    

    try:
        img = Imstore.open(input_img_file)
        if(m == True):
            print ('Image \''+input_img_file+'\' opened.')
    except IOError:
        print ('File \''+input_img_file+'\' cannot be found.')
        sys.exit()

      
    outputimg = dehaze(img.array(), a, t, rt, tmin, ps, w, px, r, eps, m)
    
    
    saveimg = Imstore.save(outputimg, output_img_file)
    if(m == True):
        print ('Image \''+output_img_file+'\' saved.')
    
    print ('Work done successfully')
