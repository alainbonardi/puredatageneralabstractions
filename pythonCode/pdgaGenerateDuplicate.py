#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.busplus#ind abstractions
_______________________________________________________
"""   
def generate_mcduplicate(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busplus#ind.pd abstraction
        fileName = dDir+'/mc.duplicate'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.duplicate#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.duplicate'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' creates\ '+str(ind)+'\ copies\ of\ the\ input\ channel '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        
        #inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 2, 'snake~ in '+str(ind))
        #outlet~
        outlet_id = bf.appendXObj(f, 0, 3, 'outlet~ ')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ to snake~ in #ind multiple connections
        for j in range(ind):
            bf.appendXConnect(f, in_id, 0, snakein_id, j)
        #snake~ in #ind to outlet~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()