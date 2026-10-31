#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.encoder#ind abstractions
_______________________________________________________
"""   
def generate_hoaencoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.encoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.encoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ ambisonic\ encoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #line 0.5 - inlet~
        in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2.5, 0.5, 'inlet')
        #line 1 - encodercontrol abstraction
        encoctrl_id = bf.appendXObj(f, 2.5, 1, 'encodercontrol')
        #line 2 - hoa.encodingmodule#ind
        encomod_id = bf.appendXObj(f, 0, 2, 'hoa.encodingmodule'+str(ind))
        #line 3 - outlet~
        out_id = bf.appendXObj(f, 0, 3, 'outlet~')

        #writes the connections
        #connects the inlet~ 1 to the first input of hoa.encodingmodule#ind
        bf.appendXConnect(f, in1_id, 0, encomod_id, 0)
        #connects the inlet 2 to the encodercontrol abstraction
        bf.appendXConnect(f, in2_id, 0, encoctrl_id, 0)
        #connects the encodercontrol to the right inlet of encodingmodule#ind
        bf.appendXConnect(f, encoctrl_id, 0, encomod_id, 1)
        #connects the encodingmodule#ind to the outlet
        bf.appendXConnect(f, encomod_id, 0, out_id, 0)
        
        f.close()
        
        
       
""" 
_______________________________________________________
Generates the hoa.cstencoder#ind abstractions
_______________________________________________________
"""   
def generate_hoacstencoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.cstencoder#ind.pd abstraction
        fileName = dDir+'/hoa.cstencoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.cstencoder#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.cstencoder#ind.pd')
        #line 0.25
        #loadbang
        loadbang_id = bf.appendXObj(f, 0, 0.25, 'loadbang')
        #line 0.5
        #msg
        msg_id = bf.appendXMsg(f, 0, 0.5, str(ind))
        #float
        float_id = bf.appendXObj(f, 1, 0.5, 'float \$1')
        #line 0.75
        #float box
        floatbox_id = bf.appendXFloat(f, 1, 0.75, '0 ')
        #line 1
        cstforencoder_id = bf.appendXObj(f, 0, 1, 'cstforencoder')
        #line 4.5
        #snake~ in
        snake_id = bf.appendXObj(f, 0, 4.5, 'snake~ in '+str(2*ind+1)+' ----------')
        #line 5
        #outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #sinandcos abstractions
        for j in range(ind):
            ind2 = j + 1
            k = bf.appendXObj(f, ind2, 3, 'sinandcos '+str(ind2))
            #ids from 9 to 9+ind-1
        #comes back to the first one
        sinandcos_id = out_id + 1
        #line 4
        #*~
        for j in range(2*ind):
            ind2 = j + 1
            ind3 = 0.5 * ind2
            k = bf.appendXObj(f, ind3, 3.5, '*~')
            #ids from 9+ind to 9+3*ind-1
        #comes back to the first one
        mult_id = sinandcos_id + ind
        #connections
        #loadbang to message
        bf.appendXConnect(f, loadbang_id, 0, msg_id, 0)
        #loadbang to float object
        bf.appendXConnect(f, loadbang_id, 0, float_id, 0)
        #float object to float box
        bf.appendXConnect(f, float_id, 0, floatbox_id, 0)
        #message to cstforencoder
        bf.appendXConnect(f, msg_id, 0, cstforencoder_id, 0)
        #float box to cstforencoder
        bf.appendXConnect(f, floatbox_id, 0, cstforencoder_id, 1)
        #cstforencoder to sinandcos abstractions
        for j in range(ind):
            bf.appendXConnect(f, cstforencoder_id, 1, sinandcos_id+j, 0)
        #cstforencoder to *~
        for j in range(2*ind):
            bf.appendXConnect(f, cstforencoder_id, 0, mult_id+j, 0)
        #cstforencoder to input 0 of snake~ in
        bf.appendXConnect(f, cstforencoder_id, 0, snake_id, 0)
        #sinandcos to *~~
        for j in range(ind):
            bf.appendXConnect(f, sinandcos_id+j, 0, mult_id+2*j, 1)
            bf.appendXConnect(f, sinandcos_id+j, 1, mult_id+2*j+1, 1)
        #*~ to snake~ in
        for j in range(2*ind):
            bf.appendXConnect(f, mult_id+j, 0, snake_id, j+1)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snake_id, 0, out_id, 0)
        f.close()

        

"""
_______________________________________________________
Generates the hoa.encodingmodule#ind abstractions
_______________________________________________________
"""   
def generate_hoaencodingmodule(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the hoa.encodingmodule#ind.pd abstraction
        fileName = dDir+'/hoa.encodingmodule'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.encodingmodule#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.encodingmodule#ind.pd')
        #line 0.25 - inlet~ 1 - signal
        in1_id = bf.appendXObj(f, 0, 0.25, 'inlet~')
        #line 0.25- inlet~ 2 - phase (angle between 0 and 1)
        in2_id = bf.appendXObj(f, 3, 0.25, 'inlet~')
        #line 4.5
        #snake~ in
        snake_id = bf.appendXObj(f, 0, 4.5, 'snake~ in '+str(2*ind+1)+' ----------')
        #line 5
        #outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #sinandcos abstractions
        for j in range(ind):
            ind2 = j + 1
            k = bf.appendXObj(f, ind2, 3, 'sinandcos '+str(ind2))
            #ids from 9 to 9+ind-1
        #comes back to the first one
        sinandcos_id = out_id + 1
        #line 4
        #*~
        for j in range(2*ind):
            ind2 = j + 1
            ind3 = 0.5 * ind2
            k = bf.appendXObj(f, ind3, 3.5, '*~')
            #ids from 9+ind to 9+3*ind-1
        #comes back to the first one
        mult_id = sinandcos_id + ind
        #connections
        #inlet~ 2 to sinandcos abstractions
        for j in range(ind):
            bf.appendXConnect(f, in2_id, 0, sinandcos_id+j, 0)
        #inlet~ 1 to *~
        for j in range(2*ind):
            bf.appendXConnect(f, in1_id, 0, mult_id+j, 0)
        #inlet~ 1 to input 0 of snake~ in
        bf.appendXConnect(f, in1_id, 0, snake_id, 0)
        #sinandcos to *~~
        for j in range(ind):
            bf.appendXConnect(f, sinandcos_id+j, 0, mult_id+2*j, 1)
            bf.appendXConnect(f, sinandcos_id+j, 1, mult_id+2*j+1, 1)
        #*~ to snake~ in
        for j in range(2*ind):
            bf.appendXConnect(f, mult_id+j, 0, snake_id, j+1)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snake_id, 0, out_id, 0)
        f.close()
        

"""
_______________________________________________________
Generates the hoa.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_hoadecoderblock(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.decoderblock#ind.pd abstraction
        fileName = dDir+'/hoa.decoderblock'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'hoa.decoderblock#ind.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1.5 - snake~ out
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(2*ind+1))
        #line 2 - *~0.5
        mult_id = bf.appendXObj(f, 0, 2, '*~ 0.5')
        #line 2.5 - snake~ in
        snakein1_id = bf.appendXObj(f, 0, 2.5, 'snake~ in '+str(2*ind+1))
        #line 4 - snake~ in
        snakein2_id = bf.appendXObj(f, 0.5*ind, 4, 'snake~ in '+str(2*ind+2))
        #line 4.5 - outlet~~
        out_id = bf.appendXObj(f, 0.5*ind, 4.5, 'outlet~')
        #line 2 - mc.cstencoder#ind
        for j in range(2*ind+2):
            ind2 = j + 1
            k = bf.appendXObj(f, ind2, 2, 'hoa.cstencoder'+str(ind)+' '+str(j))
        #comes back to the first one
        cstencoder_id = out_id + 1
        #cstencoder_id between 8 and 8+2*ind+1
        #line 3 - mc.sp#2*ind+1
        for j in range(2*ind+2):
            ind2 = j + 1
            k = bf.appendXObj(f, j, 3, 'mc.sp'+str(2*ind+1))
        #comes back to the first one
        sp_id = cstencoder_id+2*ind+2
        #connexions
        #inlet~ to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out 0 to *~0.5
        bf.appendXConnect(f, snakeout_id, 0, mult_id, 0)
        #*~0.5 to snake~ in 0
        bf.appendXConnect(f, mult_id, 0, snakein1_id, 0)
        #snake~ out 1 to 2*ind to snake~ in 1 to 2*ind
        for j in range(2*ind):
            ind2 = j + 1
            bf.appendXConnect(f, snakeout_id, ind2, snakein1_id, ind2)
        #mc.cstencoder#j to mc.sp#j inlet 1
        for j in range(2*ind+2):
            bf.appendXConnect(f, cstencoder_id+j, 0, sp_id+j, 1)
        #snake~ in to mc.sp#j inlet 0
        for j in range(2*ind+2):
            bf.appendXConnect(f, snakein1_id, 0, sp_id+j, 0)
        #mc.sp#j outlet 0 to snake~ in inlet j
        for j in range(2*ind+2):
            bf.appendXConnect(f, sp_id+j, 0, snakein2_id, j)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snakein2_id, 0, out_id, 0)
        f.close()
        

