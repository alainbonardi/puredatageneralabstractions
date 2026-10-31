#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the sa.ambi2sa#ind abstractions
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
Generates the sa.sa2ambi#ind abstractions
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
        #connects the inlet~ to the snake~ out
        bf.appendXConnect(f, in1_id, 0, snake1_id, 0)
        #connects the snake~ out outlets to the ambiPolToCar modules
        #first outlet directly to snake~ in first inlet
        bf.appendXConnect(f, snake1_id, 0, snake2_id, 0)
        #first the other amplitudes to the inlet 0 of each ambiPolToCar
        #then the phases to the inlet 1 of each ambiPolToCar
        for j in range(ind):
            bf.appendXConnect(f, snake1_id, j+1, mult_id+j, 0)
            bf.appendXConnect(f, snake1_id, j+ind+1, mult_id+j, 1)
            #bf.appendXConnect(f, snake1_id, 2*(j+1), mult_id+j, 1)
        #connects the ambiPolToCar outlets to the snake~ in inlets
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snake2_id, 2*j+1)
            bf.appendXConnect(f, mult_id+j, 1, snake2_id, 2*(j+1))
        #connects the snake~ in outlet to the outlet~
        bf.appendXConnect(f, snake2_id, 0, out_id, 0)
        f.close()
        
        
"""
_______________________________________________________
Generates the sa.encoder#ind abstractions
_______________________________________________________
"""   
def generate_saencoders(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/sa.encoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' sa.encoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' spectral\ ambisonic\ encoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #line 0.5 - sig~ 1
        sig1_id = bf.appendXObj(f, 0, 0.5, 'sig~ 1')
        #inlet~ for the phase
        in_id = bf.appendXObj(f, 1.5, 0.5, 'inlet~')
        #line 1 - phasesmoother abstraction
        phsmoo_id = bf.appendXObj(f, 1.5, 1, 'phasesmoother')
        #line 2 - *~ multipliers
        for j in range(ind):
            k = bf.appendXObj(f, 1.5+j*0.5, 2, '*~ '+str(j+1))
        #comes back to the first *~
        mult_id = phsmoo_id + 1
        #line 3 - snake~ in 
        snakein_id = bf.appendXObj(f, 0, 3, 'snake~ in '+str(2*ind+1))
        #line 4 - outlet~
        out_id = bf.appendXObj(f, 0, 4, 'outlet~')

        #writes the connections
        #connects the sig~ 1 to the first (ind+1) inlets of snake~ in
        for j in range(ind+1):
            bf.appendXConnect(f, sig1_id, 0, snakein_id, j)
        #connects the inlet~ to phasesmoother
        bf.appendXConnect(f, in_id, 0, phsmoo_id, 0)
        #connects the outlet of phasesmoother to all the inlets of the *~~
        for j in range(ind):
            bf.appendXConnect(f, phsmoo_id, 0, mult_id+j, 0)
        #connects the outlets of the *~ to the right inlets of snake~ in
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, ind+1+j)
        #connects the outlet of the snake~ in to the inlet of the outlet~
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        '''
        bf.appendXConnect(f, in1_id, 0, encomod_id, 0)
        #connects the inlet 2 to the encodercontrol abstraction
        bf.appendXConnect(f, in2_id, 0, encoctrl_id, 0)
        #connects the encodercontrol to the right inlet of encodingmodule#ind
        bf.appendXConnect(f, encoctrl_id, 0, encomod_id, 1)
        #connects the encodingmodule#ind to the outlet
        bf.appendXConnect(f, encomod_id, 0, out_id, 0)
        '''
        f.close()