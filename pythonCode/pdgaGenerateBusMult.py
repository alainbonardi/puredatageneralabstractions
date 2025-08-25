#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.busmult#ind abstractions
_______________________________________________________
"""   
def generate_mcbusmult(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busplus#ind.pd abstraction
        fileName = dDir+'/mc.busmult'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.busmult#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.busmult'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ bus\ multiplication\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        
        #inlet~ 1
        in1_id = bf.appendXObj(f, 0, 1.5, 'inlet~')
        #inlet~ 2
        in2_id = bf.appendXObj(f, 2, 1.5, 'inlet~')
        #snake~ out #ind 1
        snakeout1_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(ind))
        #snake~ out #ind 2
        snakeout2_id = bf.appendXObj(f, 2, 2, 'snake~ out '+str(ind))
        #*~ objects
        for j in range(ind):
            k = bf.appendXObj(f, j, 3, '*~')
        #comes back to the first one
        multimult_id = snakeout2_id + 1
        #snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~
        outlet_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ 1 to snake~ out 1
        bf.appendXConnect(f, in1_id, 0, snakeout1_id, 0)
        #inlet~ 2 to snake~ out 2
        bf.appendXConnect(f, in2_id, 0, snakeout2_id, 0)
        #snake~ out 1 to left inlets of *~
        #snake~ out 2 to right inlets of *~
        for j in range(ind):
            bf.appendXConnect(f, snakeout1_id, j, multimult_id+j, 0)
            bf.appendXConnect(f, snakeout2_id, j, multimult_id+j, 1)
        #+~ to snake~ in object
        for j in range(ind):
            bf.appendXConnect(f, multimult_id+j, 0, snakein_id, j)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()