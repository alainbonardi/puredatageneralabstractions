#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_hoastereodecoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.stereodecoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.stereodecoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' ambisonic\ stereo\ decoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        bf.appendXText(f, 2.5, 1, 'amp+value message')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - mc.decoderblock1#ind
        hoadb_id = bf.appendXObj(f, 0, 1.5, 'hoa.decoderblock'+str(ind))
        #line 2 - snake~ out #2*ind+2
        snakeout_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(2*ind+2))
        #line 3 - 2*ind+2 stereogains
        for j in range(2*ind+2):
            k = bf.appendXObj(f, j, 3, 'stereogains '+str(j*360/(2*ind+2)))
        #comes back to the first
        stereog_id = snakeout_id+1
        #line 4 - snake~ in 2
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in 2')
        #line 4.5- mc.gains2
        mcg_id = bf.appendXObj(f, 0, 4.5, 'mc.gain2')
        #line 5 - outlet~~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #connections
        #inlet~ to hoa.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, hoadb_id, 0)
        #hoa.decoderblock#ind to snake~ out #2*ind+2
        bf.appendXConnect(f, hoadb_id, 0, snakeout_id, 0)
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
        bf.appendXConnect(f, snakein_id, 0, mcg_id, 0)
        #connects the mc.gain2 object to the outlet~~
        bf.appendXConnect(f, mcg_id, 0, out_id, 0)
        #connects the inlet to the right input of mc.gain2
        bf.appendXConnect(f, in2_id, 0, mcg_id, 1)
        #
        f.close()