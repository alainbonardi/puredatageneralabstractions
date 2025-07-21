# -*- coding: utf-8 -*-

import os
import shutil
import pdga_generate_mcsp.py as gsp
import pdga_basicFunctions.py as bf
import tkinter as tkinter
from tkinter import filedialog

#origLibDir = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions'
#destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_abstractions'

"""
_______________________________________________________
Global constants and variables for Pure Data patches
_______________________________________________________
"""

#
#global variables
#index of current object processed
objInd = 0
#flags to run or not such or such generation
mcsp_flag = True
mccstencoder_flag = True
mcdecoderblock_flag = True




    
"""
_______________________________________________________
Generates the mc.cstencoder#ind abstractions
_______________________________________________________
"""   
def generate_mccstencoder():
    for i in range (maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.cstencoder#ind.pd abstraction
        fileName = destLibDir+'/mc.cstencoder'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.cstencoder#ind.pd Pure Data abstraction
        #writes the objects
        createMiddleCommonAbstraction(f)
        #line 0 - comment
        appendXText(f, 0, 0, commonComment+'mc.cstencoder#ind.pd')
        #line 1
        #loadbang
        loadbang_id = appendXObj(f, 0, 1, 'loadbang')
        #line 1.5
        #msg
        msg_id = appendXMsg(f, 0, 1.5, str(ind))
        #float
        float_id = appendXObj(f, 1, 1.5, 'float \$1')
        #line 1.75
        #float box
        floatbox_id = appendXFloat(f, 1, 1.75, '0 ')
        #line 2
        cstforencoder_id = appendXObj(f, 0, 2, 'cstforencoder')
        #line 4.5
        #snake~ in
        snake_id = appendXObj(f, 0, 4.5, 'snake~ in '+str(2*ind+1)+' ----------')
        #line 5
        #outlet~~
        out_id = appendXObj(f, 0, 5, 'outlet~')
        #line 3
        #sinandcos abstractions
        for j in range(ind):
            ind2 = j + 1
            k = appendXObj(f, ind2, 3, 'sinandcos '+str(ind2))
            #ids from 9 to 9+ind-1
        #comes back to the first one
        sinandcos_id = out_id + 1
        #line 4
        #*~
        for j in range(2*ind):
            ind2 = j + 1
            ind3 = 0.5 * ind2
            k = appendXObj(f, ind3, 4, '*~')
            #ids from 9+ind to 9+3*ind-1
        #comes back to the first one
        mult_id = sinandcos_id + ind
        #connections
        #loadbang to message
        appendXConnect(f, loadbang_id, 0, msg_id, 0)
        #loadbang to float object
        appendXConnect(f, loadbang_id, 0, float_id, 0)
        #float object to float box
        appendXConnect(f, float_id, 0, floatbox_id, 0)
        #message to cstforencoder
        appendXConnect(f, msg_id, 0, cstforencoder_id, 0)
        #float box to cstforencoder
        appendXConnect(f, floatbox_id, 0, cstforencoder_id, 1)
        #cstforencoder to sinandcos abstractions
        for j in range(ind):
            appendXConnect(f, cstforencoder_id, 1, sinandcos_id+j, 0)
        #cstforencoder to *~
        for j in range(2*ind):
            appendXConnect(f, cstforencoder_id, 0, mult_id+j, 0)
        #cstforencoder to input 0 of snake~ in
        appendXConnect(f, cstforencoder_id, 0, snake_id, 0)
        #sinandcos to *~~
        for j in range(ind):
            appendXConnect(f, sinandcos_id+j, 0, mult_id+2*j, 1)
            appendXConnect(f, sinandcos_id+j, 1, mult_id+2*j+1, 1)
        #*~ to snake~ in
        for j in range(2*ind):
            appendXConnect(f, mult_id+j, 0, snake_id, j+1)
        #snake~ in to outlet~~
        appendXConnect(f, snake_id, 0, out_id, 0)
        f.close()
        
"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def generate_mcdecoderblock():
    for i in range (maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.decoderblock#ind.pd abstraction
        fileName = destLibDir+'/mc.decoderblock'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
        #writes the objects
        createMiddleCommonAbstraction(f)
        #line 0 - comment
        appendXText(f, 0, 0, commonComment+'mc.decoderblock#ind.pd')
        #line 1
        #inlet~
        in_id = appendXObj(f, 0, 1, 'inlet~')
        #line 1.5
        #snake~ out
        snakeout_id = appendXObj(f, 0, 1.5, 'snake~ out '+str(2*ind+1))
        #line 2
        #*~0.5
        mult_id = appendXObj(f, 0, 2, '*~ 0.5')
        #line 2.5
        #snake~ in
        snakein1_id = appendXObj(f, 0, 2.5, 'snake~ in '+str(2*ind+1))
        #line 4
        #snake~ in
        snakein2_id = appendXObj(f, 0.5*ind, 4, 'snake~ in '+str(2*ind+2))
        #line 4.5
        #outlet~~
        out_id = appendXObj(f, 0.5*ind, 4.5, 'outlet~')
        #line 2
        #mc.cstencoder#ind
        for j in range(2*ind+2):
            ind2 = j + 1
            k = appendXObj(f, ind2, 2, 'mc.cstencoder'+str(ind)+' '+str(j))
        #comes back to the first one
        cstencoder_id = out_id + 1
        #cstencoder_id between 8 and 8+2*ind+1
        #line 3
        #mc.sp#2*ind+1
        for j in range(2*ind+2):
            ind2 = j + 1
            k = appendXObj(f, j, 3, 'mc.sp'+str(2*ind+1))
        #comes back to the first one
        sp_id = cstencoder_id+2*ind+2
        #connexions
        #inlet~ to snake~ out
        appendXConnect(f, in_id, 0, snakeout_id, 0)
        #snake~ out 0 to *~0.5
        appendXConnect(f, snakeout_id, 0, mult_id, 0)
        #*~0.5 to snake~ in 0
        appendXConnect(f, mult_id, 0, snakein1_id, 0)
        #snake~ out 1 to 2*ind to snake~ in 1 to 2*ind
        for j in range(2*ind):
            ind2 = j + 1
            appendXConnect(f, snakeout_id, ind2, snakein1_id, ind2)
        #mc.cstencoder#j to mc.sp#j inlet 1
        for j in range(2*ind+2):
            appendXConnect(f, cstencoder_id+j, 0, sp_id+j, 1)
        #snake~ in to mc.sp#j inlet 0
        for j in range(2*ind+2):
            appendXConnect(f, snakein1_id, 0, sp_id+j, 0)
        #mc.sp#j outlet 0 to snake~ in inlet j
        for j in range(2*ind+2):
            appendXConnect(f, sp_id+j, 0, snakein2_id, j)
        #snake~ in to outlet~~
        appendXConnect(f, snakein2_id, 0, out_id, 0)
        f.close()


print("________________________________________________")
print("CHOOSE A FOLDER WHERE YOU WILL INCLUDE YOUR PURE DATA GENERATED ABSTRACTIONS FOLDER")
#choose a folder
#rootPath = filedialog.askdirectory()
#destLibDir = rootPath+'/generated_pdga_abstractions'
#provisional fixed directory
destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_pdga_abstractions'
#
if os.path.exists(destLibDir):
    print("Existing directory containing the original generated abstractions, the previous one is deleted")
    shutil.rmtree(destLibDir)
#we create a new folder for the generated abstractions
os.mkdir(destLibDir)

#
print("________________________________________________")
print("GENERATING COMMON ABSTRACTIONS==================")
print("________________________________________________")
#
print("________________________________________________")
print("STEP#01 GENERATING SCALAR PRODUCT ABSTRACTIONS")
print("________________________________________________")
if (mcsp_flag):
    gsp.generate_mcsp(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.sp#ind.pd common abstractions generated')
else:
    print('=> no mc.sp#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#02 GENERATING CONSTANT ENCODERS ABSTRACTIONS")
print("________________________________________________")
if (mccstencoder_flag):
    generate_mccstencoder()
    print('=>'+str(maxAmbiOrder)+' mc.cstencoder#ind.pd common abstractions generated')
else:
    print('=> no mc.cstencoder#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#03 GENERATING DECODER BLOCK ABSTRACTIONS")
print("________________________________________________")
if (mcdecoderblock_flag):
    generate_mcdecoderblock()
    print('=>'+str(maxAmbiOrder)+' mc.decoderblock#ind.pd common abstractions generated')
else:
    print('=> no mc.decoderblock#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#04 GENERATING REGULAR DECODER ABSTRACTIONS")
print("________________________________________________")
for i in range (maxAmbiOrder):
    ind = i + 1
    #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
    fileName = destLibDir+'/mc.regdecoder'+str(ind)+".pd"
    f = open(fileName, 'w')
    #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
    #writes the objects
    f.write(patchMiddleCanvas+'\n')
    f.write(patchAbstractionCnv1_1+' mc.regdecoder'+str(ind)+' '+patchAbstractionCnv2_1+'\n')
    f.write(patchAbstractionCnv1_2+ ' multichannel\ ambisonic\ regular\ decoder\ at\ order\ '+str(ind)+'\ to\ '+str(2*ind+2)+'\ loudspeakers '+patchAbstractionCnv2_2+'\n')
    f.write(patchMiddleCredits+'\n')
    f.write(xText+str(getPx(2.5))+' '+str(getPy(1))+' amp+value message;\n')
    #line 1
    #inlet~
    f.write(xObj+str(getPx(0))+' '+str(getPy(1))+' inlet~;\n')
    in1_id = 4
    #inlet for the message amp+value
    f.write(xObj+str(getPx(2))+' '+str(getPy(1))+' inlet;\n')
    in2_id = 5
    #line 1.5
    #mc.decoderblock1#ind
    f.write(xObj+str(getPx(0))+' '+str(getPy(1.5))+' mc.decoderblock'+str(ind)+';\n')
    mcdb_id = 6
    #line 3
    #mc.gain#(2*ind+2)
    f.write(xObj+str(getPx(0))+' '+str(getPy(3))+' mc.gain'+str(2*ind+2)+';\n')
    mcga_id = 7
    #line 3.5
    #outlet~
    f.write(xObj+str(getPx(0))+' '+str(getPy(3.5))+' outlet~;\n')
    out_id = 8
    #writes the connections
    #connects the inlet~ to the mc.decoderblock#ind
    f.write(xConnect+str(in1_id)+' 0 '+str(mcdb_id)+' 0;\n')
    #connects the mc.decoderblock#ind to the mc.gain#(2*ind+2)
    f.write(xConnect+str(mcdb_id)+' 0 '+str(mcga_id)+' 0;\n')
    #connects the mc.gain#(2*ind+2) to the outlet~~
    f.write(xConnect+str(mcga_id)+' 0 '+str(out_id)+' 0;\n')
    #connects the inlet to the right input of the mc.gain#(2*ind+2)
    f.write(xConnect+str(in2_id)+' 0 '+str(mcga_id)+' 1;\n')
    #
    f.close()
print('=>'+str(maxAmbiOrder)+' mc.regdecoder#ind.pd common abstractions generated')