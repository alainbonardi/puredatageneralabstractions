#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.decoder#ind abstractions
_______________________________________________________
"""   
def generate_hoadeco(dDir):
    for i1 in range(bf.maxAmbiOrder):
        #ind1 is the ambisonic order, between 1 and maxAmbiOder
        ind1 = i1 + 1
        nh = 2 * ind1 + 1
        for q in range(nh, 2*bf.maxAmbiOrder+2):
            #opens a Pure Data file for hoa.vbap#i1_#q.pd abstraction
            fileName = dDir+'/hoa.decoder'+str(ind1)+'_'+str(q)+".pd"
            f = open(fileName, 'w')
            #writes the lines of the hoa.decoder#i1_#q.pd Pure Data abstraction
            f.write(bf.patchMiddleCanvas)
            f.write(bf.patchAbstractionCnv1_1+' hoa.decoder'+str(ind1)+'_'+str(q)+' '+bf.patchAbstractionCnv2_1+'\n')
            bf.resetObjInd()
            f.write(bf.patchAbstractionCnv1_2+ ' hoa\ decoder\ at\ ambisonic\ order\ '+str(ind1)+'\ to\ '+str(q)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
            bf.incObjInd()
            #
            #line 0.5 - inlet~
            in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
            #line 0.5 - inlet
            in2_id = bf.appendXObj(f, 3, 0.5, 'inlet')
            #line 0.75 - snake~ out #ind
            snakeout_id = bf.appendXObj(f, 0, 0.75, 'snake~ out '+str(q))
            #line 0.75 - route
            route_content = 'route'
            for j in range(q):
                route_content = route_content + ' a' + str(j)
            route_id = bf.appendXObj(f, 3, 0.75, route_content)
            #vbap elementary modules for each virtual source
            for j in range(q):
                k = bf.appendXObj(f, j, 1.25, 'vbap'+str(q)+'_f '+str(j*360/q))
            #comes back to the first
            multivbap_id = route_id +  1
            #mc.busplus#ind abstractions
            for j in range(q-1):
                k = bf.appendXObj(f, j*0.5, 1.5+0.25*j, 'mc.busplus'+str(q))
            #comes back to the first
            multibusplus_id = multivbap_id + q
            #
            #outlet~~
            out_id = bf.appendXObj(f, 0.5*(q-2), 1.5+0.25*(q-1), 'outlet~')
            #
            f.write(bf.patchMiddleCredits)
            bf.incObjInd()
            #connections
            #inlet~ to snake~ out
            bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
            #inlet to route
            bf.appendXConnect(f, in2_id, 0, route_id, 0)
            #the snake_out outputs are connected to all the first inputs of the vbap abstractions
            for j in range(q):
                bf.appendXConnect(f, snakeout_id, j, multivbap_id+j, 0)
            #the outputs of the route object are connected to all the inputs (#1 to #ind2) of the vbap abstractions
            for j in range(q):
                for k in range(q):
                    bf.appendXConnect(f, route_id, j, multivbap_id+k, j+1)
            #connection of the first two vbap abstractions to the first mc.busplus
            bf.appendXConnect(f, multivbap_id, 0, multibusplus_id, 0)
            bf.appendXConnect(f, multivbap_id+1, 0, multibusplus_id, 1)
            #
            f.close()