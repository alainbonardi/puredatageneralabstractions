#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.encodingmodule#ind abstractions
_______________________________________________________
"""   
def generate_hoaencodingmodule(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the hoa.encodingmodule#ind.pd abstraction
        fileName = dDir+'/hoa.encodingmodule'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.encodingmodule#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.encodingmodule#ind.pd')
        #line 0.25 - inlet~ 1 - signal
        in1_id = bf.appendXObj(f, 0, 0.25, 'inlet~')
        #line 0.25- inlet~ 2 - phase (angle between 0 and 1)
        in2_id = bf.appendXObj(f, 3, 0.25, 'inlet~')
        #line 4.5
        #snake~ in
        snake_id = bf.appendXObj(f, 0, 4.5, 'snake~ in '+str(2*ind+1)+' ----------')
        #line 5
        #outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #sinandcos abstractions
        for j in range(ind):
            ind2 = j + 1
            k = bf.appendXObj(f, ind2, 3, 'sinandcos '+str(ind2))
            #ids from 9 to 9+ind-1
        #comes back to the first one
        sinandcos_id = out_id + 1
        #line 4
        #*~
        for j in range(2*ind):
            ind2 = j + 1
            ind3 = 0.5 * ind2
            k = bf.appendXObj(f, ind3, 3.5, '*~')
            #ids from 9+ind to 9+3*ind-1
        #comes back to the first one
        mult_id = sinandcos_id + ind
        #connections
        #inlet~ 2 to sinandcos abstractions
        for j in range(ind):
            bf.appendXConnect(f, in2_id, 0, sinandcos_id+j, 0)
        #inlet~ 1 to *~
        for j in range(2*ind):
            bf.appendXConnect(f, in1_id, 0, mult_id+j, 0)
        #inlet~ 1 to input 0 of snake~ in
        bf.appendXConnect(f, in1_id, 0, snake_id, 0)
        #sinandcos to *~~
        for j in range(ind):
            bf.appendXConnect(f, sinandcos_id+j, 0, mult_id+2*j, 1)
            bf.appendXConnect(f, sinandcos_id+j, 1, mult_id+2*j+1, 1)
        #*~ to snake~ in
        for j in range(2*ind):
            bf.appendXConnect(f, mult_id+j, 0, snake_id, j+1)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snake_id, 0, out_id, 0)
        f.close()