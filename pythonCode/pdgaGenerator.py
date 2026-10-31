# -*- coding: utf-8 -*-

import os
import shutil
import tkinter as tkinter
from tkinter import filedialog


import pdgaBasicFunctions as bf
import pdgaHoaGeneration as hoag
import pdgaMcGeneration as mcg
import pdgaSaGeneration as sag
import pdgaCopyHelpPatches as chp
import pdgaCopyWholeLibrary as cwl

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
hoa_flag = True
mc_flag = True
sag_flag = True
chp_flag = True
cwl_flag = True


print("________________________________________________")
print("________________________________________________")
print("PURE DATA GENERATING ABSTRACTIONS===============")
print("LIBRARY GENERATION==============================")
print("________________________________________________")
print("________________________________________________")
print("\n\n\n")
#print("CHOOSE A FOLDER WHERE YOU WILL INCLUDE YOUR PURE DATA GENERATED ABSTRACTIONS FOLDER")
#choose a folder
#rootPath = filedialog.askdirectory()
#destLibDir = rootPath+'/generated_pdga_abstractions'
#provisional fixed directory
destLibDir = '/Users/alainbonardi/Library/CloudStorage/Dropbox/pythonFactory/puredatageneralabstractions_factory/puredatageneralabstractions'
#
if os.path.exists(destLibDir):
    print("Existing directory containing the original generated abstractions, the previous one is deleted")
    shutil.rmtree(destLibDir)
#we create a new folder for the generated abstractions
os.mkdir(destLibDir)

helpOrigDir = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions/helpPatches'
  
#
print("________________________________________________")
print("________________________________________________")
print("STEPS#100 HOA GENERATION")
print("________________________________________________")
print("________________________________________________")
#
if (hoa_flag):
    #
    print("________________________________________________")
    print("STEP#101 GENERATING ENCODER ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoaencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.encoder#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#102 GENERATING CONSTANT ENCODERS ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoacstencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.cstencoder#ind.pd common abstractions generated')
    #
    print("________________________________________________")
    print("STEP#103 GENERATING ENCODING MODULE ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoaencodingmodule(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.encodingmodule#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#104 GENERATING DECODER BLOCK ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoadecoderblock(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.decoderblock#ind.pd common abstractions generated')
    #
    print("________________________________________________")
    print("STEP#105 GENERATING REGULAR DECODER ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoaregdecoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.regdecoder#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#106 GENERATING HOA COMPLETE DECODERS")
    print("________________________________________________")
    hoag.generate_hoadeco(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' hoa.decoder#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#107 GENERATING 2D PROJECTIONS")
    print("________________________________________________")
    hoag.generate_hoa2dprojection(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.2dprojection#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#108 GENERATING STEREO HOA DECODERS")
    print("________________________________________________")
    hoag.generate_hoastereodecoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.stereodecoder#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#109 GENERATING ELEMENTARY VBAP ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_vbap(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' vbap#ind_f.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#110 GENERATING HOA MAP ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoamap(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.map#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#111 GENERATING HOA SCOPE ABSTRACTIONS")
    print("________________________________________________")
    hoag.generate_hoascope(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.scope#ind.pd user abstractions generated')
    #
    print("\n\n\n")
    
#
print("________________________________________________")
print("________________________________________________")
print("STEPS#200 MC GENERATION")
print("________________________________________________")
print("________________________________________________")
#
if (mc_flag):
    #
    print("________________________________________________")
    print("STEP#201 GENERATING GAIN ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcgain(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.gain#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#202 GENERATING DUPLICATE ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcduplicate(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.duplicate#ind_f.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#203 GENERATING MC METER ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcmeter(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.meter#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#204 GENERATING SCALAR PRODUCT ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcsp(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.sp#ind.pd common abstractions generated')
    #
    print("________________________________________________")
    print("STEP#205 GENERATING BUS MULT")
    print("________________________________________________")
    mcg.generate_mcbusmult(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busmult#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#206 GENERATING BUS PLUS")
    print("________________________________________________")
    mcg.generate_mcbusplus(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busplus#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#207 GENERATING BUS SELECTORS")
    print("________________________________________________")
    mcg.generate_mcbusselector(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busselector#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#208 GENERATING MC NORMALIZE ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_normalize(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.normalize#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#209 GENERATING PLAYER ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcplayer(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.player#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#210 GENERATING RECORDER ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcrecorder(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.recorder#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#211 GENERATING STEREO ZERO PADDING ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mczeropad(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.stereozeropad#ind_f.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#212 GENERATING MC VBAP ABSTRACTIONS")
    print("________________________________________________")
    mcg.generate_mcvbap(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' hoa.vbap#ind.pd user abstractions generated')
    
    #
    print("\n\n\n")
#
print("________________________________________________")
print("________________________________________________")
print("STEPS#300 SPECTRAL AMBISONIC GENERATION")
print("________________________________________________")
print("________________________________________________")
#
if (sag_flag):
    print("________________________________________________")
    print("STEP#301 GENERATING SA AMBI TO SPECTRAL ABSTRACTIONS")
    print("________________________________________________")
    sag.generate_atosAbstractions(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' sa.ambi2sa#ind.pd user abstractions generated')
    #
    print("________________________________________________")
    print("STEP#302 GENERATING SA SPECTRAL TO AMBI ABSTRACTIONS")
    print("________________________________________________")
    sag.generate_stoaAbstractions(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' sa.sa2ambi#ind.pd user abstractions generated')
    
    print("\n\n\n")
#
print("________________________________________________")
print("________________________________________________")
print("STEPS#400 FILE COPY")
print("________________________________________________")
print("________________________________________________")
#
print("________________________________________________")
print("STEP#401 COPYING HELP PATCHES")
print("________________________________________________")
if (chp_flag):
    chp.copyHelpPatches(helpOrigDir, destLibDir)
    print('=> help patches copied') 
else:
    print('=> help patches not copied') 
#
print("________________________________________________")
print("STEP#402 COPYING THE WHOLE LIBRARY")
print("________________________________________________")
if (cwl_flag):
    cwl.copyWholeLibrary(destLibDir)
    print('=> whole library copied') 
else:
    print('=> whole library not copied') 