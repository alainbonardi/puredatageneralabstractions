#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.stereodecoder#ind abstractions
_______________________________________________________
"""   
def generate_hoa2dprojection(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.2dprojection'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.2dprojection'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' stereoprojection\ of\ a\ regular\ decoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 2 - snake~ out #2*ind+2
        snakeout_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(2*ind+2))
        #line 3 - 2*ind+2 stereogains
        for j in range(2*ind+2):
            k = bf.appendXObj(f, j*1.2, 3, 'stereogains '+str(j*360/(2*ind+2)))
        #comes back to the first
        stereog_id = snakeout_id+1
        #line 4 - snake~ in 2
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in 2')
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #line 4.5- mc.gains2
        #mcg_id = bf.appendXObj(f, 0, 4.5, 'mc.gain2')
        #line 5 - outlet~~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #connections
        #inlet~ to snake~ out
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #all the outputs of snake~ out #2*ind+2 to the various stereogains
        for j in range(2*ind+2):
            bf.appendXConnect(f, snakeout_id, j, stereog_id+j, 0)
        #connects the left outputs of stereogains objects to the left input of snake~ in 2
        for j in range(2*ind+2):
            bf.appendXConnect(f, stereog_id+j, 0, snakein_id, 0)
        #connects the right outputs of stereogains objects to the right input of snake~ in 2
        for j in range(2*ind+2):
            bf.appendXConnect(f, stereog_id+j, 1, snakein_id, 1)  
        #connects the snake~ in 2 object to the mc.gain2 object
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #bf.appendXConnect(f, snakein_id, 0, mcg_id, 0)
        #connects the mc.gain2 object to the outlet~~
        #bf.appendXConnect(f, mcg_id, 0, out_id, 0)
        #connects the inlet to the right input of mc.gain2
        #bf.appendXConnect(f, in2_id, 0, mcg_id, 1)
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        #
        f.close()