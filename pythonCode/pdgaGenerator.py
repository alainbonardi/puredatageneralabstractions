# -*- coding: utf-8 -*-

import os
import shutil
import tkinter as tkinter
from tkinter import filedialog
import pdgaBasicFunctions as bf
import pdgaGenerateSp as gsp
import pdgaGenerateCstEncoder as gcstenco
import pdgaGenerateDecoderBlock as gdb
import pdgaGenerateRegDecoder as grd
import pdgaGenerateGain as gg
import pdgaGenerateEncoder as genco


#origLibDir = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions'
#destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_abstractions'

"""
_______________________________________________________
Global constants and variables for Pure Data patches
_______________________________________________________
"""

#
#global variables

#flags to run or not such or such generation
mcsp_flag = True
mccstencoder_flag = True
mcdecoderblock_flag = True
mcregdecoder_flag = True
mcgain_flag = True
mcencoder_flag = True


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
    gcstenco.generate_hoacstencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.cstencoder#ind.pd common abstractions generated')
else:
    print('=> no hoa.cstencoder#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#03 GENERATING DECODER BLOCK ABSTRACTIONS")
print("________________________________________________")
if (mcdecoderblock_flag):
    gdb.generate_hoadecoderblock(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.decoderblock#ind.pd common abstractions generated')
else:
    print('=> no hoa.decoderblock#ind.pd common abstractions generated')
#
print("________________________________________________")
print("GENERATING USER ABSTRACTIONS==================")
print("________________________________________________")
#
print("________________________________________________")
print("STEP#04 GENERATING REGULAR DECODER ABSTRACTIONS")
print("________________________________________________")
if (mcregdecoder_flag):
    grd.generate_hoaregdecoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.regdecoder#ind.pd common abstractions generated')
else :
    print('=> no hoa.regdecoder#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#05 GENERATING GAIN ABSTRACTIONS")
print("________________________________________________")
if (mcgain_flag):
    gg.generate_mcgain(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.gain#ind.pd common abstractions generated')
else:
    print('=> no mc.gain#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#06 GENERATING ENCODER ABSTRACTIONS")
print("________________________________________________")
if (mcencoder_flag):
    genco.generate_hoaencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.encoder#ind.pd common abstractions generated')
else:
    print('=> no hoa.encoder#ind.pd user abstractions generated')