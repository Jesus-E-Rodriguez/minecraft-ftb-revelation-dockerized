#!/bin/bash

echo "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula)." > minecraft/eula.txt && \
echo "$(date)" >> minecraft/eula.txt && \
echo "eula=TRUE" >> minecraft/eula.txt