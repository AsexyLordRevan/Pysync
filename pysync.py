import importlib
import os
from json import load

# load data.json
with open('data.json') as f:
      data = load(f)

colList = data["color-schemes"]
order = data["order"]
software = data["theme"]["software"]
commands = data["theme"]["commands"]
home=os.getenv("HOME")

folder=home+ "/.config/colours"
os.chdir(folder)
print (order)
theme=int(input("theme number?"))-1
newcolours=list(colList[theme].values())
newnames=list(colList[theme].keys())

#Make file types
with open("coloursgtk.css", "w") as f:
	for i in range(len(newcolours)):
		print("@define-color ", newnames[i]," #", newcolours[i],";", file=f, sep ='')
with open("colours.css", "w") as f:
	print(":root{", file=f)
	for i in range(len(newcolours)):
		print("\t","--", newnames[i],":#", newcolours[i], file=f, sep='')
	print ("}", file=f)
with open("colours.conf", "w") as f:
        for i in range(len(newcolours)):
                print("$", newnames[i],"=rgb(", newcolours[i],")", file=f, sep='')
with open("colours.css", "w") as f:
        print(":root{", file=f)
        for i in range(len(newcolours)):
                print("\t","--", newnames[i],":#", newcolours[i], ";", file=f, sep='')
        print ("}", file=f)
with open("colours.rasi", "w") as f:
        print("*{", file=f)
        for i in range(len(newcolours)):
                print("\t", newnames[i],":  #", newcolours[i],";", file=f, sep='')
        print ("}", file=f)

#Move files
for cursoftware in software:
    if cursoftware["format"] != "search&replace":
        symlink=str("ln -sf ~/.config/colours/" + cursoftware["format"] + " " + cursoftware["location"]+ "/"+cursoftware["format"])
        os.system(symlink)
    
#The hard part    
    else:
        with open(cursoftware["location"], "r+") as f:
            data = f.read() 
            for j in range(len(colList)):
                searchdict=colList[j]
                oldcolours=list(colList[j].values())
                for i in range(len(colList[0])):
                    print (list[i])
                    data=data.replace(oldcolours[i],newcolours[i])
        with open(cursoftware["location"], 'w') as f: 
            f.write(data)
for curcommand in commands:
    os.system(curcommand)
