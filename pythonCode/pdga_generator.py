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
d1 = 50
d2 = 100
d3 = 150
maxAmbiOrder = 7
patchMiddleCanvas = '#N canvas 50 50 600 600 10;'
patchMiddleCredits = '#X obj 10 550 pdga_helpcredit;'
xObj = '#X obj'

print("________________________________________________")
print("CHOOSE A FOLDER WHERE YOU WILL INCLUDE YOUR PURE DATA GENERATED ABSTRACTIONS FOLDER")
rootPath = filedialog.askdirectory()
#print(rootPath)
destLibDir = rootPath+'/generated_pdga_abstractions'
#print(destLibDir)
if os.path.exists(destLibDir):
    print("Existing directory containing the original generated abstractions, the previous one is deleted")
    shutil.rmtree(destLibDir)
#we create a new folder for the generated abstractions
os.mkdir(destLibDir)

#
print("________________________________________________")
print("STEP#1-1 GENERATING SCALAR PRODUCT PATCHES")
for i in range (2*maxAmbiOrder+1):
    ind = i + 1
    #opens a Pure Data file for the mc.sp#ind.pd abstraction
    fileName = destLibDir+'/mc.sp'+str(ind)+".pd"
    #print(fileName)
    f = open(fileName, 'w')
    #writes the lines of the mc.sp#ind.pd Pure Data abstraction
    f.write(patchMiddleCanvas+'\n')
    f.write(patchMiddleCredits+'\n')
    f.write(xObj+' '+str(leftMargin)+' '+str(topMargin)+' inlet~;\n')
    f.write(xObj+' '+str(leftMargin+d2)+' '+str(topMargin)+' inlet~;\n')
    f.write(xObj+' '+str(leftMargin)+' '+str(topMargin+4*d2)+' outlet~;\n')
    f.write(xObj+' '+str(leftMargin)+' '+str(topMargin+d2)+' snake~ out '+str(ind)+';\n')
    f.write(xObj+' '+str(leftMargin+d2)+' '+str(topMargin+d2)+' snake~ out '+str(ind)+';\n')
    #writes the *~
    for j in range(ind):
        ind2 = j + 1
        
    f.close()