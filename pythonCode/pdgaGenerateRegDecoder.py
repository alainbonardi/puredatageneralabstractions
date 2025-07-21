#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_mcregdecoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.regdecoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.regdecoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ ambisonic\ regular\ decoder\ at\ order\ '+str(ind)+'\ to\ '+str(2*ind+2)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        bf.appendXText(f, 2.5, 1, 'amp+value message')
        #f.write(xText+str(getPx(2.5))+' '+str(getPy(1))+' amp+value message;\n')
        #line 1
        #inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        print(in1_id)
        #f.write(xObj+str(getPx(0))+' '+str(getPy(1))+' inlet~;\n')
        #in1_id = 4
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #f.write(xObj+str(getPx(2))+' '+str(getPy(1))+' inlet;\n')
        #in2_id = 5
        #line 1.5
        #mc.decoderblock1#ind
        mcdb_id = bf.appendXObj(f, 0, 1.5, 'mc.decoderblock'+str(ind))
        #f.write(xObj+str(getPx(0))+' '+str(getPy(1.5))+' mc.decoderblock'+str(ind)+';\n')
        #mcdb_id = 6
        #line 3
        #mc.gain#(2*ind+2)
        mcga_id = bf.appendXObj(f, 0, 3, 'mc.gain'+str(2*ind+2))
        #f.write(xObj+str(getPx(0))+' '+str(getPy(3))+' mc.gain'+str(2*ind+2)+';\n')
        #mcga_id = 7
        #line 3.5
        #outlet~
        out_id = bf.appendXObj(f, 0, 3.5, 'outlet~')
        #f.write(xObj+str(getPx(0))+' '+str(getPy(3.5))+' outlet~;\n')
        #out_id = 8
        #writes the connections
        #connects the inlet~ to the mc.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, mcdb_id, 0)
        #f.write(xConnect+str(in1_id)+' 0 '+str(mcdb_id)+' 0;\n')
        #connects the mc.decoderblock#ind to the mc.gain#(2*ind+2)
        bf.appendXConnect(f, mcdb_id, 0, mcga_id, 0)
        #f.write(xConnect+str(mcdb_id)+' 0 '+str(mcga_id)+' 0;\n')
        #connects the mc.gain#(2*ind+2) to the outlet~~
        bf.appendXConnect(f, mcga_id, 0, out_id, 0)
        #f.write(xConnect+str(mcga_id)+' 0 '+str(out_id)+' 0;\n')
        #connects the inlet to the right input of the mc.gain#(2*ind+2)
        bf.appendXConnect(f, in2_id, 0, mcga_id, 1)
        #f.write(xConnect+str(in2_id)+' 0 '+str(mcga_id)+' 1;\n')
        #
        f.close()