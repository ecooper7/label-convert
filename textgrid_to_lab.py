#!/usr/bin/python

import sys
import re

usage = 'Usage: ./textgrid_to_lab.py input.TextGrid output.lab'

if len(sys.argv) != 3:
    print usage
    exit()

ifname = sys.argv[1]
ofname = sys.argv[2]

# boilerplate
outf = open(ofname, 'w')
outf.write('separator ;\n')
outf.write('nfields 1\n')
outf.write('#\n')

# intervals
inf = open(ifname)
start_of_intervals = False
start = ''
end = ''
text = ''
for line in inf:
    l = line.strip()
    if not start_of_intervals:
        if re.search('^intervals', l):
            start_of_intervals = True
        else:
            continue
    if re.search('^xmin', l):
        start = float(l.strip('xmin = '))
    elif re.search('^xmax', l):
        end = l.strip('xmax = ')
    elif re.search('^text', l):  # end of interval; write info
        text = l.strip('text = ').strip('"') 
        outf.write('\t %.5f' % float(end) + ' 26 \t' + text + '\n')
    else:
        continue

outf.close()
inf.close()
