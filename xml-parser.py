#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
parser = ET.parse('examples/punk-ipa-2007-2010.xml')



print(parser.tag)