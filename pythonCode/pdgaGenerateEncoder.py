#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_hoaencoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.encoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.encoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
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
        #line 2 - hoa.encodingmodule#ind
        encomod_id = bf.appendXObj(f, 0, 2, 'hoa.encodingmodule'+str(ind))
        #line 3 - outlet~
        out_id = bf.appendXObj(f, 0, 3, 'outlet~')

        #writes the connections
        #connects the inlet~ 1 to the first input of hoa.encodingmodule#ind
        bf.appendXConnect(f, in1_id, 0, encomod_id, 0)
        #connects the inlet 2 to the encodercontrol abstraction
        bf.appendXConnect(f, in2_id, 0, encoctrl_id, 0)
        #connects the encodercontrol to the right inlet of encodingmodule#ind
        bf.appendXConnect(f, encoctrl_id, 0, encomod_id, 1)
        #connects the encodingmodule#ind to the outlet
        bf.appendXConnect(f, encomod_id, 0, out_id, 0)
        
        f.close()