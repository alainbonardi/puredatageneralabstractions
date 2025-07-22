#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_hoadecoderblock(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.decoderblock#ind.pd abstraction
        fileName = dDir+'/hoa.decoderblock'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.decoderblock#ind.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1.5 - snake~ out
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(2*ind+1))
        #line 2 - *~0.5
        mult_id = bf.appendXObj(f, 0, 2, '*~ 0.5')
        #line 2.5 - snake~ in
        snakein1_id = bf.appendXObj(f, 0, 2.5, 'snake~ in '+str(2*ind+1))
        #line 4 - snake~ in
        snakein2_id = bf.appendXObj(f, 0.5*ind, 4, 'snake~ in '+str(2*ind+2))
        #line 4.5 - outlet~~
        out_id = bf.appendXObj(f, 0.5*ind, 4.5, 'outlet~')
        #line 2 - mc.cstencoder#ind
        for j in range(2*ind+2):
            ind2 = j + 1
            k = bf.appendXObj(f, ind2, 2, 'hoa.cstencoder'+str(ind)+' '+str(j))
        #comes back to the first one
        cstencoder_id = out_id + 1
        #cstencoder_id between 8 and 8+2*ind+1
        #line 3 - mc.sp#2*ind+1
        for j in range(2*ind+2):
            ind2 = j + 1
            k = bf.appendXObj(f, j, 3, 'mc.sp'+str(2*ind+1))
        #comes back to the first one
        sp_id = cstencoder_id+2*ind+2
        #connexions
        #inlet~ to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out 0 to *~0.5
        bf.appendXConnect(f, snakeout_id, 0, mult_id, 0)
        #*~0.5 to snake~ in 0
        bf.appendXConnect(f, mult_id, 0, snakein1_id, 0)
        #snake~ out 1 to 2*ind to snake~ in 1 to 2*ind
        for j in range(2*ind):
            ind2 = j + 1
            bf.appendXConnect(f, snakeout_id, ind2, snakein1_id, ind2)
        #mc.cstencoder#j to mc.sp#j inlet 1
        for j in range(2*ind+2):
            bf.appendXConnect(f, cstencoder_id+j, 0, sp_id+j, 1)
        #snake~ in to mc.sp#j inlet 0
        for j in range(2*ind+2):
            bf.appendXConnect(f, snakein1_id, 0, sp_id+j, 0)
        #mc.sp#j outlet 0 to snake~ in inlet j
        for j in range(2*ind+2):
            bf.appendXConnect(f, sp_id+j, 0, snakein2_id, j)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snakein2_id, 0, out_id, 0)
        f.close()