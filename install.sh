#!/bin/bash
set -e

git clone https://github.com/asexylordrevan/pysync/ ~/.config/colours
sudo pacman -S python swaybg rofi rofi-wayland
if [ -f ~/.config/.zshrc ]; then
    echo "alias sync="python ~/.config/colours/pysync.py"" >> ~/.config/.zshrc
elif [ -f ~/.bashrc ]; then
    echo "alias sync="python ~/.config/colours/pysync.py"" >> ~/.bashrc
else; echo "No shell found, the sync alias will not be added"
fi