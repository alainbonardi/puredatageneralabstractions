#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_hoaregdecoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.regdecoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.regdecoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' ambisonic\ regular\ decoder\ at\ order\ '+str(ind)+'\ to\ '+str(2*ind+2)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #03/01/2026 - remove the amplitude control from the regular decoder
        #bf.appendXText(f, 2.5, 1, 'amp+value message')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #03/01/2026 - remove the amplitude control from the regular decoder
        #inlet for the message amp+value
        #in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - mc.decoderblock1#ind
        mcdb_id = bf.appendXObj(f, 0, 1.5, 'hoa.decoderblock'+str(ind))
        #03/01/2026 - remove the amplitude control from the regular decoder
        #line 3 - mc.gain#(2*ind+2)
        #mcga_id = bf.appendXObj(f, 0, 3, 'mc.gain'+str(2*ind+2))
        #line 3.5 - outlet~
        out_id = bf.appendXObj(f, 0, 3.5, 'outlet~')
        #writes the connections
        #connects the inlet~ to the mc.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, mcdb_id, 0)
        #03/01/2026 - remove the amplitude control from the regular decoder
        #connects the mc.decoderblock#ind to the mc.gain#(2*ind+2)
        #bf.appendXConnect(f, mcdb_id, 0, mcga_id, 0)
        #connects the mc.gain#(2*ind+2) to the outlet~~
        #bf.appendXConnect(f, mcga_id, 0, out_id, 0)
        #connects the inlet to the right input of the mc.gain#(2*ind+2)
        #bf.appendXConnect(f, in2_id, 0, mcga_id, 1)
        bf.appendXConnect(f, mcdb_id, 0, out_id, 0)
        #
        f.close()