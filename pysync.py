import os
from theme import *
from pycolor import *
exec(open("pycolor.py").read())
i=0

TEMPLATE = """#!/bin/bash
cd ~/.config/colours
python pycolor.py
cd ~/
{links}
echo "Colours synched"
{commands}
echo "Software reloaded"
cd ~/
"""

links = ""
while i <= len(software) - 1:
    cur = software[i]
    links += "ln -sf ~/.config/colours/{format} {location}\n".format(format=cur["format"], location=cur["location"])
    i += 1

commands_str = "\n".join(commands)

with open("sync2.sh", "w") as f:
    f.write(TEMPLATE.format(links=links, commands=commands_str))
