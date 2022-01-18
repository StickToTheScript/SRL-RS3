# SRL-RS3

*This project is still a work in progress. You should expect that scripts break between updates.*

## Overview

SRL is a scripting library that provides an API for creating scripts in Simba for the game RuneScape. SRL is written in a Pascal-like scripting language using the Lape interpreter and the Simba IDE. 

Everything you need to know about SRL and Simba can be found on the [SRL Forums](https://villavu.com/forum/) or in the [Discord](https://discord.gg/RSXyB8E).

## Setup
In order to start using this library:
1. Download the latest release of Simba from [ollydev/Simba](https://github.com/ollydev/Simba/releases/tag/autobuild-simba1400)
2. Using the `Simba Package Manager`, download the latest release of this repo (*Note: There will be no releases until the library is functional. Until then, select the `master` option*)).

> All required plugins are included in the repo already.

## Broken Functions
Below is a list of broken interface functions:
- Action Bar
  - isLocked
  - clear
  - getAbilityCooldown
- Backpack
  - TRSTabBackpack.getMoneyPouchAmount
  - TRSTabBackpack.isLocked
- Bankscreen
  - All Functions
- Chatbox
  - getTextOnLine
- Game Tab
  - All Functions
- Lobby
  - getCurrentTab
  - openTab
- Loot Screen
  - All Functions
- Main Screen
  - SetZoom
  - isPlayerAnimating
- Metrics
  - All Functions
- Minimap
  - getDots
  - isFlagPresent
  - enableRest
  - getRunEnergy
  - isRunEnabled
- Stats
  - All Functions

## Untested Functions
Below is a list of interface functions that I have not had the opportunity to test yet:
- Beast of Burden
- Collect Box
- Conversation Box
- Deposit Box 
- Hero Screen
- Pin Screen
- Power Screen
- Production
- Progress Screen
- Target Info
- Tool Screen
- Trade Screen
- Worlds

## Troubleshooting
### `Duplicate declaration "Tesseract_Create"`
When attempting to compile or run a script and you encounter `Duplicate declaration "Tesseract_Create"`, simply remove any instance of `{$i Tesseract/Tesseract.simba}` from your script. 

This is because `Tesseract.simba` is already included in the library.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FStickToTheScript%2FSRL-RS3&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)