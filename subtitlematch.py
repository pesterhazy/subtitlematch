#!/usr/bin/env python

import re, getopt, os
from sys import argv, exit

really_act = False

opts, args = getopt.getopt(argv[1:], "", ["really-act"])

for o, a in opts:
    if o == "--really-act":
        really_act = True

count = len(args)

if count == 0:
    print 'Syntax: subtitlematch.py [--really-act] *.avi *.srt'
    exit(1)

if count % 2 != 0:
    print 'Even number of arguments expected.'
    exit(1)

a = args[0:count/2]
b = args[count/2:count]

for i in range(0,count/2):
    ext = re.search('\.\w*$',b[i]).group(0)
    new = re.sub('\.\w*$',ext,a[i])
    if really_act:
        print "Moving: '%s' => '%s'" % (b[i], new)
        os.rename(b[i], new)
    else:
        print "'%s' => '%s'" % (b[i], new)
