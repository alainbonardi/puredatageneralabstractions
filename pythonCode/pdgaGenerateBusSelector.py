#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.player#ind abstractions
_______________________________________________________
"""   
def generate_mcbusselector(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.busselector'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.player#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.busselector'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ bus\ selector\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #vradio in the canvas to select the input
        vradio_id = bf.appendXObj(f, 0.8, 1.9, 'vradio 16 1 0 3 empty empty empty 0 -8 0 10 #fcfcfc #000000 #000000 0')
        #number_box
        numbox_id = bf.appendXFloat(f, 0.8, 2.45, 'ramptime')
        #control inlet
        in1_id = bf.appendXObj(f, 0.2, 0.5, 'inlet')
        #inlet~ #1
        in2_id = bf.appendXObj(f, 2, 0.5, 'inlet~')
        #inlet~ #2
        in3_id = bf.appendXObj(f, 4,  0.5, 'inlet~')
        #route object
        route_id = bf.appendXObj(f, 0.2, 0.8, 'route out ramptime')
        #clip object
        clip_id = bf.appendXObj(f, 0.2, 1.1, 'clip 0 2')
        #snake~ out #ind #1
        snakeout1_id = bf.appendXObj(f, 2, 1.1, 'snake~ out '+str(ind))
        #snake~ out #ind #2
        snakeout2_id = bf.appendXObj(f, 4, 1.1, 'snake~ out '+str(ind))
        #out message
        msgout_id = bf.appendXMsg(f, 0.2, 2.6, 'out $1')
        #ramptime message
        
        #toggle in the canvas to play
        #various *~ (#ind instances)
        #for j in range(ind):
        #    k = bf.appendXObj(f, 2.5+0.5*j, 4.5, '*~')
        #comes back to the first one
        #mult_id = float_id + 1
        #snake~ in #ind object
        #snakein_id = bf.appendXObj(f, 2.5, 4.75, 'snake~ in '+str(ind))
        #outlet~ object
        #out_id = bf.appendXObj(f, 2.5, 5, 'outlet~')
        #level msg
        #msglevel_id = bf.appendXMsg(f, 2.5+0.5*ind, 3.75, '\$1 20')
        #line~ object
        #line_id = bf.appendXObj(f, 2.5+0.5*ind, 4, 'line~')
        #trigger object
        #trig_id = bf.appendXObj(f, 2, 2.25, 't f b')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to route
        #bf.appendXConnect(f, in_id, 0, route_id, 0)
        #vol in route to hsl vol
        #bf.appendXConnect(f, route_id, 0, hslvol_id, 0)
        #play in route to play toogle
        #bf.appendXConnect(f, route_id, 1, tglplay_id, 0)
        #loop in route to loop toggle
        #bf.appendXConnect(f, route_id, 2, tglloop_id, 0)
        #open bang to openpanel object
        #bf.appendXConnect(f, bngopen_id, 0, openpanel_id, 0)
        #play toggle to trigger object
        #bf.appendXConnect(f, tglplay_id, 0, trig_id, 0)
        #trigger object to readsf~ #ind
        #bf.appendXConnect(f, trig_id, 0, readsf_id, 0)
        #trigger object to open message
        #bf.appendXConnect(f, trig_id, 1, msgopen_id, 0)
        #openpanel object to list prepend object
        #bf.appendXConnect(f, openpanel_id, 0, list1_id, 0)
        #list prepend object to list trim object
        #bf.appendXConnect(f, list1_id, 0, list2_id, 0)
        #list trim to message open
        #bf.appendXConnect(f, list2_id, 0, msgopen_id, 0)
        #message open to readsf object
        #bf.appendXConnect(f, msgopen_id, 0, readsf_id, 0)
        #last output of readsf~ to bang object
        #bf.appendXConnect(f, readsf_id, ind, bang_id, 0)
        #bang object to float object
        #bf.appendXConnect(f, bang_id, 0, float_id, 0)
        #loop toggle to float object
        #bf.appendXConnect(f, tglloop_id, 0, float_id, 1)
        #float object to play toggle
        #bf.appendXConnect(f, float_id, 0, tglplay_id, 0)
        #hsl vol to level msg
        #bf.appendXConnect(f, hslvol_id, 0, msglevel_id, 0)
        #level msg to line~ object
        #bf.appendXConnect(f, msglevel_id, 0, line_id, 0)
        #connections between readsf~ object to the various *~~
        #for j in range(ind):
            #bf.appendXConnect(f, readsf_id, j, mult_id+j, 0)
        #connections between line~ object to the various *~
        #for j in range(ind):
            #bf.appendXConnect(f, line_id, 0, mult_id+j, 1)
        #connections between the various *~ and snake~ in #ind object
        #for j in range(ind):
            #bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #snake~ in #ind object to outlet~ object
        #bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.write('#X coords 0 -1 1 1 90 90 1 100 200;\n')
        f.close()