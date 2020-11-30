#!/bin/bash
echo "Do you agree to the Mojang EULA available at https://account.mojang.com/documents/minecraft_eula ?"
EULA=`read  -n 1 -p "[y/n] "`
if [ "$EULA" = "y" ]; then
    echo "eula=true" > eula.txt
fi
java -server -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -Xmx6144M -Xms4608M -jar forge-1.12.2-14.23.5.2846-universal.jar nogui