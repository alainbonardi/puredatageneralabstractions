#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the ambi2sa#ind abstractions
_______________________________________________________
"""     
def generate_atosAbstractions(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the sa.ambi2sa#ind.pd abstraction
        fileName = dDir+'/sa.ambi2sa'+str(ind)+".pd"
        f = open(fileName, 'w')
        #
        #writes the lines of the sa.ambi2sa#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'sa.ambi2sa#ind.pd')
        #line 1
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #in2_id = bf.appendXObj(f, 1, 1, 'inlet~')
        #line 5
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 1.5
        snake1_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(2*ind+1))

        #writes the ambiCarToPol on line 3
        for j in range(ind):
            k = bf.appendXObj(f, j+0.5, 3, 'sa.ambicar2pol')
        #comes back to the first one
        mult_id = snake1_id + 1
        #line 4
        snake2_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(2*ind+1))
        #writes the connections
        #connects the inlet to the snake~ out
        bf.appendXConnect(f, in1_id, 0, snake1_id, 0)
        #connects the snake~ out outlets to the ambiCarToPol modules
        #first outlet directly to snake~ in first inlet
        bf.appendXConnect(f, snake1_id, 0, snake2_id, 0)
        #next outlets to 
        for j in range(ind):
            #connections to the 2 inputs of each ambiCarToPol
            bf.appendXConnect(f, snake1_id, 1+2*j, mult_id+j, 0)
            bf.appendXConnect(f, snake1_id, 2*(j+1), mult_id+j, 1)
        #connects the ambiCarToPol outlets to the snake~ in inlets
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snake2_id, 2*j+1)
            bf.appendXConnect(f, mult_id+j, 1, snake2_id, 2*(j+1))
        #connects the snake~ in outlet to the outlet~
        bf.appendXConnect(f, snake2_id, 0, out_id, 0)
        f.close()
        
        
"""
_______________________________________________________
Generates the spectralToAmbi#ind abstractions
_______________________________________________________
"""     
def generate_stoaAbstractions(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the sa.sa2ambi#ind.pd abstraction
        fileName = dDir+'/sa.sa2ambi'+str(ind)+".pd"
        f = open(fileName, 'w')
        #
        #writes the lines of the sa.sa2ambi#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'sa.sa2ambi#ind.pd')
        #line 1
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #in2_id = bf.appendXObj(f, 1, 1, 'inlet~')
        #line 5
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 1.5
        snake1_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(2*ind+1))

        #writes the ambiPolToCar on line 3
        for j in range(ind):
            k = bf.appendXObj(f, j+0.5, 3, 'sa.ambipol2car')
        #comes back to the first one
        mult_id = snake1_id + 1
        #line 4
        snake2_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(2*ind+1))
        #writes the connections
        #connects the inlet to the snake~ out
        bf.appendXConnect(f, in1_id, 0, snake1_id, 0)
        #connects the snake~ out outlets to the ambiPolToCar modules
        #first outlet directly to snake~ in first inlet
        bf.appendXConnect(f, snake1_id, 0, snake2_id, 0)
        #next outlets to 
        for j in range(ind):
            #connections to the 2 inputs of each ambiPolToCar
            bf.appendXConnect(f, snake1_id, 1+2*j, mult_id+j, 0)
            bf.appendXConnect(f, snake1_id, 2*(j+1), mult_id+j, 1)
        #connects the ambiPolToCar outlets to the snake~ in inlets
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snake2_id, 2*j+1)
            bf.appendXConnect(f, mult_id+j, 1, snake2_id, 2*(j+1))
        #connects the snake~ in outlet to the outlet~
        bf.appendXConnect(f, snake2_id, 0, out_id, 0)
        f.close()