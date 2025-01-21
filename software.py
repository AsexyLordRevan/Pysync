software = [
{"name":"waybar", "location":"~/.config/waybar", "format":"coloursgtk.css"},
{"name":"hyprland", "location":"~/.config/hypr", "format":"colours.conf"},
{"name":"rofi", "location":"~/.config/rofi", "format":"colours.rasi"},
{"name":"betterdiscord", "location":"/home/revan/.config/BetterDiscord/themes/asexy.theme.css", "format":"search&replace"},
{"name":"kitty", "location":"/home/revan/.config/kitty/kitty.conf", "format":"search&replace"},
{"name":"mako", "location":"/home/revan/.config/mako/config", "format":"search&replace"}
]


commands = [
    "makoctl reload",
    "killall waybar",
    "waybar&",
]

