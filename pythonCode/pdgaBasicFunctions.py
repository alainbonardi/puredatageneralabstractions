#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#global constants
leftMargin = 25
topMargin = 25
dx = 100
dy = 100

patchMiddleCanvas = '#N canvas 50 50 600 600 10;\n'
patchMiddleCredits = '#X obj 10 550 pdga_helpcredit;\n'
patchAbstractionCnv1_1 = '#X obj 15 6 cnv 15 550 25 empty empty'
patchAbstractionCnv1_2 = '#X obj 15 32 cnv 15 550 25 empty empty'
patchAbstractionCnv2_1 = '20 12 0 18 #606060 #fcfcfc 0;'
patchAbstractionCnv2_2 = '20 12 0 12 #606060 #fcfcfc 0;'

xObj = '#X obj'
xText = '#X text'
xConnect = '#X connect'
xMsg = '#X msg'
xFloat = '#X floatatom'
#xFloat2 = '5 0 0 0 - - - 0;\n'
xFloat2 = '5 0 0 1 '
xFloat3 = ' - - 0'

maxAmbiOrder = 7
commonComment = 'Common abstractions generated - '

#index of current object processed
objInd = 0

"""
_______________________________________________________
Computes the x coordinate of the object
_______________________________________________________
"""
def getPx(ix):
    px = leftMargin + ix * dx
    return int(px)

"""
_______________________________________________________
Computes the y coordinate of the object
_______________________________________________________
"""
def getPy(iy):
    py = topMargin + iy * dy
    return int(py)


"""
_______________________________________________________
Resets the object index
_______________________________________________________
"""
def resetObjInd():
    global objInd
    objInd = 0
    
"""
_______________________________________________________
Increases the object index
_______________________________________________________
"""
def incObjInd():
    global objInd
    objInd = objInd + 1

"""
_______________________________________________________
Prepares an XText line for a comment
_______________________________________________________
"""
def getXText(px, py, s):
    sText = xText+' '+str(getPx(px))+' '+str(getPy(py))+' '+s+';\n'
    return sText
 
"""
_______________________________________________________
Prepares an XObj line for an object
_______________________________________________________
"""   
def getXObj(px, py, s):
    sObj = xObj+' '+str(getPx(px))+' '+str(getPy(py))+' '+s+';\n'
    return sObj

 
"""
_______________________________________________________
Prepares an XMsg line for a message
_______________________________________________________
"""   
def getXMsg(px, py, s):
    sMsg = xMsg+' '+str(getPx(px))+' '+str(getPy(py))+' '+s+';\n'
    return sMsg

"""
_______________________________________________________
Prepares an XFloat line for a float box
_______________________________________________________
"""   
def getXFloat(px, py, s):
    sFloat = xFloat+' '+str(getPx(px))+' '+str(getPy(py))+' '+xFloat2+s+xFloat3+';\n'
    return sFloat

"""
_______________________________________________________
Prepares an XConnect line for a connection
_______________________________________________________
"""  
def getXConnect(obj1, out1, obj2, in2):
    sConnect = xConnect+' '+str(obj1)+' '+str(out1)+' '+str(obj2)+' '+str(in2)+';\n'
    return sConnect

"""
_______________________________________________________
Writes an XText line for a comment
_______________________________________________________
"""
#writes the formatted XText on f file and returns the obj index
def appendXText(f, px, py, s):
    global objInd
    f.write(getXText(px, py, s))
    objInd = objInd + 1

"""
_______________________________________________________
Writes an XObj line for an object
_______________________________________________________
"""  
#writes the formatted XObj on f file and returns the obj index
def appendXObj(f, px, py, s):
    global objInd
    f.write(getXObj(px, py, s))
    objInd = objInd + 1
    return objInd

"""
_______________________________________________________
Writes an XMsg line for a message
_______________________________________________________
""" 
#writes the formatted XMsg on f file and returns the obj index
def appendXMsg(f, px, py, s):
    global objInd
    f.write(getXMsg(px, py, s))
    objInd = objInd + 1
    return objInd

"""
_______________________________________________________
Writes an XFloat line for a float box
_______________________________________________________
"""   
#writes the formatted XFloat on f file and returns the obj index
def appendXFloat(f, px, py, s):
    global objInd
    f.write(getXFloat(px, py, s))
    objInd = objInd + 1
    return objInd

"""
_______________________________________________________
Writes an XConnect line for a connection
_______________________________________________________
"""      
def appendXConnect(f, obj1, out1, obj2, in2):
    f.write(getXConnect(obj1, out1, obj2, in2))

"""
_______________________________________________________
Writes the canvas and credits lines and resets the index of objects
_______________________________________________________
"""       
def createMiddleCommonAbstraction(f):
    global objInd
    f.write(patchMiddleCanvas)
    f.write(patchMiddleCredits)
    objInd = 0

