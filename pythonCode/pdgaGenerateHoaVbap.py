#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the vbap#ind abstractions
_______________________________________________________
"""   
def generate_hoavbap(dDir):
    #one source is spatialized on ind2 loudspeakers using vbap
    for i in range(2*bf.maxAmbiOrder+1):
        #ind is the number of loudspeakers, from 2 to 2*maxAmbiOrder+2
        ind = i +2
        #opens a Pure Data file for hoa.vbap#ind.pd abstraction
        fileName = dDir+'/hoa.vbap'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.vbap#ind.pd Pure Data abstraction
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.vbap'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ vbap\ of\ one\ source\ on\ '+str(ind)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
            #
        #line 0.5 - inlet~
        in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
        #line 0.5 - inlet for the angles of the loudspeakers
        in2_id = bf.appendXObj(f, 3, 0.5, 'inlet')
        #line 0.5 - inlet for the angle of the source
        in3_id = bf.appendXObj(f, 6, 0.5, 'inlet')
        #line 0.75 - route
        route_content = 'route'
        for j in range(ind):
            route_content = route_content + ' a' + str(j)
        route_id = bf.appendXObj(f, 3, 0.75, route_content)
        #vbap elementary modules for each loudspeaker
        for j in range(ind):
            k = bf.appendXObj(f, j, 1.5, 'vbap'+str(ind)+'_f')
        #comes back to the first
        multivbap_id = route_id +  1
        #mc.busplus#ind abstractions
        for j in range(ind-1):
            k = bf.appendXObj(f, j*0.5, 1.75+0.25*j, 'mc.busplus'+str(ind))
        #comes back to the first
        multibusplus_id = multivbap_id + ind
        #
        #outlet~~
        out_id = bf.appendXObj(f, 0.5*(ind-2), 1.75+0.25*(ind-1), 'outlet~')
        #connection of the first two vbap abstractions to the 
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ to snake~ out
        #no longer the snake_out
        #bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #inlet to route
        bf.appendXConnect(f, in2_id, 0, route_id, 0)
        #the source is connected to all the first inputs of the vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, in1_id, 0, multivbap_id+j, 0)
        #the outputs of the route object are connected to all the inputs (#1 to #ind2) of the vbap abstractions
        for j in range(ind):
            for k in range(ind):
                bf.appendXConnect(f, route_id, j, multivbap_id+k, j+1)
        #the last inlet (angle of the source) is connected to all the last inputs of the vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, in3_id, 0, multivbap_id+j, ind + 1)
        #first and second vbaps are connected to the inputs of the first mc.busplus
        bf.appendXConnect(f, multivbap_id, 0, multibusplus_id, 0)
        bf.appendXConnect(f, multivbap_id+1, 0, multibusplus_id, 1)
        #other vbaps connected to the right input of the other mc.busplus
        for j in range(2, ind):
            bf.appendXConnect(f, multivbap_id+j, 0, multibusplus_id+j-1, 1)
        #mc.busplus connected to each other if ind > 2
        if (ind > 2):
            for j in range(ind-2):
                bf.appendXConnect(f, multibusplus_id+j, 0, multibusplus_id+j+1, 0)
        #connection of the last mc.busplus to the outlet~~
        bf.appendXConnect(f, multibusplus_id+ind-2, 0, out_id, 0)
        #
        f.close()