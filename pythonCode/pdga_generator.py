# -*- coding: utf-8 -*-

import os
import shutil

origLibDir = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions'
destLibDir = '/Users/alainbonardi/Dropbox/faustFactory/puredatageneralabstractions_factory/generated_abstractions'

"""
_______________________________________________________
Constants for Pure Data patches
_______________________________________________________
"""
leftMargin = 25
topMargin = 25
maxAmbiOrder = 7

print("________________________________________________")
print("STEP#1-1 GENERATING SCALAR PRODUCT PATCHES")
for i in range (2*maxAmbiOrder+1):
    