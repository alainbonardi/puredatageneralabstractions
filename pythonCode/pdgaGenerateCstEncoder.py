#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.cstencoder#ind abstractions
_______________________________________________________
"""   
def generate_hoacstencoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.cstencoder#ind.pd abstraction
        fileName = dDir+'/hoa.cstencoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.cstencoder#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.cstencoder#ind.pd')
        #line 0.25
        #loadbang
        loadbang_id = bf.appendXObj(f, 0, 0.25, 'loadbang')
        #line 0.5
        #msg
        msg_id = bf.appendXMsg(f, 0, 0.5, str(ind))
        #float
        float_id = bf.appendXObj(f, 1, 0.5, 'float \$1')
        #line 0.75
        #float box
        floatbox_id = bf.appendXFloat(f, 1, 0.75, '0 ')
        #line 1
        cstforencoder_id = bf.appendXObj(f, 0, 1, 'cstforencoder')
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
        #loadbang to message
        bf.appendXConnect(f, loadbang_id, 0, msg_id, 0)
        #loadbang to float object
        bf.appendXConnect(f, loadbang_id, 0, float_id, 0)
        #float object to float box
        bf.appendXConnect(f, float_id, 0, floatbox_id, 0)
        #message to cstforencoder
        bf.appendXConnect(f, msg_id, 0, cstforencoder_id, 0)
        #float box to cstforencoder
        bf.appendXConnect(f, floatbox_id, 0, cstforencoder_id, 1)
        #cstforencoder to sinandcos abstractions
        for j in range(ind):
            bf.appendXConnect(f, cstforencoder_id, 1, sinandcos_id+j, 0)
        #cstforencoder to *~
        for j in range(2*ind):
            bf.appendXConnect(f, cstforencoder_id, 0, mult_id+j, 0)
        #cstforencoder to input 0 of snake~ in
        bf.appendXConnect(f, cstforencoder_id, 0, snake_id, 0)
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