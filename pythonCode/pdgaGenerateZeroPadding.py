#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.zeropadding#ind abstractions
_______________________________________________________
"""   
def generate_mczeropad(dDir):
    for i in range (4, 2*bf.maxAmbiOrder+2+1):
        ind = i
        #opens a Pure Data file for the mc.stereozeropad#ind.pd abstraction
        fileName = dDir+'/mc.stereozeropad'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.stereozeropad#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.stereozeropad'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' completes\ stereo\ with\ '+str(ind-2)+'\ zeros '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        #
        #inlet~ for the stereo initial flow
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #snake~ out 2 object to decompose the 2 channels
        snakeout_id = bf.appendXObj(f, 0, 2, 'snake~ out 2')
        #snake~ in ind object for the final result
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~ for the output
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #sig~ 0 for the zero padding
        sig0_id = bf.appendXObj(f, 1, 2, 'sig~ 0')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out two channels to snake~ in first two channels
        bf.appendXConnect(f, snakeout_id, 0, snakein_id, 0)
        bf.appendXConnect(f, snakeout_id, 1, snakein_id, 1)
        #sig~ 0 to all the other inputs of snake~ in #ind
        for j in range(2, ind):
            bf.appendXConnect(f, sig0_id, 0, snakein_id, j)
        #snake~ in #ind to outlet~~
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()