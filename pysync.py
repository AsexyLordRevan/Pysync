import os
import subprocess
from pathlib import Path
from software import commands, software
import argparse
home=os.environ['HOME']
if not os.path.exists(home+"/.config/colours"):
    os.makedirs(home+"/.config/colours")
if not os.path.exists(home+"/.config/colours/colorschemes"):
    os.makedirs(home+"/.config/colours/colorschemes")
if not os.path.exists(home+"/.config/colours/themes"):
    os.makedirs(home+"/.config/colours/themes")
if not os.path.exists(home+"/.config/colours/theme.py"):
    with open(home+"/.config/colours/theme.py", "w") as f:
        print("colorscheme='default'\nwallpaper='default'", file=f)
# Get the right directory
home=os.environ['HOME']
os.chdir(home+"/.config/colours")
wallpaperdir=home+"/Documents/wallpapers/"
# Create arguments
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rofi", help="Use rofi to select theme", action="store_true")
parser.add_argument("-l", "--load", help="Reload all config files", action="store_true")
parser.add_argument("-t", "--theme", help="Apply theme instead of colors", action="store_true")
parser.add_argument("-s", "--save", help="Save current theme", action="store_true")
parser.add_argument("-c", "--colours", help="Change colours", action="store_true")
parser.add_argument("-w", "--wallpaper", help="Select and Change wallpaper Colorscheme", action="store_true")
parser.add_argument("-i", "--init", help="Initialise wallpaper on boot", action="store_true")
args=parser.parse_args()


#-----Subprograms------#

# Wallpaper
def setwallpaper(wlpr):
    os.chdir(home+"/.config/colours/")
    subprocess.call("swaybg -i "+wallpaperdir+wlpr+" &", shell=True)
    with open("theme.py") as f:
        lines = f.readlines()
        lines[1] = "wallpaper='"+wlpr+"'\n"
    with open("theme.py", "w") as f:
        f.writelines(lines)

# Colours
def setcolors(colorscheme):
    os.chdir(home+"/.config/colours/")
    #Gets colours from selected file
    subprocess.call("ln -sf ~/.config/colours/colorschemes/"+colorscheme+" ~/.config/colours/colors.py", shell=True)
    from colors import colList
    #print("Colourscheme set to", theme)
    new_colors = list(colList.values())
    new_names = list(colList.keys())
    # Create colour files
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

    # Move files
    for cursoftware in software:
        if cursoftware["format"] != "search&replace":
            symlink = str("ln -sf ~/.config/colours/" + cursoftware["format"] + " " + cursoftware["location"] + "/" + cursoftware["format"])
            os.system(symlink)

        # The hard part    
        else:
            with open(cursoftware["location"]+".template", "r+") as f:
                data = f.read()
                for i in range(len(colList)):
                    data = data.replace(new_names[i], new_colors[i])
            with open(cursoftware["location"], 'w') as f:
                f.write(data)
    with open("theme.py") as f:
        lines = f.readlines()
        lines[0] = "colorscheme='"+colorscheme+"'\n"
    with open("theme.py", "w") as f:
        f.writelines(lines)
#Set theme
def settheme(curtheme):    
    subprocess.call("cp ~/.config/colours/themes/"+curtheme+"/theme.py ~/.config/colours/theme.py", shell=True)
    for i in software:
        if software in os.listdir(home+"/.config/colours/themes/"+curtheme):
                subprocess.call("cp -r ~/.config/colours/themes/"+curtheme+"/"+i["name"]+" "+i["location"], shell=True)
    import theme
    setcolors(theme.colorscheme)
    for i in commands:
        subprocess.call(i, shell=True)
    setwallpaper(theme.wallpaper)
#-----Colours-----#
if args.colours:
    #Rofi
    if args.rofi:
        colorscheme = str(subprocess.check_output("ls ~/.config/colours/colorschemes | sed -e 's/\.py$//'| rofi -dmenu -p 'Color?'", shell=True))[2:-3]+".py"
    #Normal    
    else:
        os.chdir(home+"/.config/colours/colorschemes")
        directory_content = os.listdir(os.getenv("HOME") + "/.config/colours/colorschemes")
        files = []
        for item in directory_content:
            if os.path.isfile(item):
                files.append(item)
        
        for index in range(len(files)):
            print("%s: %s" % (str(index+1), files[index]))
        
        colorscheme = int(input("Enter the theme number: "))
        colorscheme = files[colorscheme-1]
    setcolors(colorscheme)

#-----Wallpaper-----#
if args.wallpaper:
    if args.rofi:
        roficommand= str("ls "+wallpaperdir+" |rofi -dmenu")
        wlpr = str(subprocess.check_output(roficommand, shell=True))[2:-3]
    else:
        os.chdir(wallpaperdir)
        directory_content = os.listdir()
        files = []

        for item in directory_content:
            if os.path.isfile(item):
                files.append(item)
        
        for index in range(len(files)):
            print("%s: %s" % (str(index+1), files[index]))

        wlpr=input("Wallpaper number ?")
        wlpr = files[int(wlpr)-1]
    setwallpaper(wlpr)
#-----Reload software-----#
if args.load:
    for i in commands:
        subprocess.call(i, shell=True)

#-----Save configuration-----#
if args.save:
    if args.rofi:
        input=subprocess.check_output("ls ~/.config/colours/themes | sed -e 's/\.py$//'", shell=True)
        curtheme=str(subprocess.check_output("ls ~/.config/colours/themes | sed -e 's/\.py$//'| rofi -dmenu -p 'Theme?'", shell=True))[2:-3]
        os.makedirs(home+"/.config/colours/themes/"+themename)
        subprocess.call("cp ~/.config/colours/theme.py ~/.config/colours/themes/"+themename+"/theme.py", shell=True)
        for i in software:
            subprocess.call("cp -r "+i["location"]+" ~/.config/colours/themes/"+themename+"/"+i["name"], shell=True)
    else:
        # Get the name of the theme
        themename = input("Enter the theme name: ")
        themename=themename.replace(" ", "_")
        os.makedirs(home+"/.config/colours/themes/"+themename)
        subprocess.call("cp ~/.config/colours/theme.py ~/.config/colours/themes/"+themename+"/theme.py", shell=True)
        if input("Save extra configuration files ? [y/N]")=="y":
            for i in software:
                print(i["name"])

            re = input("Choose from these [name, a(ll)]\n")
            if re in ("A", "a", "all", "All"):
                for i in software:
                    subprocess.call("cp -r "+i["location"]+" ~/.config/colours/themes/"+themename+"/"+i["name"], shell=True)
            else:   
                softwareinput=re.split(",")
                for i in software:
                    if i["name"] in software:
                        subprocess.call("cp -r "+i["location"]+" ~/.config/colours/themes/"+themename+"/"+i["name"], shell=True)

#-----Apply theme-----#
if args.theme:
    if args.rofi:
        curtheme=str(subprocess.check_output("ls ~/.config/colours/themes | sed -e 's/\.py$//'| rofi -dmenu -p 'Theme?'", shell=True))[2:-3]
    else :
        os.chdir(home+"/.config/colours/themes")
        directory_content = os.listdir(os.getenv("HOME") + "/.config/colours/themes")
        files = []
        for item in directory_content:
            files.append(item)
        
        for index in range(len(files)):
            print("%s: %s" % (str(index+1), files[index]))
        
        curtheme = int(input("Enter the theme number: "))
        curtheme = files[curtheme-1]
    settheme(curtheme)

if args.init:
    import theme
    subprocess.call("swaybg -i "+wallpaperdir+theme.wallpaper+" &", shell=True)
    