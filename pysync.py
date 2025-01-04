import os
import subprocess
from pathlib import Path
from theme import *
from colors import *

#Get the right directory
HOME = Path.home()
CONFIG_FOLDER = HOME / ".config/colours"
CONFIG_FOLDER.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists
os.chdir(CONFIG_FOLDER)

rofi =True
if rofi == False:
        for i in order:
                print(order.index(i)+1, i)
        theme=int(input("theme number?"))-1
        if theme < 0 or theme >= len(order):
            raise ValueError("Invalid theme number.")
       
else:
        roficommand='echo -e "'
        for i in order:
                roficommand= roficommand+str(order.index(i)+1)+" "+str(i)+"\n"
        roficommand=roficommand+'"|rofi -dmenu'
        theme=str(subprocess.check_output(roficommand,shell=True))
        print(theme)
        theme=int(theme[2])-1
print(theme)
new_colors=list(colList[theme].values())
new_names=list(colList[theme].keys())

#Make file types
with open("coloursgtk.css", "w") as f:
	for i in range(len(new_colors)):
		print("@define-color ", new_names[i]," #", new_colors[i],";", file=f, sep ='')
with open("colours.css", "w") as f:
	print(":root{", file=f)
	for i in range(len(new_colors)):
		print("\t","--", new_names[i],":#", new_colors[i], file=f, sep='')
	print ("}", file=f)
with open("colours.conf", "w") as f:
        for i in range(len(new_colors)):
                print("$", new_names[i],"=rgb(", new_colors[i],")", file=f, sep='')
with open("colours.css", "w") as f:
        print(":root{", file=f)
        for i in range(len(new_colors)):
                print("\t","--", new_names[i],":#", new_colors[i], ";", file=f, sep='')
        print ("}", file=f)
with open("colours.rasi", "w") as f:
        print("*{", file=f)
        for i in range(len(new_colors)):
                print("\t", new_names[i],":  #", new_colors[i],";", file=f, sep='')
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
                    data=data.replace(oldcolours[i],new_colors[i])
        with open(cursoftware["location"], 'w') as f: 
            f.write(data)
for command in commands:
    subprocess.call(command,shell=True,text=False)

print ("Sync Done")
