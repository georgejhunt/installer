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
    	    if val[name] == line.split("=")[1]:
           	print("%s=%s"%(name,val[name]))
	    else:
           	print("%s=%s # updated from olpc"%(name,val[name]))
        else:
            print("%s"% line.rstrip())
    else:
        print line.rstrip() 

# now print out the values in first config missing in second
for config in val:
    if not config in val2:
        print("%s=%s # additional config from olpc defconfig"%(config,val[config]))



# vim: ts=4 expandtab	    
