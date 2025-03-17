#!/bin/bash
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
dunstify -u critical --icon="info" --appname="Nombre del proceso" "Título" "$1"