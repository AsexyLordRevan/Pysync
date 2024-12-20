import os  
from colors import *

i=0
colours=list(colList.values())
names=list(colList.keys())
with open("coloursgtk.css", "w") as f:
	while i<= len(colours)-1:
		print("@define-color ", names[i]," #", colours[i],";", file=f, sep ='')
		i=i+1
i=0
with open("colours.css", "w") as f:
	print(":root{", file=f)
	while i<= len(colours)-1:
		print("\t","--", names[i],":#", colours[i], file=f, sep='')
		i=i+1
	print ("}", file=f)
i=0
with open("colours.conf", "w") as f:
        while i<= len(colours)-1:
                print("$", names[i],"=rgb(", colours[i],")", file=f, sep='')
                i=i+1
i=0
with open("colours.css", "w") as f:
        print(":root{", file=f)
        while i<= len(colours)-1:
                print("\t","--", names[i],":#", colours[i], ";", file=f, sep='')
                i=i+1
        print ("}", file=f)
i=0
with open("colours.rasi", "w") as f:
        print("*{", file=f)
        while i<= len(colours)-1:
                print("\t", names[i],":  #", colours[i],";", file=f, sep='')
                i=i+1
        print ("}", file=f)

