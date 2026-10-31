#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.meter#ind abstractions
_______________________________________________________
"""   
def generate_mcmeter(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.meter#ind.pd abstraction
        fileName = dDir+'/mc.meter'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.meter#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'mc.meter#ind.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1.5 - snake~ out
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind)+' ----------')
        #line 2 - multiple env~ to measure each channel
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 2, 'env~')
        #comes back to the first one
        env_id = snakeout_id + 1
        #line 2.5 - series of [- 100]
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 2.5, '- 100')
        #comes back to the first one
        minus100_id = snakeout_id + ind + 1
        #the ind-1 normal vumeter (without graduation)   
        for j in range(ind-1):
            k = bf.appendXObj(f, j*0.16 + 0.3, 3.49, 'vu 10 120 empty empty -1 -8 0 10 #404040 #000000 0 0')
        #the last one with the graduation
        k = bf.appendXObj(f, (ind-1)*0.16 + 0.3, 3.49, 'vu 10 120 empty empty -1 -8 0 10 #404040 #000000 1 0')
        #comes back to the first one
        vu_id = minus100_id +  ind
           
        #connections
        #inlet to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #[snake~ out] to the various [env~]
        #and the [env~] to the [- 100]
        #and the [- 100] to the vumeter
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, env_id + j, 0)
            bf.appendXConnect(f, env_id+j, 0, minus100_id+j, 0)
            bf.appendXConnect(f, minus100_id+j, 0, vu_id+j, 0)

        f.write('#X coords 0 -1 1 1 '+str(42+ind*15)+' 145 1 50 355;\n')
        
        f.close()