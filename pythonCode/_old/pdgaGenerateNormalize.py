#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.normalize#ind abstractions
_______________________________________________________
"""   
def generate_normalize(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.decoderblock#ind.pd abstraction
        fileName = dDir+'/mc.normalize'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.normalize#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.normalize'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' mc\ normalize\ for\ '+str(ind)+' channels\ '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()


        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1.5 - snake~ out
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind))
        #line 2 - multiple *~ to get squares of each component
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 2, '*~')
        #comes back to the first one
        mult1_id = snakeout_id + 1
        #line 2.5 - sqrt~~
        sqrt_id = bf.appendXObj(f, ind * 0.5, 2.5, 'sqrt~')
        #line 3 - ==~ 0
        testZero_id = bf.appendXObj(f, ind * 0.5, 3, '==~ 0')
        #line 3.5 - +~~
        plus_id = bf.appendXObj(f, ind * 0.5 - 0.5, 3.5, '+~')
        #line 4 - expr~ 1 / $v1
        expr_id = bf.appendXObj(f, ind * 0.5 -0.5, 4, 'expr~ 1 / $v1')
        #line 4.5 - second series of *~
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 4.5, '*~')
        #comes back to the first one
        mult2_id = expr_id + 1
        #line 5 - snake~ in
        snakein_id = bf.appendXObj(f, 0, 5, 'snake~ in '+str(ind))
        #line 5.5 - outlet~
        out_id = bf.appendXObj(f, 0, 5.5, 'outlet~')
        
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        
        
        #connexions
        #inlet~ to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out to various *~~
        for j in range(ind):
            #connexion of each output of snake~ out to the first input of *~ 1
            bf.appendXConnect(f, snakeout_id, j, mult1_id + j, 0)
            #connexion of each output of snake~ out to the second input of *~ 1
            bf.appendXConnect(f, snakeout_id, j, mult1_id + j, 1)
            #connexion of each output of snake~ out to the first input of *~ 2
            bf.appendXConnect(f, snakeout_id, j, mult2_id + j, 0)
        #connexion of all outputs of *~ 1 to the input of sqrt~~
        for j in range(ind):
            bf.appendXConnect(f, mult1_id + j, 0, sqrt_id, 0)
        #connexion of sqrt~ to ==~ 0
        bf.appendXConnect(f, sqrt_id, 0, testZero_id, 0)
        #connexion of sqrt~ and ==~ to +~~
        bf.appendXConnect(f, sqrt_id, 0, plus_id, 0)
        bf.appendXConnect(f, testZero_id, 0, plus_id, 1)
        #connexion of +~ to expr~~
        bf.appendXConnect(f, plus_id, 0, expr_id, 0)
        #connexion of expr~ to all right inlets of *~ 2
        for j in range(ind):
            bf.appendXConnect(f, expr_id, 0, mult2_id + j, 1)
        #connexion of all *~ 2 to snake~ in
        for j in range(ind):
            bf.appendXConnect(f, mult2_id + j, 0, snakein_id, j)
        #connexion of the snake~ in to the outlet~~
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()