"""
_______________________________________________________
Generates the hoa.regdecoder#ind abstractions
_______________________________________________________
"""   
def generate_hoaregdecoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.regdecoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.regdecoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' ambisonic\ regular\ decoder\ at\ order\ '+str(ind)+'\ to\ '+str(2*ind+2)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #03/01/2026 - remove the amplitude control from the regular decoder
        #bf.appendXText(f, 2.5, 1, 'amp+value message')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #03/01/2026 - remove the amplitude control from the regular decoder
        #inlet for the message amp+value
        #in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - mc.decoderblock1#ind
        mcdb_id = bf.appendXObj(f, 0, 1.5, 'hoa.decoderblock'+str(ind))
        #03/01/2026 - remove the amplitude control from the regular decoder
        #line 3 - mc.gain#(2*ind+2)
        #mcga_id = bf.appendXObj(f, 0, 3, 'mc.gain'+str(2*ind+2))
        #line 3.5 - outlet~
        out_id = bf.appendXObj(f, 0, 3.5, 'outlet~')
        #writes the connections
        #connects the inlet~ to the mc.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, mcdb_id, 0)
        #03/01/2026 - remove the amplitude control from the regular decoder
        #connects the mc.decoderblock#ind to the mc.gain#(2*ind+2)
        #bf.appendXConnect(f, mcdb_id, 0, mcga_id, 0)
        #connects the mc.gain#(2*ind+2) to the outlet~~
        #bf.appendXConnect(f, mcga_id, 0, out_id, 0)
        #connects the inlet to the right input of the mc.gain#(2*ind+2)
        #bf.appendXConnect(f, in2_id, 0, mcga_id, 1)
        bf.appendXConnect(f, mcdb_id, 0, out_id, 0)
        #
        f.close()
        

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
                k = bf.appendXObj(f, j, 2, 'mc.vbap'+str(q))
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
            #the decostereocontrol abstraction is connected to all second inputs of mc.vbap#i abstractions
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
            f.close()
            
            
