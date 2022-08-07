#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# xml 2 environment adapter

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 0:
    # print("please give file to adapt")
    exit()

file=str(sys.argv[1])
tree = ET.parse(file)
root = tree.getroot()

hop_number=0
ferment_number=0
prefix='BREW_'

for it in root.iter():
    txt = str(it.text).strip().replace('\n',' ')
    if txt:
        print(prefix+it.tag+'='+'"'+txt+'"')
    else:
        if it.tag == 'HOP':
            prefix=it.tag+str(hop_number)+'_'
            hop_number = hop_number+1
        elif it.tag == 'FERMENTABLE':
            prefix='BREW_'+it.tag+str(ferment_number)+'_'
            ferment_number = ferment_number+1
        else:
            prefix='BREW_'+it.tag+'_'
