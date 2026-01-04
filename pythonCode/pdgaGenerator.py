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
import pdgaGenerateRecorder as genrec
import pdgaGeneratePlayer as genplay
import pdgaGenerate2dprojection as gen2dproj
import pdgaGenerateStereoDecoder as gstereodec
import pdgaGenerateBusSelector as gbussel
import pdgaGenerateBusPlus as gbusplus
import pdgaGenerateBusMult as gbusmult
import pdgaGenerateDuplicate as gdup
import pdgaGenerateElemVbap as gvbap
import pdgaGenerateHoaVbap as ghoavbap
import pdgaGenerateCompleteDecoder as ghoadeco
import pdgaGenerateZeroPadding as gzeropad
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
mcsp_flag = True
hoacstencoder_flag = True
hoadecoderblock_flag = True
hoaregdecoder_flag = True
mcgain_flag = True
hoaencoder_flag = True
mcrecorder_flag = True
mcplayer_flag = True
hoa2dprojection_flag = True
hoastereodecoder_flag = True
mcbusselector_flag = True
mcbusplus_flag = True
mcbusmult_flag = True
mcduplicate_flag = True
vbap_flag = True
hoavbap_flag = True
mczeropad_flag = True
hoadeco_flag = True
chp_flag = True
cwl_flag = True


print("________________________________________________")
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
if (hoacstencoder_flag):
    gcstenco.generate_hoacstencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.cstencoder#ind.pd common abstractions generated')
else:
    print('=> no hoa.cstencoder#ind.pd common abstractions generated')
#
print("________________________________________________")
print("STEP#03 GENERATING DECODER BLOCK ABSTRACTIONS")
print("________________________________________________")
if (hoadecoderblock_flag):
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
if (hoaregdecoder_flag):
    grd.generate_hoaregdecoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.regdecoder#ind.pd user abstractions generated')
else :
    print('=> no hoa.regdecoder#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#05 GENERATING GAIN ABSTRACTIONS")
print("________________________________________________")
if (mcgain_flag):
    gg.generate_mcgain(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.gain#ind.pd user abstractions generated')
else:
    print('=> no mc.gain#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#06 GENERATING ENCODER ABSTRACTIONS")
print("________________________________________________")
if (hoaencoder_flag):
    genco.generate_hoaencoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.encoder#ind.pd user abstractions generated')
else:
    print('=> no hoa.encoder#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#07 GENERATING RECORDER ABSTRACTIONS")
print("________________________________________________")
if (mcrecorder_flag):
    genrec.generate_mcrecorder(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.recorder#ind.pd user abstractions generated')
else:
    print('=> no mc.recorder#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#08 GENERATING PLAYER ABSTRACTIONS")
print("________________________________________________")
if (mcplayer_flag):
    genplay.generate_mcplayer(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.player#ind.pd user abstractions generated')
else:
    print('=> no mc.player#ind.pd user abstractions generated')
#
print("________________________________________________")
print("STEP#09 GENERATING 2D PROJECTIONS")
print("________________________________________________")
if (hoa2dprojection_flag):
    gen2dproj.generate_hoa2dprojection(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.2dprojection#ind.pd user abstractions generated')
else:
    print('=> no hoa.stereodecoder#ind.pduser abstractions generated')
#
print("________________________________________________")
print("STEP#10 GENERATING STEREO HOA DECODERS")
print("________________________________________________")
if (mcplayer_flag):
    gstereodec.generate_hoastereodecoder(destLibDir)
    print('=>'+str(bf.maxAmbiOrder)+' hoa.stereodecoder#ind.pd user abstractions generated')
else:
    print('=> no hoa.stereodecoder#ind.pduser abstractions generated')
#
print("________________________________________________")
print("STEP#11 GENERATING BUS SELECTORS")
print("________________________________________________")
if (mcbusselector_flag):
    gbussel.generate_mcbusselector(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busselector#ind.pd user abstractions generated')
else:
    print('=> no mc.busselector#ind.pd user abstractions generated')   
#
print("________________________________________________")
print("STEP#12 GENERATING BUS PLUS")
print("________________________________________________")
#
if (mcbusplus_flag):
    gbusplus.generate_mcbusplus(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busplus#ind.pd user abstractions generated')
else:
    print('=> no mc.busplus#ind.pd user abstractions generated')  
#
print("________________________________________________")
print("STEP#13 GENERATING BUS MULT")
print("________________________________________________")
#
if (mcbusmult_flag):
    gbusmult.generate_mcbusmult(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.busmult#ind.pd user abstractions generated')
else:
    print('=> no mc.busmult#ind.pd user abstractions generated')  
#
print("________________________________________________")
print("STEP#14 GENERATING DUPLICATE ABSTRACTIONS")
print("________________________________________________")
if (mcduplicate_flag):
    gdup.generate_mcduplicate(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.duplicate#ind_f.pd user abstractions generated')
else:
    print('=> no mc.duplicate#ind_f.pd user abstractions generated')   
#
print("________________________________________________")
print("STEP#15 GENERATING ELEMENTARY VBAP ABSTRACTIONS")
print("________________________________________________")
if (vbap_flag):
    gvbap.generate_vbap(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' vbap#ind_f.pd user abstractions generated')
else:
    print('=> no vbap#ind_f.pd user abstractions generated')   
#
print("________________________________________________")
print("STEP#16 GENERATING HOA VBAP ABSTRACTIONS")
print("________________________________________________")
if (hoavbap_flag):
    ghoavbap.generate_hoavbap(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' hoa.vbap#ind.pd user abstractions generated')
else:
    print('=> no hoa.vbap#ind.pd user abstractions generated')  
#
print("________________________________________________")
print("STEP#17 GENERATING STEREO ZERO PADDING ABSTRACTIONS")
print("________________________________________________")
if (mczeropad_flag):
    gzeropad.generate_mczeropad(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' mc.stereozeropad#ind_f.pd user abstractions generated')
else:
    print('=> no mc.stereozeropad#ind_f.pd user abstractions generated')  
#
print("________________________________________________")
print("STEP#18 GENERATING HOA COMPLETE DECODERS")
print("________________________________________________")
if (hoadeco_flag):
    ghoadeco.generate_hoadeco(destLibDir)
    print('=>'+str(2*bf.maxAmbiOrder+2)+' hoa.decoder#ind.pd user abstractions generated')
else:
    print('=> no hoa.decoder#ind.pd user abstractions generated')  
#
print("________________________________________________")
print("STEP#19 COPYING HELP PATCHES")
print("________________________________________________")
if (chp_flag):
    chp.copyHelpPatches(helpOrigDir, destLibDir)
    print('=> help patches copied') 
else:
    print('=> help patches not copied') 
#
print("________________________________________________")
print("STEP#20 COPYING THE WHOLE LIBRARY")
print("________________________________________________")
if (cwl_flag):
    cwl.copyWholeLibrary(destLibDir)
    print('=> whole library copied') 
else:
    print('=> whole library not copied') 