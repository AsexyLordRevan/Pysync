software = [
{"name":"waybar", "location":"~/.config/waybar", "format":"coloursgtk.css"},
{"name":"hyprland", "location":"~/.config/hypr", "format":"colours.conf"},
{"name":"rofi", "location":"~/.config/rofi", "format":"colours.rasi"},
{"name":"betterdiscord", "location":"/home/USER/.config/Vencord/themes/rose-pine.theme.css", "format":"search&replace"},
{"name":"kitty", "location":"/home/USER/.config/kitty/kitty.conf", "format":"search&replace"},
]

commands = [
    "killall waybar",
    "killall hyprpaper"
    "hyprpaper&"
    "waybar &",
    "makoctl reload",
]
