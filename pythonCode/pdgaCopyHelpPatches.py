#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the mc.decoderblock#ind abstractions
_______________________________________________________
"""   
def copyHelpPatches(dir1, dir2):
    f = '/doubledelay-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/flanger-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/gt~-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/hoa.decoder-help.pd'
    #full decoders
    for n in range(bf.maxAmbiOrder):
        for p in range(4, 2*bf.maxAmbiOrder+2+1):
            shutil.copy(dir1+f, dir2+'/hoa.decoder'+str(n+1)+'_'+str(p)+'-help.pd')
    #regular decoders
    for n in range(bf.maxAmbiOrder):
        shutil.copy(dir1+f, dir2+'/hoa.regdecoder'+str(n+1)+'-help.pd')
    #regular decoders
    for n in range(bf.maxAmbiOrder):
        shutil.copy(dir1+f, dir2+'/hoa.stereodecoder'+str(n+1)+'-help.pd')
    #decoder1
    shutil.copy(dir1+f, dir2+'/decoder1-help.pd')
    #
    f = '/hoa.encoder-help.pd'
    #hoa encoders
    for n in range(bf.maxAmbiOrder):
        shutil.copy(dir1+f, dir2+'/hoa.encoder'+str(n+1)+'-help.pd')
    #encoder1
    shutil.copy(dir1+f, dir2+'/encoder1-help.pd')
    #
    f = '/hoa.vbap-help.pd'
    for n in range(bf.maxAmbiOrder):
        shutil.copy(dir1+f, dir2+'/hoa.vbap'+str(n+1)+'-help.pd')
    #
    f = '/looper-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/mc.busmult-help.pd'
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.busmult'+str(n+1)+'-help.pd')
    #
    f = '/mc.busplus-help.pd'
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.busplus'+str(n+1)+'-help.pd')
    #
    f = '/mc.busselector-help.pd'
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.busselector'+str(n+1)+'-help.pd')
    #
    f = '/mc.gain-help.pd'
    #mc.gain
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.gain'+str(n+1)+'-help.pd')
    #gain
    shutil.copy(dir1+f, dir2+'/gain-help.pd')
    #
    f = '/mc.player-help.pd'
    #mc.player
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.player'+str(n+1)+'-help.pd')
    #player
    shutil.copy(dir1+f, dir2+'/player-help.pd')
    #stereoplayer
    shutil.copy(dir1+f, dir2+'/stereoplayer-help.pd')
    #quadriplayer
    shutil.copy(dir1+f, dir2+'/quadriplayer-help.pd')
    #
    f = '/mc.recorder-help.pd'
    #mc.recorder
    for n in range(2*bf.maxAmbiOrder+2):
        shutil.copy(dir1+f, dir2+'/mc.recorder'+str(n+1)+'-help.pd')
    #recorder
    shutil.copy(dir1+f, dir2+'/recorder-help.pd')
    #stereorecorder
    shutil.copy(dir1+f, dir2+'/stereorecorder-help.pd') 
    #
    f = '/meter-help.pd'
    #meter
    shutil.copy(dir1+f, dir2+f)
    #mc.meter2
    shutil.copy(dir1+f, dir2+'/mc.meter2-help.pd')
    #mc.meter4
    shutil.copy(dir1+f, dir2+'/mc.meter4-help.pd')
    #mc.meter8
    shutil.copy(dir1+f, dir2+'/mc.meter8-help.pd')
    #mc.meter16
    shutil.copy(dir1+f, dir2+'/mc.meter16-help.pd')
    #
    f = '/multisource-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/musdelay-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/mypong-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/rtgranu-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/scope-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/selector2-help.pd'
    #selector2
    shutil.copy(dir1+f, dir2+f)
    #selector2-mod
    shutil.copy(dir1+f, dir2+'/selector2-mod-help.pd')
    #
    f = '/simpleharmo-help.pd'
    shutil.copy(dir1+f, dir2+f)
    #
    f = '/spectrogram-help.pd'
    shutil.copy(dir1+f, dir2+f)