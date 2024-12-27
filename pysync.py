import importlib
import os
from json import load

# usage: FMT_SYMLINK.format("file", "folder")
FMT_SYMLINK = "ln -sf ~/.config/colours/{0} {1}/{0}"
# load data.json
with open('data.json') as f:
      data = load(f)

colList = data["color-schemes"]
order = list(data["color-schemes"].keys())
software = data["theme"]["software"]
commands = data["theme"]["commands"]
home=os.getenv("HOME")

folder=home+ "/.config/colours"
os.chdir(folder)
print (order)
theme=colList[order[int(input("theme number?"))-1]]   
newcolours=theme.values()
newnames=theme.keys()


#Make file types
with open("coloursgtk.css", "w") as f:
        fc = ""
        for i in range(len(newcolours)):
                fc += f"@define-color {newnames[i]} #{newcolours[i]};\n"

        f.write(fc)

with open("colours.css", "w") as f:
        fc = ":root {\n"
        for i in range(len(newcolours)):
                fc += f"\t--{newnames[i]}: #{newcolours[i]};\n"
        
        fc += "}"
        f.write(fc)

with open("colours.conf", "w") as f:
        fc = ""
        for i in range(len(newcolours)):
                fc += f"${newnames[i]}=rgb({newcolours[i]})\n"
        f.write(fc)
        
with open("colours.css", "w") as f:
        fc = ":root {\n"
        for i in range(len(newcolours)):
                fc += f"\t--{newnames[i]}: #{newcolours[i]};\n"
        fc += "}"
        f.write(fc)

with open("colours.rasi", "w") as f:
        fc = "*{\n"
        for i in range(len(newcolours)):
                fc += f"\t{newnames[i]}: #{newcolours[i]};\n"
        fc += "}"
        f.write(fc)

#Move files
for cursoftware in software:
    if cursoftware["format"] != "search&replace":
        symlink = FMT_SYMLINK.format(cursoftware["format"], cursoftware["location"])
        os.system(symlink)
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
