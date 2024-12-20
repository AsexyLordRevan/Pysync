import os
from theme import *
from pycolor import *
exec(open("pycolor.py").read())
i=0
with open("../../.sync.sh", "w") as f:
    print('#!/bin/bash\ncd ~/.config/colours\npython pycolor.py\ncd ~/', file=f, sep='')
    while i<= len(software)-1:
        cur=software[i]
        print("ln -sf ", "~/.config/colours/",cur["format"]," ",cur["location"],sep='',file=f)
        i=i+1
    print('echo "Colours synched"\n',file=f)
    i=0
    while i<= len(commands)-1:
        print(commands[i],file=f)
        i=i+1
    print('\necho "Software reloaded"\ncd ~/', file=f,sep='')
