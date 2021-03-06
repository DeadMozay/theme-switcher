#!/usr/bin/bash

time=$(date +"%H")

# List and set your gnome-terminal profiles:
# gsettings get org.gnome.Terminal.ProfilesList list
terminal_dark='88173e30-df6e-4442-b012-4e1119c7385f'
terminal_light='b4bd0ffd-117e-4778-82ef-da4ccdf4cb2c'
night=$(gsettings get com.github.Latesil.theme-switcher nighttime)
daytime=$(gsettings get com.github.Latesil.theme-switcher daytime)
night_wallpapers=$(gsettings get com.github.Latesil.theme-switcher path-to-night-wallpaper)
day_wallpapers=$(gsettings get com.github.Latesil.theme-switcher path-to-day-wallpaper)
light_theme=$(gsettings get com.github.Latesil.theme-switcher light-theme)
dark_theme=$(gsettings get com.github.Latesil.theme-switcher dark-theme)

if [[ ${time#0} -ge ${night#0} ]] || [[ ${time#0} -le ${daytime#0} ]]; then
    gsettings set org.gnome.desktop.interface gtk-theme "$dark_theme"
    if [ "$night_wallpapers" != "''" ]; then
        gsettings set org.gnome.desktop.background picture-uri "$night_wallpapers"
    fi
    gsettings set org.gnome.Terminal.ProfilesList default $terminal_dark
    exit 0
else
    gsettings set org.gnome.desktop.interface gtk-theme "$light_theme"
    if [ "$day_wallpapers" != "''" ]; then
        gsettings set org.gnome.desktop.background picture-uri "$day_wallpapers"
    fi
    gsettings set org.gnome.Terminal.ProfilesList default $terminal_light
    exit 0
fi
