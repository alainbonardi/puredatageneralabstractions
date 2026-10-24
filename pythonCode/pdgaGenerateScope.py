#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdgaBasicFunctions as bf

"""
_______________________________________________________
Generates the hoa.scope#ind abstractions
_______________________________________________________
"""   
def generate_hoascope(dDir):
    for i in range (bf.maxAmbiOrder):
        ind = i + 1
        #opens a Pure Data file for the mc.regdecoder#ind.pd abstraction
        fileName = dDir+'/hoa.scope'+str(ind)+".pd"
        f = open(fileName, 'w')
        #writes the lines of the hoa.scope#ind.pd Pure Data abstraction
        #writes the objects
        f.write(bf.patchMiddleCanvas)
        f.write(bf.patchAbstractionCnv1_1+' hoa.scope'+str(ind)+' '+bf.patchAbstractionCnv2_1+'\n')
        bf.resetObjInd()
        f.write(bf.patchAbstractionCnv1_2+ ' hoa\ scope\ at\ order\ '+str(ind)+' '+bf.patchAbstractionCnv2_2+'\n')
        bf.incObjInd()

        #the scope in the canvas
        scope_id = bf.appendXObj(f, 0.29, 1.45, 'else/scope~ 128 128 64 3 32 -1 1 0 0 0 0 30 30 30 190 190 190 160 160 160 0 empty;')
        #line 0.5 - else/initmess 64 32
        init_id = bf.appendXObj(f, 1, 0.5, 'else/initmess 64 32')
        #line 1 - list box
        listBox_id = bf.appendXListBox(f, '125 125 10 0 0 0 - - - 10')
        #line 1 - inlet~
        in_id = bf.appendXObj(f, 2, 1, 'inlet~')
        #line 1 - loadbang
        loadbang_id = bf.appendXObj(f, 4, 1, 'loadbang')
        #line 1.25 - snake~ out
        snakeout_id = bf.appendXObj(f, 2, 1.25, 'snake~ out '+str(2*ind+1))
        #line 1.25 - msg 1
        msg1_id = bf.appendXMsg(f, 4, 1.25, '1')
        #line 1.25 - msg 25
        msg25_id = bf.appendXMsg(f, 5, 1.25, '25')
        #line 1.5 - *~ 0.5
        mult0_id = bf.appendXObj(f, 2, 1.5, '*~ 0.5')
        #line 1.5 - toggle
        tgl_id = bf.appendXObj(f, 4, 1.5, 'tgl 15 0 empty empty empty 0 -10 0 12 #fcfcfc #000000 #000000 0 1')
        #line 1.5 - float
        flo_id = bf.appendXFloat(f, 5, 1.5, '5 0 0 0 - - - 0')
        #line 1.75 - snake~ in
        snakein_id = bf.appendXObj(f, 2, 1.75, 'snake~ in '+str(2*ind+1))
        #line 1.75 - metro
        metro_id = bf.appendXObj(f, 4, 1.75, 'metro 1')
        #line 1.75 - phasor~~
        phasor_id = bf.appendXObj(f, 5, 1.75, 'phasor~')
        #line 1.75 - sig~~
        sig_id = bf.appendXObj(f, 3, 1.75, 'sig~ 1')
        #line 2 - *~ 360
        mult360_id = bf.appendXObj(f, 5, 2, '*~ 360')
        #line 2.25 - snapshot~
        snap_id = bf.appendXObj(f, 4, 2.25, 'snapshot~')
        #line 2.5 - msgangle
        msgangle_id = bf.appendXMsg(f, 3.75, 2.5, 'angle \$1')
        #line 2.75 - hoa.encoder
        encoder_id = bf.appendXObj(f, 3, 2.75, 'hoa.encoder'+str(ind))
        #line 2.75 - expr~~
        expr_id = bf.appendXObj(f, 4.5, 2.75, 'expr~ 0.75 - $v1')
        #line 3. - mc.normalize 1 and 2
        norm1_id = bf.appendXObj(f, 2, 3, 'mc.normalize'+str(2*ind+1))
        norm2_id = bf.appendXObj(f, 3, 3, 'mc.normalize'+str(2*ind+1))
        #line 3. - cos~ 1 and 2
        cos1_id = bf.appendXObj(f, 4.5, 3, 'cos~')
        cos2_id = bf.appendXObj(f, 5.5, 3, 'cos~')
        #line 4 - mc.sp
        sp_id = bf.appendXObj(f, 2, 4, 'mc.sp'+str(2*ind+1))
        #line 4.25 - abs~
        abs_id = bf.appendXObj(f, 2, 4.25, 'abs~')
        #line 4.5 - mult1 and mult2
        mult1_id = bf.appendXObj(f, 1.5, 4.5, '*~')
        mult2_id = bf.appendXObj(f, 2.5, 4.5, '*~')
        
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        
        #connections
        #else/initmess to listbox
        bf.appendXConnect(f, init_id, 0, listBox_id, 0)
        #listbox to scope
        bf.appendXConnect(f, listBox_id, 0, scope_id, 0)
        #inlet~ to snake~ out
        bf.appendXConnect(f, in_id, 0, snakeout_id, 0)
        #outlet 0 of snake~ out to *~ 0.5
        bf.appendXConnect(f, snakeout_id, 0, mult0_id, 0)
        #outlet of *~ 0.5 to inlet 0 of snake~ in
        bf.appendXConnect(f, mult0_id, 0, snakein_id, 0)
        #connections of all other outlets of snake~ out to the corresponding outlets of snake~ in
        for j in range(2*ind):
            bf.appendXConnect(f, snakeout_id, j+1, snakein_id, j+1)
        #snake~ in to mc.normalize
        bf.appendXConnect(f, snakein_id, 0, norm1_id, 0)
        #mc.normalize 1 to inlet 0 of mc.sp
        bf.appendXConnect(f, norm1_id, 0, sp_id, 0)
        #mc.normalize 2 to inlet 1 of mc.sp
        bf.appendXConnect(f, norm2_id, 0, sp_id, 1)
        #mc.sp to abs~~
        bf.appendXConnect(f, sp_id, 0, abs_id, 0)
        #abs~ to mult1 and mult2
        bf.appendXConnect(f, abs_id, 0, mult1_id, 0)
        bf.appendXConnect(f, abs_id, 0, mult2_id, 0)
        #loadbang to msg 1
        bf.appendXConnect(f, loadbang_id, 0, msg1_id, 0)
        #loadbang to msg 25
        bf.appendXConnect(f, loadbang_id, 0, msg25_id, 0)
        #msg1 to toggle
        bf.appendXConnect(f, msg1_id, 0, tgl_id, 0)
        #toggle to metro
        bf.appendXConnect(f, tgl_id, 0, metro_id, 0)
        #msg25 to Float
        bf.appendXConnect(f, msg25_id, 0, flo_id, 0)
        #Float to phasor~
        bf.appendXConnect(f, flo_id, 0, phasor_id, 0)
        #metro to snapshot~
        bf.appendXConnect(f, metro_id, 0, snap_id, 0)
        #phasor~ to *~ 360
        bf.appendXConnect(f, phasor_id, 0, mult360_id, 0)
        #*~ 360 to snapshot~~
        bf.appendXConnect(f, mult360_id, 0, snap_id, 0)
        #snapshot~ to msgangle
        bf.appendXConnect(f, snap_id, 0, msgangle_id, 0)
        #msgangle to inlet 1 of encoder
        bf.appendXConnect(f, msgangle_id, 0, encoder_id, 1)
        #phasor~ to expr~~
        bf.appendXConnect(f, phasor_id, 0, expr_id, 0)
        #phasor~ to cos~ 2
        bf.appendXConnect(f, phasor_id, 0, cos2_id, 0)
        #expr~ to cos~ 1
        bf.appendXConnect(f, expr_id, 0, cos1_id, 0)
        #cos~ 1 to the inlet 1 of mult 1
        bf.appendXConnect(f, cos1_id, 0, mult1_id, 1)
        #cos~ 2 to the inlet 1 of mult 2
        bf.appendXConnect(f, cos2_id, 0, mult2_id, 1)        
        #sig~ to encoder
        bf.appendXConnect(f, sig_id, 0, encoder_id, 0)
        #encoder to mc.normalize 2
        bf.appendXConnect(f, encoder_id, 0, norm2_id, 0)
        #mult1 to inlet 0 of scope
        bf.appendXConnect(f, mult1_id, 0, scope_id, 0)
        #mult2 to inlet 1 of scope
        bf.appendXConnect(f, mult2_id, 0, scope_id, 1)        
        
        '''
        bngopen_id = bf.appendXObj(f, 0.8, 1.46, 'bng 15 250 50 0 empty empty open 17 7 0 10 #0c4044 #000000 #000000')
        #toggle in the canvas to play
        tglplay_id = bf.appendXObj(f, 1.27, 1.46, 'tgl 15 0 empty empty play 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        #toggle for loop/no loop selection
        tglloop_id = bf.appendXObj(f, 1.8, 1.46, 'tgl 15 0 empty empty loop 17 7 0 10 #fcfcfc #000000 #000000 0 1')
        #horizontal slider to set the volume
        hslvol_id = bf.appendXObj(f, 2.35, 1.46, 'hsl 80 15 0 1 0 0 empty empty vol -2 -8 0 10 #fcfcfc #000000 #000000 0 1')
        #inlet for control messages of the player
        in_id = bf.appendXObj(f, 2.5, 0.5, 'inlet')
        #route object
        route_id = bf.appendXObj(f, 2.5, 0.8, 'route vol play loop')
        #openpanel object
        openpanel_id = bf.appendXObj(f, 2.5, 2, 'openpanel')
        #list prepend
        list1_id = bf.appendXObj(f, 2.5, 2.25, 'list prepend set open')
        #list trim
        list2_id = bf.appendXObj(f, 2.5, 2.5, 'list trim')
        #open message
        msgopen_id = bf.appendXMsg(f, 2.5, 2.75, 'open')
        #readsf~ #ind object
        readsf_id = bf.appendXObj(f, 2.5, 3.25, 'readsf~ '+str(ind))
        #bang object
        bang_id = bf.appendXObj(f, 3.5, 3.75, 'bang')
        #float object
        float_id = bf.appendXObj(f, 3.5, 4, 'f 0')
        #various *~ (#ind instances)
        for j in range(ind):
            k = bf.appendXObj(f, 2.5+0.5*j, 4.5, '*~')
        #comes back to the first one
        mult_id = float_id + 1
        #snake~ in #ind object
        snakein_id = bf.appendXObj(f, 2.5, 4.75, 'snake~ in '+str(ind))
        #outlet~ object
        out_id = bf.appendXObj(f, 2.5, 5, 'outlet~')
        #level msg
        msglevel_id = bf.appendXMsg(f, 2.5+0.5*ind, 3.75, '\$1 20')
        #line~ object
        line_id = bf.appendXObj(f, 2.5+0.5*ind, 4, 'line~')
        #trigger object
        trig_id = bf.appendXObj(f, 2, 2.25, 't f b')
        #
        f.write(bf.patchMiddleCredits)
        bf.incObjInd()
        #connections
        #inlet to route
        bf.appendXConnect(f, in_id, 0, route_id, 0)
        #vol in route to hsl vol
        bf.appendXConnect(f, route_id, 0, hslvol_id, 0)
        #play in route to play toogle
        bf.appendXConnect(f, route_id, 1, tglplay_id, 0)
        #loop in route to loop toggle
        bf.appendXConnect(f, route_id, 2, tglloop_id, 0)
        #open bang to openpanel object
        bf.appendXConnect(f, bngopen_id, 0, openpanel_id, 0)
        #play toggle to trigger object
        bf.appendXConnect(f, tglplay_id, 0, trig_id, 0)
        #trigger object to readsf~ #ind
        bf.appendXConnect(f, trig_id, 0, readsf_id, 0)
        #trigger object to open message
        bf.appendXConnect(f, trig_id, 1, msgopen_id, 0)
        #openpanel object to list prepend object
        bf.appendXConnect(f, openpanel_id, 0, list1_id, 0)
        #list prepend object to list trim object
        bf.appendXConnect(f, list1_id, 0, list2_id, 0)
        #list trim to message open
        bf.appendXConnect(f, list2_id, 0, msgopen_id, 0)
        #message open to readsf object
        bf.appendXConnect(f, msgopen_id, 0, readsf_id, 0)
        #last output of readsf~ to bang object
        bf.appendXConnect(f, readsf_id, ind, bang_id, 0)
        #bang object to float object
        bf.appendXConnect(f, bang_id, 0, float_id, 0)
        #loop toggle to float object
        bf.appendXConnect(f, tglloop_id, 0, float_id, 1)
        #float object to play toggle
        bf.appendXConnect(f, float_id, 0, tglplay_id, 0)
        #hsl vol to level msg
        bf.appendXConnect(f, hslvol_id, 0, msglevel_id, 0)
        #level msg to line~ object
        bf.appendXConnect(f, msglevel_id, 0, line_id, 0)
        #connections between readsf~ object to the various *~~
        for j in range(ind):
            bf.appendXConnect(f, readsf_id, j, mult_id+j, 0)
        #connections between line~ object to the various *~
        for j in range(ind):
            bf.appendXConnect(f, line_id, 0, mult_id+j, 1)
        #connections between the various *~ and snake~ in #ind object
        for j in range(ind):
            bf.appendXConnect(f, mult_id+j, 0, snakein_id, j)
        #snake~ in #ind object to outlet~ object
        bf.appendXConnect(f, snakein_id, 0, out_id, 0)
        '''
        f.write('#X coords 0 -1 1 1 135 150 1 50 150;\n')
    
        f.close()