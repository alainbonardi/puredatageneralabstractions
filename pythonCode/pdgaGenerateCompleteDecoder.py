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
        for q in range(4, 2*bf.maxAmbiOrder+2+1):
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
            #line 0.5 - loadbang
            loadbang_id = bf.appendXObj(f, 6, 0.5, 'loadbang')
            #line 0.75 - snake~ out #ind abstraction
            decoblock_id = bf.appendXObj(f, 0, 0.75, 'hoa.decoderblock'+str(ind1))
            #line 0.75 - decostereocontrol abstraction
            stereoctl_id = bf.appendXObj(f, 3, 0.75, 'decostereocontrol')
            #line 1.25 - snake_out#ind1
            snakeout_id = bf.appendXObj(f, 0, 1.25, 'snake~ out '+str(nh+1))
            #vbap elementary modules for each virtual source
            for j in range(nh+1):
                #k = bf.appendXObj(f, j, 1.25, 'vbap'+str(q)+'_f '+str(j*360/q))
                k = bf.appendXObj(f, j, 2, 'hoa.vbap'+str(q))
            #comes back to the first
            multivbap_id = snakeout_id +  1
            #mc.busplus#ind abstractions
            for j in range(nh):
                k = bf.appendXObj(f, j*0.5, 2.5+0.25*j, 'mc.busplus'+str(q))
            #comes back to the first
            multibusplus_id = multivbap_id + nh + 1
            #messages for the initialization of the angles of the virtual sources
            for j in range(nh+1):
                k = bf.appendXMsg(f, j+0.5, 1.75, str(j*360/(nh+1)))
            #comes back to the first
            multimsg_id = multibusplus_id + nh
            #
            #outlet~~
            out_id = bf.appendXObj(f, 0.5*(nh+1), 2.5+0.25*(nh+4), 'outlet~')
            #hoa.2dprojection#ind1
            hoa2dproj_id = bf.appendXObj(f, nh+1, 1.25, 'hoa.2dprojection'+str(ind1))
            #mc.stereozeropad#q
            mczeropad_id = bf.appendXObj(f, nh+1, 2, 'mc.stereozeropad'+str(q))
            #mc.busselector#q
            mcbussel_id = bf.appendXObj(f, (nh+1)*0.5, 2.5+0.25*nh, 'mc.busselector'+str(q))
            #
            f.write(bf.patchMiddleCredits)
            bf.incObjInd()
            #----------connections-----------#
            #inlet~ to decoderblock#ind1
            bf.appendXConnect(f, in1_id, 0, decoblock_id, 0)
            #decoderblock#ind1 to snake~ out#ind1
            bf.appendXConnect(f, decoblock_id, 0, snakeout_id, 0)
            #inlet to decostereocontrol abstraction
            bf.appendXConnect(f, in2_id, 0, stereoctl_id, 0)
            #decostereocontrol abstraction to mc.busselector#q abstraction
            bf.appendXConnect(f, stereoctl_id, 0, mcbussel_id, 2)
            #bf.appendXConnect(f, in2_id, 0, route_id, 0)
            #the snake_out outputs are connected to all the first inputs of the vbap abstractions
            for j in range(nh+1):
                bf.appendXConnect(f, snakeout_id, j, multivbap_id+j, 0)
            #the decostereocontrol abstraction is connected to all second inputs of hoa.vbap#i abstractions
            for j in range(nh+1):
                bf.appendXConnect(f, stereoctl_id, 1, multivbap_id+j, 1)
            #the loadbang object is connected to all messages
            for j in range(nh+1):
                bf.appendXConnect(f, loadbang_id, 0, multimsg_id+j, 0)
            #the messages are connected to the vbap#i abstractions
            for j in range(nh+1):
                bf.appendXConnect(f, multimsg_id+j, 0, multivbap_id+j, 2)
            #connects the two first hoa.vbap#i to the inputs of the mc.busplus#i
            bf.appendXConnect(f, multivbap_id, 0, multibusplus_id, 0)
            bf.appendXConnect(f, multivbap_id+1, 0, multibusplus_id, 1)
            #connects the following hoa.vbap#i to the inputs of the mc.busplus#i
            for j in range(2, nh+1):
                bf.appendXConnect(f, multivbap_id+j, 0, multibusplus_id+j-1, 1)
            #connections between the mc.busplus#i
            for j in range(nh-1):
                bf.appendXConnect(f, multibusplus_id+j, 0, multibusplus_id+j+1, 0)
            #connection between the hoa.decoblock#ind1 and the hoa.2dprojection#ind1 abstractions
            bf.appendXConnect(f, decoblock_id, 0, hoa2dproj_id, 0)
            #connection between the hoa.2dprojection#ind1 and the mc.stereozeropad#q abstractions
            bf.appendXConnect(f, hoa2dproj_id, 0, mczeropad_id, 0)
            #connection between the last mc.busplus#q and the mc.busselector#q abstractions
            bf.appendXConnect(f, multibusplus_id+nh-1, 0, mcbussel_id, 0)
            #connection between the mc.stereozeropad#q and the mc.busselector#q abstractions
            bf.appendXConnect(f, mczeropad_id, 0, mcbussel_id, 1)
            #connection between the mc.busselector#q and the outlet~ object
            bf.appendXConnect(f, mcbussel_id, 0, out_id, 0)
            

            #
            f.close()