#!/usr/bin/env python3

import sys

word = (len(sys.argv)-1)

if word <= 0:
    print('None')
else :
    print(sys.argv[1])