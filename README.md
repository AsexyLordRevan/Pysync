# Pysync
A color management tool

Pysync syncs between pieces of software using the colours provided by the user. It pulls software and its various attributes from a file named themes.py, located in the same directory as the main script (`~/.config/colours`).

# Install
Download the scripts, and move them to your colors directory or clone them with:

`git clone https://github.com/asexylordrevan/pysync`

Just so you know, if you installed Pycolor before, you'll need to remove the folder first, as Pysync covers Pycolor as well.

To easily access the sync script, add an alias to your `.bashrc` or `.zshrc`, such as `sync=bash ~/.config/colours/sync.sh `.

# Configuring
Pieces of software are stored as dictionaries, under the format

`{name, location, format}`.

`name` is primarily for readability and serves no actual purpose. `location` is the destination file for symlinked files, or the file to be used for search and replace. `format` is the file format, and can be `colours.css`, `coloursgtk.css`, `colours.rasi` and `colours.conf`. The format `search&replace` marks it foreplaceand replacing. In this case, the format must be given with the absolute bath under the format `/home/USER/example/example.txt`

Just add the relevant information for each piece of software. The default configuration supports Waybar, Hyprland, Rofi, Vencord/BetterDiscord, and Kitty.
