#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("must pass small list first to merge into second file")
    sys.exit()
val = {}
for line in open(sys.argv[1]):
    if line.find("=") > -1:
        name = line.split("=")[0]
        val[name] = line.split("=")[1].rstrip()
        
val2 = {}
for line in open(sys.argv[2]):
    if line.find("=") > -1:
        name = line.split("=")[0]
        val2[name] = line.split("=")[1].rstrip()
        if (name in val):
            if val[name] == line.split("=")[1].rstrip():
                print('same,%s=%s'%(name,val[name]))
            else:
                print('changed,%s=1->%s,2->%s # updated from #1'%(name,val[name],val2[name]))
        else:
            print('missing in 1->,%s'% line.rstrip())
    else:
        print line.rstrip() 

# now print out the values in first config missing in second
for config in val:
    if not config in val2:
        print('missing in 2->,%s=%s'%(config,val[config]))


# vim: ts=8 expandtab softtabstop=4 shiftwidth=4
