#!/usr/bin/python
# Script for Opping a player

import sys
import json
from pathlib import Path
import argparse

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

# Set up the argument parser
parser = argparse.ArgumentParser(description="OP a player.")
parser.add_argument("name", type=str, help="The player\'s username")
parser.add_argument("level", type=int, default=4, nargs="?", help="The permission level for the player.")
args = parser.parse_args()

# Collect the relevant args
name = args.name
level = args.level

# Create variable to store matching player
matching_player = {}
# Open the usercache json file
with open(ROOT_DIR / "usercache.json") as file:
    try:
        # Load the file contents as a python list
        players = json.load(file)
        # Iterate through the list of dictionaries and see if any of their values
        # contains the player name we are looking for. Once found, then copy the corresponding
        # dictionary of user information. If none can be found
        # then the exception gets triggered.
        matching_player = [p for p in players if p.get("name") == name][0]
        # Delete an uneeded key from the player's dictionary
        matching_player.pop("expiresOn", None)
        # Add the permission level for the op player
        matching_player["level"] = level

    except IndexError:
        print("Matching player not found in cache. Exiting command...")

    except json.decoder.JSONDecodeError as e:
        print(f"Error: Could not parse json file. {e}")


# Create variable to store op players
op_players = []
# Open the ops json file
with open(ROOT_DIR / "ops.json", "r+") as file:
    try:
        # Load the player list
        op_players = json.load(file)
        # Check for a matching player. If the player has already been opped, then
        # this will enter the exception

        # If there are players, check if there is a duplicate
        possible_matching_player = [p for p in op_players if p.get("name") == name]
        if op_players and possible_matching_player[0]:
            print("Player has already been opped. Exiting command...")
        else:
            # Add the new player to the op list and write to the file
            op_players.append(matching_player)
            file.seek(0)
            file.truncate(0)
            file.write(json.dumps(op_players))

    except json.decoder.JSONDecodeError as e:
        print(f"Error: Could not parse json file. {e}")