"""
_______________________________________________________
Generates the hoa.2dprojection#ind abstractions
_______________________________________________________
"""   
def generate_hoa2dprojection(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.2dprojection'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.2dprojection'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' stereoprojection\ of\ a\ regular\ decoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 2 - snake~ out #2*ind+2
        snakeout_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(2*ind+2))
        #line 3 - 2*ind+2 stereogains
        for j in range(2*ind+2):
            k = bf.appendXObj(f, j*1.2, 3, 'stereogains '+str(j*360/(2*ind+2)))
        #comes back to the first
        stereog_id = snakeout_id+1
        #line 4 - snake~ in 2
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in 2')
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #line 4.5- mc.gains2
        #mcg_id = bf.appendXObj(f, 0, 4.5, 'mc.gain2')
        #line 5 - outlet~~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #connections
        #inlet~ to snake~ out
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #all the outputs of snake~ out #2*ind+2 to the various stereogains
        for j in range(2*ind+2):
            bf.appendXConnect(f, snakeout_id, j, stereog_id+j, 0)
        #connects the left outputs of stereogains objects to the left input of snake~ in 2
        for j in range(2*ind+2):
            bf.appendXConnect(f, stereog_id+j, 0, snakein_id, 0)
        #connects the right outputs of stereogains objects to the right input of snake~ in 2
        for j in range(2*ind+2):
            bf.appendXConnect(f, stereog_id+j, 1, snakein_id, 1)  
        #connects the snake~ in 2 object to the mc.gain2 object
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #bf.appendXConnect(f, snakein_id, 0, mcg_id, 0)
        #connects the mc.gain2 object to the outlet~~
        #bf.appendXConnect(f, mcg_id, 0, out_id, 0)
        #connects the inlet to the right input of mc.gain2
        #bf.appendXConnect(f, in2_id, 0, mcg_id, 1)
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        #
        f.close()
        
        
