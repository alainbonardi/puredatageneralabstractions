# -*- coding: utf-8 -*-

import os
import shutil
import tkinter as tkinter
from tkinter import filedialog

#origLibDir = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions'
#destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_abstractions'

"""
_______________________________________________________
Constants for Pure Data patches
_______________________________________________________
"""
leftMargin = 25
topMargin = 25
dx = 100
dy = 100
maxAmbiOrder = 7
patchMiddleCanvas = '#N canvas 50 50 600 600 10;'
patchMiddleCredits = '#X obj 10 550 pdga_helpcredit;'
patchAbstractionCnv1_1 = '#X obj 15 6 cnv 15 550 25 empty empty'
patchAbstractionCnv1_2 = '#X obj 15 32 cnv 15 550 25 empty empty'
patchAbstractionCnv2_1 = '20 12 0 18 #606060 #fcfcfc 0;'
patchAbstractionCnv2_2 = '20 12 0 12 #606060 #fcfcfc 0;'
commonComment = ' Common abstractions generated - '
xObj = '#X obj '
xText = '#X text '
xConnect = '#X connect '
xMsg = '#X msg '
xFloat = '#X floatatom '
xFloat2 = '5 0 0 0 - - - 0;\n'

def getPx(ix):
    px = leftMargin + ix * dx
    return int(px)

def getPy(iy):
    py = topMargin + iy * dy
    return int(py)

print("________________________________________________")
print("CHOOSE A FOLDER WHERE YOU WILL INCLUDE YOUR PURE DATA GENERATED ABSTRACTIONS FOLDER")
#choose a folder
#rootPath = filedialog.askdirectory()
#destLibDir = rootPath+'/generated_pdga_abstractions'
destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_pdga_abstractions'
#
if os.path.exists(destLibDir):
    print("Existing directory containing the original generated abstractions, the previous one is deleted")
    shutil.rmtree(destLibDir)
#we create a new folder for the generated abstractions
os.mkdir(destLibDir)

#
print("________________________________________________")
print("STEP#01 GENERATING SCALAR PRODUCT ABSTRACTIONS")
print("________________________________________________")
for i in range (2*maxAmbiOrder+1):
    ind = i + 1
    #opens a Pure Data file for the mc.sp#ind.pd abstraction
    fileName = destLibDir+'/mc.sp'+str(ind)+".pd"
    f = open(fileName, 'w')
    #writes the lines of the mc.sp#ind.pd Pure Data abstraction
    #writes the objects
    f.write(patchMiddleCanvas+'\n')
    f.write(patchMiddleCredits+'\n')
    #line 0 - comment
    f.write(xText+str(getPx(0))+' '+str(getPy(0))+commonComment+'mc.sp#ind.pd;\n')
    #line 1
    f.write(xObj+str(getPx(0))+' '+str(getPy(1))+' inlet~;\n')
    in1_id = 2
    f.write(xObj+str(getPx(1))+' '+str(getPy(1))+' inlet~;\n')
    in2_id = 3
    #line 5
    f.write(xObj+str(getPx(0))+' '+str(getPy(5))+' outlet~;\n')
    out_id = 4
    #line 2
    f.write(xObj+str(getPx(0))+' '+str(getPy(2))+' snake~ out '+str(ind)+';\n')
    snake1_id = 5
    f.write(xObj+str(getPx(1))+' '+str(getPy(2))+' snake~ out '+str(ind)+';\n')
    snake2_id = 6
    #writes the *~ on the line 4
    for j in range(ind):
        #the ids of the *~ are between 7 and 7+ind-1
        f.write(xObj+str(getPx(j))+' '+str(getPy(4))+' *~;\n')
    mult_id = 7
    #writes the connections
    #connects the inlets to the snake~ out
    f.write(xConnect+str(in1_id)+' 0 '+str(snake1_id)+' 0;\n')
    f.write(xConnect+str(in2_id)+' 0 '+str(snake2_id)+' 0;\n')
    #connects the snake~ out to the *~~
    #connects the *~ to the outlet~
    for j in range(ind):
        f.write(xConnect+str(snake1_id)+' '+str(j)+' '+str(mult_id+j)+' 0;\n')
        f.write(xConnect+str(snake2_id)+' '+str(j)+' '+str(mult_id+j)+' 1;\n')
        f.write(xConnect+str(mult_id+j)+' 0 '+str(out_id)+' 0;\n')
    f.close()
