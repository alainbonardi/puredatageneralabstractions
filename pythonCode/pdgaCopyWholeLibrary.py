#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import shutil
from distutils.dir_util import copy_tree
#import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def copyWholeLibrary(dir2):
    #common abstractions
    dir1 = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions/commonAbstractions'
    copy_tree(dir1, dir2)
    #misc (credits)
    dir1 = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions/misc'
    copy_tree(dir1, dir2)
    #sounds
    dir1 = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions/sounds'
    copy_tree(dir1, dir2)
    #user abstractions
    dir1 = '/Users/alainbonardi/Documents/Github/puredatageneralabstractions/userAbstractions'
    copy_tree(dir1, dir2)
    