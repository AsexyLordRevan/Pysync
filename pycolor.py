import importlib
from colors import *

def generate_theme_files(theme_key):
        i = 0
        theme_module = importlib.import_module('colors')
        theme = getattr(theme_module, theme_key)
        colours = list(theme.values())
        names = list(theme.keys())

        with open("coloursgtk.css", "w") as f:
                while i <= len(colours) - 1:
                        print("@define-color ", names[i], " #", colours[i], ";", file=f, sep='')
                        i += 1

        i = 0
        with open("colours.css", "w") as f:
                print(":root{", file=f)
                while i <= len(colours) - 1:
                        print("\t", "--", names[i], ":#", colours[i], ";", file=f, sep='')
                        i += 1
                print("}", file=f)

        i = 0
        with open("colours.conf", "w") as f:
                while i <= len(colours) - 1:
                        print("$", names[i], "=rgb(", colours[i], ")", file=f, sep='')
                        i += 1

        i = 0
        with open("colours.rasi", "w") as f:
                print("*{", file=f)
                while i <= len(colours) - 1:
                        print("\t", names[i], ":  #", colours[i], ";", file=f, sep='')
                        i += 1
                print("}", file=f)
