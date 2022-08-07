#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xml parser tests
https://docs.python.org/3.8/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
https://www.youtube.com/watch?v=j0xr0-IAqyk
https://www.youtube.com/watch?v=bWfAD7wAfOI
"""
import xml.etree.ElementTree as ET

from inspect import getmembers, isclass, isfunction

# print ("classes in ET module")
# for (name, member) in getmembers(ET, isclass):
#   if not name.startswith("_"):
#       print(" "+name)

# print ("functions in ET module")
# for (name, member) in getmembers(ET, isfunction):
#   if not name.startswith("_"):
#       print(" "+name)

# tree = ET.parse('examples/docs.xml')
# tree = ET.parse('examples/punk-ipa-2007-2010.xml')
tree = ET.parse('examples/kajaani-22-19.xml')
root = tree.getroot()



hop_number=0
ferment_number=0
prefix="DATA_"
for it in root.iter():
    txt = str(it.text).strip().replace('\n',' ')
    if txt:
        print(prefix+it.tag+'='+'"'+txt+'"')
    else:
        if it.tag == 'HOP':
            prefix='BREW_'+it.tag+str(hop_number)+'_'
            hop_number = hop_number+1
        elif it.tag == 'FERMENTABLE':
            prefix='BREW_'+it.tag+str(ferment_number)+'_'
            ferment_number = ferment_number+1
        else:
            prefix='BREW_'+it.tag+'_'



# get whole file as string
# print(ET.tostring(root))

# dump whole shit as it is
# ET.dump(tree)

# for x in root.findall('.'):
#   print(x.tag)
#   # style =x.find('IPA').text
#   # print(style)

# for hop in root.findall(".//HOP"):
#   print(hop.tag, hop.text)


# # get root child object
# for child in root:
#   print(child.tag, child.attrib, child.text)

# print (root[0][1].text)
# for i in root[0]:
#     print(i.tag,i.text)
