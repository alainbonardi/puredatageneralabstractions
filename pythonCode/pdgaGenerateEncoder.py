#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_mcencoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.encoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.encoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ ambisonic\ encoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #line 0.5 - inlet~
        in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2.5, 0.5, 'inlet')
        #line 1 - encodercontrol abstraction
        encoctrl_id = bf.appendXObj(f, 2.5, 1, 'encodercontrol')
        #line 4.5 - snake~ in 2*#ind+1
        snakein_id = bf.appendXObj(f, 0, 4.5, 'snake~ in '+str(2*ind+1)+' ----------')
        #line 5 - outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 1.5 - sinandcos abstractions (ind)
        for j in range(ind):
            ind2 = j + 1
            k = bf.appendXObj(f, 2.5+j, 1.5, 'sinandcos '+str(ind2))
        #comes back to the first
        sinandcos_id = out_id + 1
        #line 3.5
        #multipliers *~ (ind )
        for j in range(2*ind):
            k = bf.appendXObj(f, (j+1)*0.5, 3.5, '*~')
        #comes back to the first
        mult_id = sinandcos_id+ind
        #writes the connections
        #connects the inlet to the first input of snake~ in 2*#ind+1
        bf.appendXConnect(f, in1_id, 0, snakein_id, 0)
        #connects the inlet to the left inputs of the *~~
        for j in range(2*ind):
            bf.appendXConnect(f, in1_id, 0, mult_id+j, 0)
        #connects the inlet to the encodercontrol abstraction
        bf.appendXConnect(f, in2_id, 0, encoctrl_id, 0)
        #connects the encodercontrol abstraction to all the sinandcos abstractions
        for j in range(ind):
            bf.appendXConnect(f, encoctrl_id, 0, sinandcos_id+j, 0)
        #connects the left outputs of sinandcos abstractions to the even multipliers (0 to 2*ind-2)
        for j in range(ind):
            bf.appendXConnect(f, sinandcos_id+j, 0, mult_id+2*j, 1)
        #connects the right outputs of sinandcos abstractions to the odd multipliers (1 to 2*ind-1)
        for j in range(ind):
            bf.appendXConnect(f, sinandcos_id+j, 1, mult_id+2*j+1, 1)
        #connects the outputs of the multipliers to the inputs of the snake~ in (1 to 2*ind)
        for j in range(2*ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j+1)
        #connects the output of snake~ in #ind
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()