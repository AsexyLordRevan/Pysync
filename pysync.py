import os
from theme import *
from pycolor import *
import argparse


TEMPLATE = """#!/bin/bash
# Generated by pysync.py
# https://github.com/
cd ~/.config/colours
python pycolor.py
cd ~/
{links}
echo "Colours synched"
{commands}
echo "Software reloaded"
cd ~/
"""

parser = argparse.ArgumentParser(prog="PySync", description="Generate a script to sync colours")
parser.add_argument("-t", "--theme", help="The theme to use")
parser.add_argument("-o", "--output", help="The output file (shell script)", default="sync.sh")
args = parser.parse_args()
print("Using theme: ", args.theme)
links = ""
for cur in software:
    links += "ln -sf ~/.config/colours/{format} {location}\n".format(format=cur["format"], location=cur["location"])

commands_str = "\n".join(commands)

with open(args.output, "w") as f:
    f.write(TEMPLATE.format(links=links, commands=commands_str))

generate_theme_files(args.theme)