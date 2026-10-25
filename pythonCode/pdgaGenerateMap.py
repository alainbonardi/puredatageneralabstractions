#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.map#ind abstractions
_______________________________________________________
"""   
def generate_hoamap(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the hoa.map#ind.pd abstraction
        fileName = dDir+'/hoa.map'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.map#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.map'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' hoa\ map\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()


        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 1, 1, 'inlet~')
        #line 1 - inlet
        in2_id = bf.appendXObj(f, 3, 1, 'inlet')
        #line 1.25 - route distance
        route_id = bf.appendXObj(f, 3, 1.25, 'route distance')
        #line 2 - hoa.encoder
        encoder_id = bf.appendXObj(f, 1, 2, 'hoa.encoder'+str(ind))
        #line 2 - flonum
        flo_id = bf.appendXFloat(f, 3, 2, '5 0 0 0 - - - 0')       
        #line 2.25 - snake~ out
        snakeout_id = bf.appendXObj(f, 1, 2.25, 'snake~ out '+str(2*ind+1))
        #line 3 - list of mapWeight
        for j in range(ind+1):
            k = bf.appendXObj(f, 3+j, 3, 'mapWeight '+str(ind)+' '+str(j))
        #comes back to the beginning
        mapweight_id = snakeout_id + 1
        #line 4 - mutipliers of the initial encoder
        mult_id = mapweight_id + ind + 1
        for j in range(2*ind+1):
            k = bf.appendXObj(f, j*0.5+1, 4, '*~')
        #line 4.5 - snake~ in
        snakein_id = bf.appendXObj(f, 1, 4.5, 'snake~ in '+str(2*ind+1)+' -------')
        #line 5 - outlet~
        out_id = bf.appendXObj(f, 1, 5, 'outlet~')
        
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        
        #connections
        #inlet to route
        bf.appendXConnect(f, in2_id, 0, route_id, 0)
        #inlet~ to encoder
        bf.appendXConnect(f, in1_id, 0, encoder_id, 0)
        #route to flonum
        bf.appendXConnect(f, route_id, 0, flo_id, 0)
        #outlet 1 of route to inlet1 of encoder
        bf.appendXConnect(f, route_id, 1, encoder_id, 1)
        #hoa.encoder to snake~ out
        bf.appendXConnect(f, encoder_id, 0, snakeout_id, 0)
        #flo_id to mapWeights
        for j in range(ind+1):
            bf.appendXConnect(f, flo_id, 0, mapweight_id+j, 0)
        #snake~ out to *~
        for j in range(2*ind+1):
            bf.appendXConnect(f, snakeout_id, j, mult_id+j, 0)
        #mapWeight ind 0 to inlet 1 of *~ #0
        bf.appendXConnect(f, mapweight_id, 0, mult_id, 1)
        #all other mapWeight ind j+1 to inlet 1 of *~ #2*j+1 and #2*j+2
        for j in range(ind):
            bf.appendXConnect(f, mapweight_id+j+1, 0, mult_id+2*j+1, 1)
            bf.appendXConnect(f, mapweight_id+j+1, 0, mult_id+2*j+2, 1)
        #connects all the *~ to the inlets of the snake~ in
        for j in range(2*ind+1):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #snake~ in to outlet~
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        
        f.close()