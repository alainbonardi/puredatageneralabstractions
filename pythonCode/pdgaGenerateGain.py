#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_mcgain(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.gain'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.gain'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ gain\ on\ '+str(ind)+'\ signals\ in\ dB '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        bf.appendXText(f, 2.5, 1, 'message amp followed by the level in dB')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - snake~ out #ind
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind)+' -------------')
        #db2rms
        db2rms_id = bf.appendXObj(f, 2, 1.5, 'db2rms')
        #line 4 - snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind)+' -------------')
        #line 5 - outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #multipliers *~ (ind )
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 3, '*~')
        #comes back to the first
        mult_id = out_id + 1
        #writes the connections
        #connects the inlet~ to the snake~ out #ind
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #connects the inlet to the db2rms abstraction
        bf.appendXConnect(f, in2_id, 0, db2rms_id, 0)
        #connects the snake~ out # ind outputs to the first inputs of the different *~
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, mult_id+j, 0)
        #connects the output of db2rms to the second inputs of the different *~~
        for j in range(ind):
            bf.appendXConnect(f, db2rms_id, 0, mult_id+j, 1)
        #connects the outputs of the different *~to the inputs of snake~ in #ind
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #connects the output of snake~ in #ind
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()