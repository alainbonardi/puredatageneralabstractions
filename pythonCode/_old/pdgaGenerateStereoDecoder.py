#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.stereodecoder#ind abstractions
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
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #bf.appendXText(f, 2.5, 1, 'amp+value message')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #inlet for the message amp+value
        #in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - mc.decoderblock1#ind
        hoadb_id = bf.appendXObj(f, 0, 1.5, 'hoa.decoderblock'+str(ind))
        #line 2 - hoa.2dprojection#ind
        hoa2dproj_id = bf.appendXObj(f, 0, 2, 'hoa.2dprojection'+str(ind))
        #line 3 - outlet~~
        out_id = bf.appendXObj(f, 0, 3, 'outlet~')
        #connections
        #inlet~ to hoa.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, hoadb_id, 0)
        #hoa.decoderblock#ind to hoa.2dprojection#ind
        bf.appendXConnect(f, hoadb_id, 0, hoa2dproj_id, 0)
        #hoa.2dprojection#ind to outlet~~
        bf.appendXConnect(f, hoa2dproj_id, 0, out_id, 0)
        #
        #
        f.close()