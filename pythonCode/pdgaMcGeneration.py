#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.gain#ind abstractions
_______________________________________________________
"""   
def generate_mcgain(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.gain'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.gain'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ gain\ on\ '+str(ind)+'\ signals\ in\ dB '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        bf.appendXText(f, 2.5, 1, 'message amp followed by the level in dB')
        #line 1 - inlet~
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #inlet for the message amp+value
        in2_id = bf.appendXObj(f, 2, 1, 'inlet')
        #line 1.5 - snake~ out #ind
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind)+' -------------')
        #db2rms
        db2rms_id = bf.appendXObj(f, 2, 1.5, 'db2rms')
        #line 4 - snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind)+' -------------')
        #line 5 - outlet~
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #multipliers *~ (ind )
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 3, '*~')
        #comes back to the first
        mult_id = out_id + 1
        #writes the connections
        #connects the inlet~ to the snake~ out #ind
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #connects the inlet to the db2rms abstraction
        bf.appendXConnect(f, in2_id, 0, db2rms_id, 0)
        #connects the snake~ out # ind outputs to the first inputs of the different *~
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, mult_id+j, 0)
        #connects the output of db2rms to the second inputs of the different *~~
        for j in range(ind):
            bf.appendXConnect(f, db2rms_id, 0, mult_id+j, 1)
        #connects the outputs of the different *~to the inputs of snake~ in #ind
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #connects the output of snake~ in #ind
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()
        


"""
_______________________________________________________
Generates the mc.duplicate#ind abstractions
_______________________________________________________
"""   
def generate_mcduplicate(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busplus#ind.pd abstraction
        fileName = dDir+'/mc.duplicate'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.duplicate#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.duplicate'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' creates\ '+str(ind)+'\ copies\ of\ the\ input\ channel '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        
        #inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 2, 'snake~ in '+str(ind))
        #outlet~
        outlet_id = bf.appendXObj(f, 0, 3, 'outlet~ ')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ to snake~ in #ind multiple connections
        for j in range(ind):
            bf.appendXConnect(f, in_id, 0, snakein_id, j)
        #snake~ in #ind to outlet~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()
        
        
"""
_______________________________________________________
Generates the mc.meter#ind abstractions
_______________________________________________________
"""   
def generate_mcmeter(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.meter#ind.pd abstraction
        fileName = dDir+'/mc.meter'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.meter#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'mc.meter#ind.pd')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #line 1.5 - snake~ out
        snakeout_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind)+' ----------')
        #line 2 - multiple env~ to measure each channel
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 2, 'env~')
        #comes back to the first one
        env_id = snakeout_id + 1
        #line 2.5 - series of [- 100]
        for j in range(ind):
            k = bf.appendXObj(f, j*0.5, 2.5, '- 100')
        #comes back to the first one
        minus100_id = snakeout_id + ind + 1
        #the ind-1 normal vumeter (without graduation)   
        for j in range(ind-1):
            k = bf.appendXObj(f, j*0.16 + 0.3, 3.49, 'vu 10 120 empty empty -1 -8 0 10 #404040 #000000 0 0')
        #the last one with the graduation
        k = bf.appendXObj(f, (ind-1)*0.16 + 0.3, 3.49, 'vu 10 120 empty empty -1 -8 0 10 #404040 #000000 1 0')
        #comes back to the first one
        vu_id = minus100_id +  ind
           
        #connections
        #inlet to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #[snake~ out] to the various [env~]
        #and the [env~] to the [- 100]
        #and the [- 100] to the vumeter
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, env_id + j, 0)
            bf.appendXConnect(f, env_id+j, 0, minus100_id+j, 0)
            bf.appendXConnect(f, minus100_id+j, 0, vu_id+j, 0)

        f.write('#X coords 0 -1 1 1 '+str(42+ind*15)+' 145 1 50 355;\n')
        
        f.close()
        
    
        
"""
_______________________________________________________
Generates the mc.sp#ind abstractions
_______________________________________________________
"""     
def generate_mcsp(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.sp#ind.pd abstraction
        fileName = dDir+'/mc.sp'+str(ind)+".pd"
        f = open(fileName, 'w')
        #
        #writes the lines of the mc.sp#ind.pd Pure Data abstraction
        #writes the objects
        bf.createMiddleCommonAbstraction(f)
        #line 0 - comment
        bf.appendXText(f, 0, 0, bf.commonComment+'mc.sp#ind.pd')
        #line 1
        in1_id = bf.appendXObj(f, 0, 1, 'inlet~')
        in2_id = bf.appendXObj(f, 1, 1, 'inlet~')
        #line 5
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #line 1.5
        snake1_id = bf.appendXObj(f, 0, 1.5, 'snake~ out '+str(ind))
        snake2_id = bf.appendXObj(f, 1, 1.5, 'snake~ out '+str(ind))
        #writes the *~ on the line 3
        for j in range(ind):
            #the ids of the *~ are between 7 and 7+ind-1
            k = bf.appendXObj(f, j*0.5, 3, '*~')
        #comes back to the first one
        mult_id = snake2_id + 1
        #writes the connections
        #connects the inlets to the snake~ out
        bf.appendXConnect(f, in1_id, 0, snake1_id, 0)
        bf.appendXConnect(f, in2_id, 0, snake2_id, 0)
        #connects the snake~ out to the *~~
        #connects the *~ to the outlet~
        for j in range(ind):
            bf.appendXConnect(f, snake1_id, j, mult_id+j, 0)
            bf.appendXConnect(f, snake2_id, j, mult_id+j, 1)
            bf.appendXConnect(f, mult_id+j, 0, out_id, 0)
        f.close()
        
        

"""
_______________________________________________________
Generates the mc.busmult#ind abstractions
_______________________________________________________
"""   
def generate_mcbusmult(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busplus#ind.pd abstraction
        fileName = dDir+'/mc.busmult'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.busmult#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.busmult'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ bus\ multiplication\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        
        #inlet~ 1
        in1_id = bf.appendXObj(f, 0, 1.5, 'inlet~')
        #inlet~ 2
        in2_id = bf.appendXObj(f, 2, 1.5, 'inlet~')
        #snake~ out #ind 1
        snakeout1_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(ind))
        #snake~ out #ind 2
        snakeout2_id = bf.appendXObj(f, 2, 2, 'snake~ out '+str(ind))
        #*~ objects
        for j in range(ind):
            k = bf.appendXObj(f, j, 3, '*~')
        #comes back to the first one
        multimult_id = snakeout2_id + 1
        #snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~
        outlet_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ 1 to snake~ out 1
        bf.appendXConnect(f, in1_id, 0, snakeout1_id, 0)
        #inlet~ 2 to snake~ out 2
        bf.appendXConnect(f, in2_id, 0, snakeout2_id, 0)
        #snake~ out 1 to left inlets of *~
        #snake~ out 2 to right inlets of *~
        for j in range(ind):
            bf.appendXConnect(f, snakeout1_id, j, multimult_id+j, 0)
            bf.appendXConnect(f, snakeout2_id, j, multimult_id+j, 1)
        #+~ to snake~ in object
        for j in range(ind):
            bf.appendXConnect(f, multimult_id+j, 0, snakein_id, j)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()
        
        

"""
_______________________________________________________
Generates the mc.busplus#ind abstractions
_______________________________________________________
"""   
def generate_mcbusplus(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.busplus#ind.pd abstraction
        fileName = dDir+'/mc.busplus'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.busplus#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.busplus'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ bus\ addition\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        
        #inlet~ 1
        in1_id = bf.appendXObj(f, 0, 1.5, 'inlet~')
        #inlet~ 2
        in2_id = bf.appendXObj(f, 2, 1.5, 'inlet~')
        #snake~ out #ind 1
        snakeout1_id = bf.appendXObj(f, 0, 2, 'snake~ out '+str(ind))
        #snake~ out #ind 2
        snakeout2_id = bf.appendXObj(f, 2, 2, 'snake~ out '+str(ind))
        #+~ objects
        for j in range(ind):
            k = bf.appendXObj(f, j, 3, '+~')
        #comes back to the first one
        multiplus_id = snakeout2_id + 1
        #snake~ in #ind
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~
        outlet_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet~ 1 to snake~ out 1
        bf.appendXConnect(f, in1_id, 0, snakeout1_id, 0)
        #inlet~ 2 to snake~ out 2
        bf.appendXConnect(f, in2_id, 0, snakeout2_id, 0)
        #snake~ out 1 to left inlets of +~
        #snake~ out 2 to right inlets of +~
        for j in range(ind):
            bf.appendXConnect(f, snakeout1_id, j, multiplus_id+j, 0)
            bf.appendXConnect(f, snakeout2_id, j, multiplus_id+j, 1)
        #+~ to snake~ in object
        for j in range(ind):
            bf.appendXConnect(f, multiplus_id+j, 0, snakein_id, j)
        #snake~ in to outlet~~
        bf.appendXConnect(f, snakein_id, 0, outlet_id, 0)
        f.close()
        
        

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
        
        
        
"""
_______________________________________________________
Generates the mc.player#ind abstractions
_______________________________________________________
"""   
def generate_mcplayer(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.player#ind.pd abstraction
        fileName = dDir+'/mc.player'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.player#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.player'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ player\ on\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #bang in the canvas to open the file
        bngopen_id = bf.appendXObj(f, 0.8, 1.46, 'bng 15 250 50 0 empty empty open 17 7 0 10 #0c4044 #000000 #000000')
        #toggle in the canvas to play
        tglplay_id = bf.appendXObj(f, 1.27, 1.46, 'tgl 15 0 empty empty play 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        #toggle for loop/no loop selection
        tglloop_id = bf.appendXObj(f, 1.8, 1.46, 'tgl 15 0 empty empty loop 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        #horizontal slider to set the volume
        hslvol_id = bf.appendXObj(f, 2.35, 1.46, 'hsl 80 15 0 1 0 0 empty empty vol -2 -8 0 10 #fcfcfc #000000 #000000 0 1')
        #inlet for control messages of the player
        in_id = bf.appendXObj(f, 2.5, 0.5, 'inlet')
        #route object
        route_id = bf.appendXObj(f, 2.5, 0.8, 'route vol play loop')
        #openpanel object
        openpanel_id = bf.appendXObj(f, 2.5, 2, 'openpanel')
        #list prepend
        list1_id = bf.appendXObj(f, 2.5, 2.25, 'list prepend set open')
        #list trim
        list2_id = bf.appendXObj(f, 2.5, 2.5, 'list trim')
        #open message
        msgopen_id = bf.appendXMsg(f, 2.5, 2.75, 'open')
        #readsf~ #ind object
        readsf_id = bf.appendXObj(f, 2.5, 3.25, 'readsf~ '+str(ind))
        #bang object
        bang_id = bf.appendXObj(f, 3.5, 3.75, 'bang')
        #float object
        float_id = bf.appendXObj(f, 3.5, 4, 'f 0')
        #various *~ (#ind instances)
        for j in range(ind):
            k = bf.appendXObj(f, 2.5+0.5*j, 4.5, '*~')
        #comes back to the first one
        mult_id = float_id + 1
        #snake~ in #ind object
        snakein_id = bf.appendXObj(f, 2.5, 4.75, 'snake~ in '+str(ind))
        #outlet~ object
        out_id = bf.appendXObj(f, 2.5, 5, 'outlet~')
        #level msg
        msglevel_id = bf.appendXMsg(f, 2.5+0.5*ind, 3.75, '\$1 20')
        #line~ object
        line_id = bf.appendXObj(f, 2.5+0.5*ind, 4, 'line~')
        #trigger object
        trig_id = bf.appendXObj(f, 2, 2.25, 't f b')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to route
        bf.appendXConnect(f, in_id, 0, route_id, 0)
        #vol in route to hsl vol
        bf.appendXConnect(f, route_id, 0, hslvol_id, 0)
        #play in route to play toogle
        bf.appendXConnect(f, route_id, 1, tglplay_id, 0)
        #loop in route to loop toggle
        bf.appendXConnect(f, route_id, 2, tglloop_id, 0)
        #open bang to openpanel object
        bf.appendXConnect(f, bngopen_id, 0, openpanel_id, 0)
        #play toggle to trigger object
        bf.appendXConnect(f, tglplay_id, 0, trig_id, 0)
        #trigger object to readsf~ #ind
        bf.appendXConnect(f, trig_id, 0, readsf_id, 0)
        #trigger object to open message
        bf.appendXConnect(f, trig_id, 1, msgopen_id, 0)
        #openpanel object to list prepend object
        bf.appendXConnect(f, openpanel_id, 0, list1_id, 0)
        #list prepend object to list trim object
        bf.appendXConnect(f, list1_id, 0, list2_id, 0)
        #list trim to message open
        bf.appendXConnect(f, list2_id, 0, msgopen_id, 0)
        #message open to readsf object
        bf.appendXConnect(f, msgopen_id, 0, readsf_id, 0)
        #last output of readsf~ to bang object
        bf.appendXConnect(f, readsf_id, ind, bang_id, 0)
        #bang object to float object
        bf.appendXConnect(f, bang_id, 0, float_id, 0)
        #loop toggle to float object
        bf.appendXConnect(f, tglloop_id, 0, float_id, 1)
        #float object to play toggle
        bf.appendXConnect(f, float_id, 0, tglplay_id, 0)
        #hsl vol to level msg
        bf.appendXConnect(f, hslvol_id, 0, msglevel_id, 0)
        #level msg to line~ object
        bf.appendXConnect(f, msglevel_id, 0, line_id, 0)
        #connections between readsf~ object to the various *~~
        for j in range(ind):
            bf.appendXConnect(f, readsf_id, j, mult_id+j, 0)
        #connections between line~ object to the various *~
        for j in range(ind):
            bf.appendXConnect(f, line_id, 0, mult_id+j, 1)
        #connections between the various *~ and snake~ in #ind object
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #snake~ in #ind object to outlet~ object
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.write('#X coords 0 -1 1 1 250 40 1 100 150;\n')
        f.close()
        
        
        
"""
_______________________________________________________
Generates the mc.recorder#ind abstractions
_______________________________________________________
"""   
def generate_mcrecorder(dDir):
    for i in range (2*bf.maxAmbiOrder+2):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/mc.recorder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.recorder#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.recorder'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ recorder\ of\ '+str(ind)+'\ channels '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #bang in the canvas to open a file
        bng_id = bf.appendXObj(f, 0.8, 0.96, 'bng 15 250 50 0 empty empty open 17 7 0 10 #0c4044 #000000 #000000')
        #toggle in the canvas to start recording
        tgl_id = bf.appendXObj(f, 1.27, 0.96, 'tgl 15 0 empty empty record 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #recordercontrol abstraction
        recoctrl_id = bf.appendXObj(f, 0.5, 1.5, 'recordercontrol')
        #inlet~~
        in1_id = bf.appendXObj(f, 2, 1.5, 'inlet~')
        #snake~ out #ind
        snakeout_id = bf.appendXObj(f, 2, 2, 'snake~ out '+str(ind))
        #writesf~ #ind
        w_id = bf.appendXObj(f, 0.5, 3, 'writesf~ '+str(ind))
        #adds the canvas
        f.write('#X coords 0 -1 1 1 110 40 1 100 100;\n')
        #connections
        #open bang to left input of recordercontrol abstraction
        bf.appendXConnect(f, bng_id, 0, recoctrl_id, 0)
        #write toggle to right input of recordercontrol abstraction
        bf.appendXConnect(f, tgl_id, 0, recoctrl_id, 1)
        #inlet~ to snake~ out #ind
        bf.appendXConnect(f, in1_id, 0, snakeout_id, 0)
        #recodercontrol to input 0 of writesf~~
        bf.appendXConnect(f, recoctrl_id, 0, w_id, 0)
        #connections to the various outputs of snake~ out #ind to the inputs of writesf~ #ind
        for j in range(ind):
            bf.appendXConnect(f, snakeout_id, j, w_id, j)
        f.close()
        
        
        
"""
_______________________________________________________
Generates the mc.zeropadding#ind abstractions
_______________________________________________________
"""   
def generate_mczeropad(dDir):
    for i in range (4, 2*bf.maxAmbiOrder+2+1):
        ind = i
        #opens a Pure Data file for the mc.stereozeropad#ind.pd abstraction
        fileName = dDir+'/mc.stereozeropad'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.stereozeropad#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.stereozeropad'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' completes\ stereo\ with\ '+str(ind-2)+'\ zeros '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        #
        #inlet~ for the stereo initial flow
        in_id = bf.appendXObj(f, 0, 1, 'inlet~')
        #snake~ out 2 object to decompose the 2 channels
        snakeout_id = bf.appendXObj(f, 0, 2, 'snake~ out 2')
        #snake~ in ind object for the final result
        snakein_id = bf.appendXObj(f, 0, 4, 'snake~ in '+str(ind))
        #outlet~ for the output
        out_id = bf.appendXObj(f, 0, 5, 'outlet~')
        #sig~ 0 for the zero padding
        sig0_id = bf.appendXObj(f, 1, 2, 'sig~ 0')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out two channels to snake~ in first two channels
        bf.appendXConnect(f, snakeout_id, 0, snakein_id, 0)
        bf.appendXConnect(f, snakeout_id, 1, snakein_id, 1)
        #sig~ 0 to all the other inputs of snake~ in #ind
        for j in range(2, ind):
            bf.appendXConnect(f, sig0_id, 0, snakein_id, j)
        #snake~ in #ind to outlet~~
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        f.close()
        
        
        
"""
_______________________________________________________
Generates the mc.vbap#ind abstractions
_______________________________________________________
"""   
def generate_mcvbap(dDir):
    #one source is spatialized on ind2 loudspeakers using vbap
    for i in range(2*bf.maxAmbiOrder+1):
        #ind is the number of loudspeakers, from 2 to 2*maxAmbiOrder+2
        ind = i +2
        #opens a Pure Data file for hoa.vbap#ind.pd abstraction
        fileName = dDir+'/mc.vbap'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.vbap#ind.pd Pure Data abstraction
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' mc.vbap'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' multichannel\ vbap\ of\ one\ source\ on\ '+str(ind)+'\ loudspeakers '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()
        #
        #line 0.5 - inlet~
        in1_id = bf.appendXObj(f, 0, 0.5, 'inlet~')
        #line 0.5 - inlet for the angles of the loudspeakers
        in2_id = bf.appendXObj(f, 3, 0.5, 'inlet')
        #line 0.5 - inlet for the angle of the source
        in3_id = bf.appendXObj(f, 7, 0.5, 'inlet')
        #line 0.75 - route
        route_content = 'route'
        for j in range(ind):
            route_content = route_content + ' a' + str(j)
        #we add direct $1 (1 or 0) message
        #we add shift $1 (angle in degrees) message
        route_content = route_content+' direct'
        route_content = route_content+' shift'
        route_id = bf.appendXObj(f, 3, 0.75, route_content)
        #we add the anglecontrol abstraction to transform the angle of the source
        #according to the global parameters (direct and shift)
        ang_ctrl_id = bf.appendXObj(f, 7, 1, 'anglecontrol')
        #vbap elementary modules for each loudspeaker
        for j in range(ind):
            k = bf.appendXObj(f, j, 1.75, 'vbap'+str(ind))
        #comes back to the first
        multivbap_id = ang_ctrl_id +  1
        #mc.busplus#ind abstractions
        for j in range(ind-1):
            k = bf.appendXObj(f, j*0.5, 2+0.25*j, 'mc.busplus'+str(ind))
        #comes back to the first
        multibusplus_id = multivbap_id + ind
        #
        #outlet~~
        out_id = bf.appendXObj(f, 0.5*(ind-2), 2+0.25*(ind-1), 'outlet~')
        #connection of the first two vbap abstractions to the 
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to route
        bf.appendXConnect(f, in2_id, 0, route_id, 0)
        #inlet 3 connected to anglecontrol
        bf.appendXConnect(f, in3_id, 0, ang_ctrl_id, 0)
        #the source is connected to all the first inputs of the vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, in1_id, 0, multivbap_id+j, 0)
        #the outputs of the route object are connected to all the inputs (#1 to #ind2) of the vbap abstractions
        for j in range(ind):
            for k in range(ind):
                bf.appendXConnect(f, route_id, j, multivbap_id+k, j+1)
        #the anglecontrol abstraction (angle of the source recomputed) is connected to all the last inputs of the vbap abstractions
        for j in range(ind):
            bf.appendXConnect(f, ang_ctrl_id, 0, multivbap_id+j, ind + 1)
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
        #connection of the direct and shift outputs of the route to the inputs of anglecontrol
        bf.appendXConnect(f, route_id, ind, ang_ctrl_id, 1)
        bf.appendXConnect(f, route_id, ind+1, ang_ctrl_id, 2)
        #
        f.close()
        