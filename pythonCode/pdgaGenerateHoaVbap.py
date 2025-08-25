#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the vbap#ind abstractions
_______________________________________________________
"""   
def generate_hoavbap(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for hoa.vbap#ind.pd abstraction
        fileName = dDir+'/hoa.vbap'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.vbap#ind.pd Pure Data abstraction
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.vbap'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ vbap\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        #
        #line 0.5 - inlet~
        in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
        #line 0.5 - inlet
        in2_id = bf.appendXObj(f, 2, 0.5, 'inlet')
        #line 0.75 - snake~ out #ind
        snakeout_id = bf.appendXObj(f, 0, 0.75, 'snake~ out '+str(ind))
        #line 0.75 - route
        route_content = 'route'
        for j in range(ind):
            route_content = route_content + ' a' + str(j)
        route_id = bf.appendXObj(f, 2, 0.75, route_content)
        #vbap elementary modules #ind
        for j in range(ind):
            k = bf.appendXObj(f, j, 1.25, 'vbap'+str(ind)+'_f '+str(j*360/ind))
        #comes back to the first
        multivbap_id = route_id +  1
        #mc.busplus#ind abstractions
        for j in range(ind-1):
            k = bf.appendXObj(f, j*0.5, 1.5+0.25*j, 'mc.busplus'+str(ind))
        #comes back to the first
        multibusplus_id = multivbap_id + ind
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        
        
        f.close()