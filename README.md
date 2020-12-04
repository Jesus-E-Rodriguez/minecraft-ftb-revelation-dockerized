# FTB Revelation Dockerized Version


## What is this for?
This project allows you to spin up a FTB Revelation server with one simple command:

    $ ./start.sh
    
## Table of contents

- [Quick Start](#quick-start)
- [Deploy Steps](#local-deploy-steps)
- [Additional Notes](#additional-notes)

## Quick start

- Download the repo.
- Clone the repo: `https://github.com/Jesus-E-Rodriguez/minecraft-ftb-revelation-dockerized.git`

`Note:` You will need [Docker](https://www.docker.com/products/docker-desktop) for this project. What is docker and why should I download it?
Docker allows for standardization of application deployments across various types of operation systems. And for you, it simplifies the 
process of deploying this server to a single command. If that still isn't enough to convince you, then check out their [explanation](https://www.docker.com/resources/what-container).

Once you have the repo in your system and have downloaded Docker, open up a terminal or command prompt. Navigate to the proper folder, and
run the following command (note: the `$` indicates this is a console command. It does not need to be copied):

    $ ./start.sh

## Additional Notes

`Warning:` by using this project, you are automatically agreeing to the [EULA](https://account.mojang.com/documents/minecraft_eula). Please make sure you 
understand what it is and how it affects you.

What mods are included here? All the regular FTB Revelation mods, plus Gliby's Voice Chat Reloaded. Note, you will need to add If you'd like to add more mods, 
just add them to the `minecraft/mod` folder.

You will also need to download the client to connect to the server. Instructions for that are outlined below.

Once the container is running, you can op yourself with the following command (Note that players you op must have logged into
the server at least once, including yourself.):

    $ docker-compose run minecraft python3 management/op.py TheNameOfYourPlayer

### Client Instructions

Download [feed the beast](https://www.feed-the-beast.com/). Once downloaded, open the app
and click on the home tab. Once there click on `Featured Packs` and download `FTB Revelation`.

For quality shaders, first download [Optifine](https://optifine.net/downloads). 
Click on `Show all versions` and download the version that matches your Minecraft version. 
I.e, if your Minecraft version is 1.12.2, then choose the same version.

Once downloaded, open up FTB and hover over `FTB Revelation` and click the `...More`. Once there click the 
`Open Folder` button. Open the `mods` folder, and place the downloaded Optifine jar file in there. If you need more step
by step instructions, please check [here](https://ftb.gamepedia.com/Shaders_(programs)).

`Warning:` You may not have enough ram for the mod pack. In order to increase ram,
click the play button on `FTB Revelation`. When the Minecraft launcher initializes, click `Installations` tab.
Hover over `FTB Revelation` and click on `...` and chose `Edit` from the dropdown. The click the `More Options`
at the bottom. You can change `-Xmx4096M` to `-Xmx6144M` or to `-Xmx8192M` and click `Save`. This changes the ram
from 4GB to 6GB or 8GB respectfully. Remember, you can only make this change
if your computer has the actual amount of available ram you specified.

Shaders can make your game look better. The best recommended shaders are [SEUS Renewed](https://www.sonicether.com/seus/).
Once downloaded, open up FTB and hover over `FTB Revelation` and click the `...More`. Once there click the 
`Open Folder` button. Look for the `shaderpacks` folder and move the zipped SEUS file there. Then launch FTB Minecraft. Once opened,
click `Options` and then `Video Settings` and then `Shaders` and click on the `SEUS`. Depending on your ram specifications, your game
make take some time to apply the shaders. If instead it crashes, you may not have enough ram available.