print('=>'+str(2*maxAmbiOrder+1)+' mc.sp#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#02 GENERATING CONSTANT ENCODERS ABSTRACTIONS")
print("________________________________________________")
for i in range (maxAmbiOrder):
    ind = i + 1
    #opens a Pure Data file for the mc.cstencoder#ind.pd abstraction
    fileName = destLibDir+'/mc.cstencoder'+str(ind)+".pd"
    f = open(fileName, 'w')
    #writes the lines of the mc.cstencoder#ind.pd Pure Data abstraction
    #writes the objects
    f.write(patchMiddleCanvas+'\n')
    f.write(patchMiddleCredits+'\n')
    #line 0 - comment
    f.write(xText+str(getPx(0))+' '+str(getPy(0))+commonComment+'mc.cstencoder#ind.pd;\n')
    #line 1
    #loadbang
    f.write(xObj+str(getPx(0))+' '+str(getPy(1))+' loadbang;\n')
    loadbang_id = 2
    #line 1.5
    #msg
    f.write(xMsg+str(getPx(0))+' '+str(getPy(1.5))+' '+str(ind)+';\n')
    msg_id = 3
    #float
    f.write(xObj+str(getPx(1))+' '+str(getPy(1.5))+' float \$1;\n')
    float_id = 4
    #line 1.75
    #float box
    f.write(xFloat+str(getPx(1))+' '+str(getPy(1.75))+' 0 '+xFloat2)
    floatbox_id = 5
    #line 2
    f.write(xObj+str(getPx(0))+' '+str(getPy(2))+' cstforencoder;\n')
    cstforencoder_id = 6
    #line 4.5
    #snake~ in
    f.write(xObj+str(getPx(0))+' '+str(getPy(4.5))+' snake~ in '+str(2*ind+1)+' ----------;\n')
    snake_id = 7
    #line 5
    #outlet~~
    f.write(xObj+str(getPx(0))+' '+str(getPy(5))+' outlet~;\n')
    out_id = 8
    #line 3
    #sinandcos abstractions
    for j in range(ind):
        ind2 = j + 1
        f.write(xObj+str(getPx(ind2))+' '+str(getPy(3))+' sinandcos '+str(ind2)+';\n')
        #ids from 9 to 9+ind-1
    sinandcos_id = 9
    #line 4
    #*~
    for j in range(2*ind):
        ind2 = j + 1
        ind3 = 0.5 * ind2
        f.write(xObj+str(getPx(ind3))+' '+str(getPy(4))+' *~;\n')
        #ids from 9+ind to 9+3*ind-1
    mult_id = 9 + ind
    #connections
    #loadbang to message
    f.write(xConnect+str(loadbang_id)+' 0 '+str(msg_id)+' 0;\n')
    #loadbang to float object
    f.write(xConnect+str(loadbang_id)+' 0 '+str(float_id)+' 0;\n')
    #float object to float box
    f.write(xConnect+str(float_id)+' 0 '+str(floatbox_id)+' 0;\n')
    #message to cstforencoder
    f.write(xConnect+str(msg_id)+' 0 '+str(cstforencoder_id)+' 0;\n')
    #float box to cstforencoder
    f.write(xConnect+str(floatbox_id)+' 0 '+str(cstforencoder_id)+' 1;\n')
    #cstforencoder to sinandcos abstractions
    for j in range(ind):
        f.write(xConnect+str(cstforencoder_id)+' 1 '+str(sinandcos_id+j)+' 0;\n')
    #cstforencoder to *~
    for j in range(2*ind):
        f.write(xConnect+str(cstforencoder_id)+' 0 '+str(mult_id+j)+' 0;\n')
    #cstforencoder to input 0 of snake~ in
    f.write(xConnect+str(cstforencoder_id)+' 0 '+str(snake_id)+' 0;\n')
    #sinandcos to *~~
    for j in range(ind):
        f.write(xConnect+str(sinandcos_id+j)+' 0 '+str(mult_id+2*j)+' 1;\n')
        f.write(xConnect+str(sinandcos_id+j)+' 1 '+str(mult_id+2*j+1)+' 1;\n')
    #*~ to snake~ in
    for j in range(2*ind):
        f.write(xConnect+str(mult_id+j)+' 0 '+str(snake_id)+' '+str(j+1)+';\n')
    #snake~ in to outlet~~
    f.write(xConnect+str(snake_id)+' 0 '+str(out_id)+' 0;\n')
    f.close()
print('=>'+str(maxAmbiOrder)+' mc.cstencoder#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#03 GENERATING CONSTANT ENCODERS ABSTRACTIONS")
print("________________________________________________")
for i in range (maxAmbiOrder):
    ind = i + 1
    #opens a Pure Data file for the mc.decoderblock#ind.pd abstraction
    fileName = destLibDir+'/mc.decoderblock'+str(ind)+".pd"
    f = open(fileName, 'w')
    #writes the lines of the mc.decoderblock#ind.pd Pure Data abstraction
    #writes the objects
    f.write(patchMiddleCanvas+'\n')
    f.write(patchMiddleCredits+'\n')
    #line 0 - comment
    f.write(xText+str(getPx(0))+' '+str(getPy(0))+commonComment+'mc.decoderblock#ind.pd;\n')
    #line 1
    #inlet~
    f.write(xObj+str(getPx(0))+' '+str(getPy(1))+' inlet~;\n')
    in_id = 2
    #line 1.5
    #snake~ out
    f.write(xObj+str(getPx(0))+' '+str(getPy(1.5))+' snake~ out '+str(2*ind+1)+';\n')
    snakeout_id = 3
    #line 2
    #*~0.5
    f.write(xObj+str(getPx(0))+' '+str(getPy(2))+' *~ 0.5;\n')
    mult_id = 4
    #line 2.5
    #snake~ in
    f.write(xObj+str(getPx(0))+' '+str(getPy(2.5))+' snake~ in '+str(2*ind+1)+';\n')
    snakein1_id = 5
    #line 4
    #snake~ in
    f.write(xObj+str(getPx(0.5*ind))+' '+str(getPy(4))+' snake~ in '+str(2*ind+2)+';\n')
    snakein2_id = 6
    #line 4.5
    #outlet~~
    f.write(xObj+str(getPx(0.5*ind))+' '+str(getPy(4.5))+' outlet~;\n')
    out_id = 7
    #line 2
    #mc.cstencoder#ind
    for j in range(2*ind+2):
        ind2 = j + 1
        f.write(xObj+str(getPx(ind2))+' '+str(getPy(2))+' mc.cstencoder'+str(ind)+' '+str(j)+';\n')
    cstencoder_id = 8
    #cstencoder_id between 8 and 8+2*ind+1
    #line 3
    #mc.sp#2*ind+1
    for j in range(2*ind+2):
        ind2 = j + 1
        f.write(xObj+str(getPx(j))+' '+str(getPy(3))+' mc.sp'+str(2*ind+1)+';\n')
    sp_id = 8+2*ind+2
    #connexions
    #inlet~ to snake~ out
    f.write(xConnect+str(in_id)+' 0 ' +str(snakeout_id)+' 0;\n')
    #snake~ out 0 to *~0.5
    f.write(xConnect+str(snakeout_id)+' 0 '+str(mult_id)+' 0;\n')
    #*~0.5 to snake~ in 0
    f.write(xConnect+str(mult_id)+' 0 '+str(snakein1_id)+' 0;\n')
    #snake~ out 1 to 2*ind to snake~ in 1 to 2*ind
    for j in range(2*ind):
        ind2 = j + 1
        f.write(xConnect+str(snakeout_id)+' '+str(ind2)+' '+str(snakein1_id)+' '+str(ind2)+' 0;\n')
    #mc.cstencoder#j to mc.sp#j inlet 1
    for j in range(2*ind+2):
        f.write(xConnect+str(cstencoder_id+j)+' 0 '+str(sp_id+j)+' 1;\n')
    #snake~ in to mc.sp#j inlet 0
    for j in range(2*ind+2):
        f.write(xConnect+str(snakein1_id)+' 0 '+str(sp_id+j)+' 0;\n')
    #mc.sp#j outlet 0 to snake~ in inlet j
    for j in range(2*ind+2):
        f.write(xConnect+str(sp_id+j)+' 0 '+str(snakein2_id)+' '+str(j)+';\n')
    #snake~ in to outlet~~
    f.write(xConnect+str(snakein2_id)+' 0 '+str(out_id)+' 0;\n')
    f.close()
print('=>'+str(maxAmbiOrder)+' mc.decoderblock#ind.pd common abstractions generated')
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