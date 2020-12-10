# FTB Revelation Dockerized Version
[![minecraft](https://img.shields.io/badge/minecraft-1.12.2-green.svg)](https://www.minecraft.net/en-us)
[![ftb](https://img.shields.io/badge/ftb-3.4.0-orange.svg)](https://www.feed-the-beast.com/)
[![forgejar](https://img.shields.io/badge/forgejar-1.12.2.14.23.5.28.46-purple.svg)](https://www.feed-the-beast.com/modpack/ftb_revelation)


## What is this for?
This project allows you to spin up a Minecraft FTB Revelation server with one simple command:

    $ ./start.sh

The project is also compatible with the Raspberry Pi.
    
## Table of contents
- [Quick Start](#quick-start)
- [Deployment Instructions](#deployment-instructions)
- [Client Instructions](#client-instructions)
- [Additional Notes](#additional-notes)
- [Raspberry Pi Instructions](#raspberry-pi-instructions)

## Quick start
You can do either of the following:
- Download the repo.
- Clone the repo: `https://github.com/Jesus-E-Rodriguez/minecraft-ftb-revelation-dockerized.git`

`Note:` You will need [Docker](https://www.docker.com/products/docker-desktop) for this project. 
What is Docker and why should you download it? Docker allows for standardization of application 
deployments across various types of operating systems. In short, for you, it simplifies the 
process of deploying this server to a single command. If that still isn't enough to convince 
you, then check out their [explanation](https://www.docker.com/resources/what-container).

## Deployment Instructions
Make sure Docker is running. Once you have the repo in your system open up a terminal or 
command prompt (Mac or Windows respectively) and navigate to the proper folder. Once there
run the following command inside the folder (note: the `$` indicates this is a console 
command. It does not need to be copied):

    $ ./start.sh

## Client Instructions
Download [feed the beast](https://www.feed-the-beast.com/). Once downloaded, open the app
and click on the home tab. Once there click on `Featured Packs` and download `FTB Revelation`.

`Warning:` You may not have enough ram for the mod pack. In order to increase ram,
click the play button on `FTB Revelation`. When the Minecraft launcher initializes, 
click `Installations` tab. Hover over `FTB Revelation` and click on `...` and chose 
`Edit` from the dropdown. The click the `More Options` at the bottom. You can 
change `-Xmx4096M` to `-Xmx6144M` or to `-Xmx8192M` and click `Save`. This changes the ram
from 4GB to 6GB or 8GB respectfully. Remember, you can only make this change
if your computer has the actual amount of available ram you specified.

For quality shaders, first download [Optifine](https://optifine.net/downloads).
Click on `Show all versions` and download the version that matches your Minecraft version.
I.e, if your Minecraft version is 1.12.2, then choose the same version.

Once downloaded, open up FTB and hover over `FTB Revelation` and click the `...More`. Once there click the
`Open Folder` button. Open the `mods` folder, and place the downloaded Optifine jar file in there. 
If you need more step-by-step instructions, please check [here](https://ftb.gamepedia.com/Shaders_(programs)).

The best recommended shaders are [SEUS Renewed](https://www.sonicether.com/seus/).
Once downloaded, open up FTB and hover over `FTB Revelation` and click the `...More`. Once there click the 
`Open Folder` button. Look for the `shaderpacks` folder and move the zipped SEUS file there. 
Then launch FTB Minecraft. Once opened, click `Options` and then `Video Settings` and then `Shaders...`
and click on the `SEUS-Renewed-v1.0.1.zip`. Depending on your ram specifications, your game
make take some time to apply the shaders. If instead it crashes, you may not have enough 
ram available. If that is the case please read above to learn how to allow more ram to your client instance.

If you are running the client in the same host, then you can connect to the server with the following
ip `0`. Otherwise, you will need to figure out the ip of the server running instance.

## Additional Notes

`Warning:` by using this project, you automatically agree to the [EULA](https://account.mojang.com/documents/minecraft_eula). Please make sure you
understand what it is and how it affects you.

`Note:` Remember this is only the server you connect to. You will also need to download the client
which then connects to this server. Instructions for that are outlined above.

What mods are included here? All the regular FTB Revelation mods, plus Gliby's Voice Chat Reloaded.
Note, you will need to add it to your client mod folder as well. If you'd like to add more mods,
just add them to the `minecraft/mod` folder, but keep in mind that they need to match what is in
your client mod folder.

Once the container is running, you can op yourself with the following command
(Note that players you op must have logged into the server at least once, including yourself):

    $ docker-compose run minecraft python3 management/op.py TheNameOfYourPlayer
    $ docker restart minecraft

## Raspberry Pi Instructions

`Note:` This will not work on any 32-bit OS such as Raspian. This is simply due to the way Java 
allocates memory. As such, you will need to run it on an Ubuntu 64-bit OS. The version that was used for
this project was Ubuntu Server 20.04.1 LTS. As stated before, you will need Docker installed on the system.

Git clone this project in a directory of your choice, and run:

    $ ./start.sh

If you are installing this alongside an [IOTstack](https://github.com/SensorsIot/IOTstack), I have some recommendations.
You should install this project in the `volumes` directory like so:

    $ cd ~/IOTstack/volumes
    $ git clone https://github.com/Jesus-E-Rodriguez/minecraft-ftb-revelation-dockerized.git minecraft

The reason is that the minecraft directory is already bound to the minecraft directory of the container image, essentially
acting as a volume mapping. Therefore, if you want to back up your minecraft world, you should backup the minecraft
directory.

Make sure the EULA is created and signed with:

    $ cd minecraft
    $ ./eula.sh
    
Then move up to the directory above volumes:

    $ cd ~/IOTstack
    $ cd ls

This directory should contain the `docker-compose.yml` file, you can edit it with the following command:

    $ sudo vi docker-compose.yml

Press `i` to edit the file and paste (note this should be pasted in the services column after any other services. The
order doesn't matter, but the alignment between different services does):

```yaml
  minecraft:
    build:
      context: ./volumes/minecraft
      dockerfile: ./compose/minecraft/Dockerfile
    image: minecraft_server
    restart: unless-stopped
    container_name: minecraft
    env_file:
      - ./volumes/minecraft/.envs/.minecraft/.jvm
    volumes:
      - ./volumes/minecraft/minecraft:/minecraft:z
    ports:
      - "25565:25565"
    command: /start
```

Then press the `esc` button and type `:wq`. Afterwards you can run the container with the typical docker commands. Such as:

    $ docker-compose up -d