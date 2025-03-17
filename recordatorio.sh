#!/bin/bash
export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
dunstify -u critical --icon="info" --appname="Nombre del proceso" "Título" "$1"

zenity --info --title="Mensaje informativo" --text="$1"