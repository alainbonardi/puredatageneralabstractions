#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_mcrecorder(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.recorder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.recorder#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.recorder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ recorder\ of\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #bang in the canvas to open a file
        bng_id = bf.appendXObj(f, 0.8, 0.95, 'bng 15 250 50 0 empty empty open 17 7 0 10 #0c4044 #000000 #000000')
        #toggle in the canvas to start recording
        tgl_id = bf.appendXObj(f, 1.27, 0.95, 'tgl 15 0 empty empty record 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #recordercontrol abstraction
        recoctrl_id = bf.appendXObj(f, 0.5, 1.5, 'recordercontrol')
        #inlet~~
        in1_id = bf.appendXObj(f, 2, 1.5, 'inlet~')
        #snake~ out #ind
        snakeout_id = bf.appendXObj(f, 2, 2, 'snake~ out '+str(ind))
        #writesf~ #ind
        w_id = bf.appendXObj(f, 0.5, 3, 'writesf~ '+str(ind))
        #adds the canvas
        f.write('#X coords 0 -1 1 1 110 40 1 100 100;\n')
        #connections
        #open bang to left input of recordercontrol abstraction
        bf.appendXConnect(f, bng_id, 0, recoctrl_id, 0)
        #write toggle to right input of recordercontrol abstraction
        bf.appendXConnect(f, tgl_id, 0, recoctrl_id, 1)
        #inlet~ to snake~ out #ind
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #recodercontrol to input 0 of writesf~~
        bf.appendXConnect(f, recoctrl_id, 0, w_id, 0)
        #connections to the various outputs of snake~ out #ind to the inputs of writesf~ #ind
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, w_id, j)
        f.close()