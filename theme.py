software = [
{"name":"waybar", "location":"~/.config/waybar", "format":"coloursgtk.css"},
{"name":"hyprland", "location":"~/.config/hypr", "format":"colours.conf"},
{"name":"rofi", "location":"~/.config/rofi", "format":"colours.rasi"},
{"name":"betterdiscord", "location":"~/.config/wlogout", "format":"colours.css"}
]

commands = [
    "killall waybar",
    "waybar &",
    "makoctl reload",
]
