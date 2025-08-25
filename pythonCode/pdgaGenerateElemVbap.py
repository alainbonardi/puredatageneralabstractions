#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the vbap#ind abstractions
_______________________________________________________
"""   
def generate_vbap(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for vbap#ind_f.pd abstraction
        fileName = dDir+'/vbap'+str(ind)+"_f.pd"
        f = open(fileName, 'w')
        #writes the lines of the vbap#ind_f.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'vbap#ind_f.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1 - (ind) inlets
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 1, 'inlet')
        #comes back to the first one
        multiinlet_id = in_id + 1
        #loadbang
        loadbang_id = bf.appendXObj(f, ind+1, 1, 'loadbang')
        #float object
        float_id = bf.appendXObj(f, ind+1, 1.5, 'float \$1')
        #vbap abstractions
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 2, 'vbap')
        #comes back to the first one
        multivbap_id = float_id + 1
        #+~ objects
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 3, '+~')
        #comes back to the first one
        multiplus_id = multivbap_id + ind
        #snake~ in #ind object
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~ object
        outlet_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #connexions
        #loadbang to float
        bf.appendXConnect(f, loadbang_id, 0, float_id, 0)
        #inlet~ to all vbap abstrations
        for j in range(ind):
            bf.appendXConnect(f, in_id, 0, multivbap_id+j, 0)
        #inlets to vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, multiinlet_id+j, 0, multivbap_id+j, 1)
            if (j > 0):
                bf.appendXConnect(f, multiinlet_id+j, 0, multivbap_id+j-1, 2)
        bf.appendXConnect(f, multiinlet_id, 0, multivbap_id+ind-1, 2)
        #float to vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, float_id, 0, multivbap_id+j, 3)
        #vbap abstractions to +~ objects
        for j in range(ind):
            bf.appendXConnect(f, multivbap_id+j, 0, multiplus_id+j, 1)
            if (j < ind-1):
                bf.appendXConnect(f, multivbap_id+j, 1, multiplus_id+j+1, 0)
        bf.appendXConnect(f, multivbap_id+ind-1, 1, multiplus_id, 0)
        #+~ to snake~ in #ind object
        for j in range(ind):
            bf.appendXConnect(f, multiplus_id+j, 0, snakein_id, j)
        #snake~ in #ind object to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()