"""
_______________________________________________________
Generates the vbap#ind abstractions
_______________________________________________________
"""   
def generate_vbap(dDir):
    for i in range (1, 2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for vbap#ind_f.pd abstraction
        fileName = dDir+'/vbap'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the vbap#ind_f.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'vbap#ind_f.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1 - (ind) inlets
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 1, 'inlet')
        #comes back to the first one
        multiinlet_id = in_id + 1
        """
        #loadbang
        loadbang_id = bf.appendXObj(f, ind+1, 1, 'loadbang')
        #float object
        float_id = bf.appendXObj(f, ind+1, 1.5, 'float \$1')
        """
        #inlet for the angle of the source
        in_ang_id = bf.appendXObj(f, ind+1, 1, 'inlet')
        #vbap abstractions
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 2, 'vbap')
        #comes back to the first one
        multivbap_id = in_ang_id + 1
        #+~ objects
        for j in range(ind):
            k = bf.appendXObj(f, j+1, 3, '+~')
        #comes back to the first one
        multiplus_id = multivbap_id + ind
        #snake~ in #ind object
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~ object
        outlet_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #connexions
        """
        #loadbang to float
        bf.appendXConnect(f, loadbang_id, 0, float_id, 0)
        """
        #inlet~ to all vbap abstrations
        for j in range(ind):
            bf.appendXConnect(f, in_id, 0, multivbap_id+j, 0)
        #inlets to vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, multiinlet_id+j, 0, multivbap_id+j, 1)
            if (j > 0):
                bf.appendXConnect(f, multiinlet_id+j, 0, multivbap_id+j-1, 2)
        bf.appendXConnect(f, multiinlet_id, 0, multivbap_id+ind-1, 2)
        #float to vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, in_ang_id, 0, multivbap_id+j, 3)
        #vbap abstractions to +~ objects
        for j in range(ind):
            bf.appendXConnect(f, multivbap_id+j, 0, multiplus_id+j, 1)
            if (j < ind-1):
                bf.appendXConnect(f, multivbap_id+j, 1, multiplus_id+j+1, 0)
        bf.appendXConnect(f, multivbap_id+ind-1, 1, multiplus_id, 0)
        #+~ to snake~ in #ind object
        for j in range(ind):
            bf.appendXConnect(f, multiplus_id+j, 0, snakein_id, j)
        #snake~ in #ind object to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()
        
        
