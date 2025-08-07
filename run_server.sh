#!/bin/bash
mkdir -p ~/webserver/admin
echo "Welcome to /admin" > ~/webserver/admin/index.html
cd ~/webserver
sudo python3 -m http.server 80
