#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.busselector#ind abstractions
_______________________________________________________
"""   
def generate_mcbusselector(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busselector#ind.pd abstraction
        fileName = dDir+'/mc.busselector'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.busselector#ind.pd Pure Data abstraction
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
        in1_id = bf.appendXObj(f, 0.2, 0.5, 'inlet~')
        #inlet~ #1
        in2_id = bf.appendXObj(f, 2, 0.5, 'inlet~')
        #inlet~ #2
        in3_id = bf.appendXObj(f, 4,  0.5, 'inlet')
        #route object
        route_id = bf.appendXObj(f, 4, 0.8, 'route out ramptime')
        #clip object
        clip_id = bf.appendXObj(f, 4, 1.1, 'clip 0 2')
        #snake~ out #ind #1
        snakeout1_id = bf.appendXObj(f, 0.2, 1.1, 'snake~ out '+str(ind))
        #snake~ out #ind #2
        snakeout2_id = bf.appendXObj(f, 2, 1.1, 'snake~ out '+str(ind))
        #out message
        msgout_id = bf.appendXMsg(f, 4, 2.8, 'out \$1')
        #ramptime message
        msgramptime_id = bf.appendXMsg(f, 4.5, 2.8, 'ramptime \$1') 
        #adds ind selector2-mod abstractions
        for j in range(ind):
            k = bf.appendXObj(f, 0.8+j, 3.5, 'selector2-mod')
        #comes back to the first one
        selector2_mult_id = msgramptime_id + 1
        #adds snake~ in #ind object
        snakein_id = bf.appendXObj(f, 0.8, 4, 'snake~ in '+str(ind))
        #adds outlet~ object
        outlet_id = bf.appendXObj(f, 0.8, 4.5, 'outlet~')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to route
        bf.appendXConnect(f, in3_id, 0, route_id, 0)
        #route to clip
        bf.appendXConnect(f, route_id, 0, clip_id, 0)
        #clip to vradio
        bf.appendXConnect(f, clip_id, 0, vradio_id, 0)
        #vradio to out message
        bf.appendXConnect(f, vradio_id, 0, msgout_id, 0)
        #2nd outlet of route (ramptime) to ramptime box number
        bf.appendXConnect(f, route_id, 1, numbox_id, 0)
        #ramptime box number to ramptime msg
        bf.appendXConnect(f, numbox_id, 0, msgramptime_id, 0)
        #inlet~ 1 to snake~ out 1
        bf.appendXConnect(f, in1_id, 0, snakeout1_id, 0)
        #inlet~ 2 to snake~ out 2
        bf.appendXConnect(f, in2_id, 0, snakeout2_id, 0)
        #snake~ in #ind to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        #multiple connections
        for j in range(ind):
            #connects out $1 message to all right inlets of selector2-mod abstractions
            bf.appendXConnect(f, msgout_id, 0, selector2_mult_id+j, 2)
            #connects ramptime $1 message to all right inlets of selector2-mod abstractions
            bf.appendXConnect(f, msgramptime_id, 0, selector2_mult_id+j, 2)
            #connects outlets of the first snake~ out to the left inlet of selector2-mod abstractions
            bf.appendXConnect(f, snakeout1_id, j, selector2_mult_id+j, 0)
            #connects outlets of the second snake~ out to the middle inlet of selector2-mod abstrationcs
            bf.appendXConnect(f, snakeout2_id, j, selector2_mult_id+j, 1)
            #connects all selector2-mod outlets to the inlets of snake~ in #ind object
            bf.appendXConnect(f, selector2_mult_id+j, 0, snakein_id, j)
        f.write('#X coords 0 -1 1 1 90 90 1 100 200;\n')
        f.close()