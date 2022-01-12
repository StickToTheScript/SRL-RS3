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

## Troubleshooting
### Duplicate declaration "Tesseract_Create"
When attempting to compile or run a script and you encounter `Duplicate declaration "Tesseract_Create"`, simply remove any instance of `{$i Tesseract/Tesseract.simba}` from your script. 

This is because `Tesseract.simba` is already included in the library.