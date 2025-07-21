#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.sp#ind abstractions
_______________________________________________________
"""     
def generate_mcsp(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.sp#ind.pd abstraction
        fileName = dDir+'/mc.sp'+str(ind)+".pd"
        f = open(fileName, 'w')
        #
        #writes the lines of the mc.sp#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'mc.sp#ind.pd')
        #line 1
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        in2_id = bf.appendXObj(f, 1, 1, 'inlet~')
        #line 5
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 1.5
        snake1_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind))
        snake2_id = bf.appendXObj(f, 1, 1.5, 'snake~ out '+str(ind))
        #writes the *~ on the line 3
        for j in range(ind):
            #the ids of the *~ are between 7 and 7+ind-1
            k = bf.appendXObj(f, j*0.5, 3, '*~')
        #comes back to the first one
        mult_id = snake2_id + 1
        #writes the connections
        #connects the inlets to the snake~ out
        bf.appendXConnect(f, in1_id, 0, snake1_id, 0)
        bf.appendXConnect(f, in2_id, 0, snake2_id, 0)
        #connects the snake~ out to the *~~
        #connects the *~ to the outlet~
        for j in range(ind):
            bf.appendXConnect(f, snake1_id, j, mult_id+j, 0)
            bf.appendXConnect(f, snake2_id, j, mult_id+j, 1)
            bf.appendXConnect(f, mult_id+j, 0, out_id, 0)
        f.close()