"""
_______________________________________________________
Generates the hoa.stereodecoder#ind abstractions
_______________________________________________________
"""   
def generate_hoastereodecoder(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.stereodecoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.stereodecoder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' ambisonic\ stereo\ decoder\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #bf.appendXText(f, 2.5, 1, 'amp+value message')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #03/01/2026 - remove the amplitude control from the stereodecoder
        #inlet for the message amp+value
        #in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - mc.decoderblock1#ind
        hoadb_id = bf.appendXObj(f, 0, 1.5, 'hoa.decoderblock'+str(ind))
        #line 2 - hoa.2dprojection#ind
        hoa2dproj_id = bf.appendXObj(f, 0, 2, 'hoa.2dprojection'+str(ind))
        #line 3 - outlet~~
        out_id = bf.appendXObj(f, 0, 3, 'outlet~')
        #connections
        #inlet~ to hoa.decoderblock#ind
        bf.appendXConnect(f, in1_id, 0, hoadb_id, 0)
        #hoa.decoderblock#ind to hoa.2dprojection#ind
        bf.appendXConnect(f, hoadb_id, 0, hoa2dproj_id, 0)
        #hoa.2dprojection#ind to outlet~~
        bf.appendXConnect(f, hoa2dproj_id, 0, out_id, 0)
        #
        #
        f.close()
        
        

        
        
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
        


"""
_______________________________________________________
Generates the hoa.scope#ind abstractions
_______________________________________________________
"""   
def generate_hoascope(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the hoa.scope#ind.pd abstraction
        fileName = dDir+'/hoa.scope'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.scope#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.scope'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' hoa\ scope\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #the scope in the canvas
        scope_id = bf.appendXObj(f, 0.29, 1.45, 'else/scope~ 128 128 64 3 32 -1 1 0 0 0 0 30 30 30 190 190 190 160 160 160 0 empty;')
        #line 0.5 - else/initmess 64 32
        init_id = bf.appendXObj(f, 1, 0.5, 'else/initmess 64 32')
        #line 1 - list box
        listBox_id = bf.appendXListBox(f, '125 125 10 0 0 0 - - - 10')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 2, 1, 'inlet~')
        #line 1 - loadbang
        loadbang_id = bf.appendXObj(f, 5, 1, 'loadbang')
        #line 1.25 - snake~ out
        snakeout_id = bf.appendXObj(f, 2, 1.25, 'snake~ out '+str(2*ind+1))
        #line 1.25 - msg 1
        #msg1_id = bf.appendXMsg(f, 4, 1.25, '1')
        #line 1.25 - msg 25
        msg25_id = bf.appendXMsg(f, 5, 1.25, '25')
        #line 1.5 - *~ 0.5
        mult0_id = bf.appendXObj(f, 2, 1.5, '*~ 0.5')
        #line 1.5 - float
        flo_id = bf.appendXFloat(f, 5, 1.5, '5 0 0 0 - - - 0')
        #line 1.75 - snake~ in
        snakein_id = bf.appendXObj(f, 2, 1.75, 'snake~ in '+str(2*ind+1))
        #line 1.75 - phasor~~
        phasor_id = bf.appendXObj(f, 5, 1.75, 'phasor~')
        #line 1.75 - sig~~
        sig_id = bf.appendXObj(f, 3, 1.75, 'sig~ 1')
        #line 2.75 - hoa.encodingmodule
        encomod_id = bf.appendXObj(f, 3, 2.75, 'hoa.encodingmodule'+str(ind))
        #line 2.75 - expr~~
        expr_id = bf.appendXObj(f, 4.5, 2.75, 'expr~ 0.75 - $v1')
        #line 3. - mc.normalize 1 and 2
        norm1_id = bf.appendXObj(f, 2, 3, 'mc.normalize'+str(2*ind+1))
        norm2_id = bf.appendXObj(f, 3, 3, 'mc.normalize'+str(2*ind+1))
        #line 3. - cos~ 1 and 2
        cos1_id = bf.appendXObj(f, 4.5, 3, 'cos~')
        cos2_id = bf.appendXObj(f, 5.5, 3, 'cos~')
        #line 4 - mc.sp
        sp_id = bf.appendXObj(f, 2, 4, 'mc.sp'+str(2*ind+1))
        #line 4.25 - abs~
        abs_id = bf.appendXObj(f, 2, 4.25, 'abs~')
        #line 4.5 - mult1 and mult2
        mult1_id = bf.appendXObj(f, 1.5, 4.5, '*~')
        mult2_id = bf.appendXObj(f, 2.5, 4.5, '*~')
        
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        
        #connections
        #else/initmess to listbox
        bf.appendXConnect(f, init_id, 0, listBox_id, 0)
        #listbox to scope
        bf.appendXConnect(f, listBox_id, 0, scope_id, 0)
        #inlet~ to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #outlet 0 of snake~ out to *~ 0.5
        bf.appendXConnect(f, snakeout_id, 0, mult0_id, 0)
        #outlet of *~ 0.5 to inlet 0 of snake~ in
        bf.appendXConnect(f, mult0_id, 0, snakein_id, 0)
        #connections of all other outlets of snake~ out to the corresponding outlets of snake~ in
        for j in range(2*ind):
            bf.appendXConnect(f, snakeout_id, j+1, snakein_id, j+1)
        #snake~ in to mc.normalize
        bf.appendXConnect(f, snakein_id, 0, norm1_id, 0)
        #mc.normalize 1 to inlet 0 of mc.sp
        bf.appendXConnect(f, norm1_id, 0, sp_id, 0)
        #mc.normalize 2 to inlet 1 of mc.sp
        bf.appendXConnect(f, norm2_id, 0, sp_id, 1)
        #mc.sp to abs~~
        bf.appendXConnect(f, sp_id, 0, abs_id, 0)
        #abs~ to mult1 and mult2
        bf.appendXConnect(f, abs_id, 0, mult1_id, 0)
        bf.appendXConnect(f, abs_id, 0, mult2_id, 0)
        #loadbang to msg 25
        bf.appendXConnect(f, loadbang_id, 0, msg25_id, 0)
        #msg25 to Float
        bf.appendXConnect(f, msg25_id, 0, flo_id, 0)
        #Float to phasor~
        bf.appendXConnect(f, flo_id, 0, phasor_id, 0)
        #phasor to inlet 1 of hoa.encodingmodule#ind
        bf.appendXConnect(f, phasor_id, 0, encomod_id, 1)
        #phasor~ to expr~~
        bf.appendXConnect(f, phasor_id, 0, expr_id, 0)
        #phasor~ to cos~ 2
        bf.appendXConnect(f, phasor_id, 0, cos2_id, 0)
        #expr~ to cos~ 1
        bf.appendXConnect(f, expr_id, 0, cos1_id, 0)
        #cos~ 1 to the inlet 1 of mult 1
        bf.appendXConnect(f, cos1_id, 0, mult1_id, 1)
        #cos~ 2 to the inlet 1 of mult 2
        bf.appendXConnect(f, cos2_id, 0, mult2_id, 1)        
        #sig~ to encodingmodule
        bf.appendXConnect(f, sig_id, 0, encomod_id, 0)
        #encodingmodule to mc.normalize 2
        bf.appendXConnect(f, encomod_id, 0, norm2_id, 0)
        #mult1 to inlet 0 of scope
        bf.appendXConnect(f, mult1_id, 0, scope_id, 0)
        #mult2 to inlet 1 of scope
        bf.appendXConnect(f, mult2_id, 0, scope_id, 1)        
        

        f.write('#X coords 0 -1 1 1 135 150 1 50 150;\n')
    
        f.close()
        
