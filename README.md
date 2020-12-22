# Battilde Client

[Battilde server](https://github.com/jmdejong/battilde)

A multiplayer top-down terminal shooter.

## About Battilde

Battilde is a multiplayer co-op shooter game that is played in the terminal.

The intended use is to play this servers with a shared login (through ssh) but it can be played in other contexts too.

Players fight of progressively stronger waves of monsters.

You start in the sanctuary, an area that heals you.
If your health is full you can leave the sanctuary.
You can not come back through the gates after leaving.
If you die you respawn in the sanctuary again.

There are 4 several pillars around the sanctuary.
Some monsters will attack these.
The game ends when all pillars are destroyed.

## Installation/Running

_a better installation with pip will be added in the future_

The asciifarm client requires [ratuil](https://github.com/jmdejong/ratuil) to run.
To install ratuil run:

    python3 -m pip install --user ratuil

To install the client download or clone this repository.
Make sure the current working directory is the root folder of the repository.
Then run `python3 -m battildeclient`.

## Controls

The controls can be customised by giving a new keybindings file.
Assuming that you haven't done this the most important controls are as follows:

- `wasd`, `hjkl` or arrow keys: move around
- `WASD` or `HJKL`: attack in the corresponding direction
- `f`, `F` or spacebar: attack in the last used direction
- `pageup`: scroll the chat messages up
- `pagedown`: scroll the chat messages down
- `t` or `enter`: send a message or command in the chat. Commands start with `/`
- `/`: send a message or command in the chat and fill in a `/` already. This is the same as first pressing `t` and then pressing `/`

When entering a message or command `enter` will send the message / execute the command, `escape` will trow away the message and `tab` will take you back to the game input, but leave the message so you can continue it the next time you start send a message/command.


## Command line arguments

Run `python3 -m asciifarmclient --help` to see the list of command line arguments.

	$ python3 -m battildeclient --help
	usage: __main__.py [-h] [-n NAME] [-a ADDRESS] [-s {abstract,unix,inet}] [-t SPRITE] [-k KEYBINDINGS] [-c CHARACTERS] [-o LOGFILE] [--reset-style]
					[--blink-bright-background] [-b]

	The client to Battilde. Run this to connect to to the server.

	optional arguments:
	-h, --help            show this help message and exit
	-n NAME, --name NAME  Your player name (must be unique!). Defaults to username. All characters must be unicode letters, numbers or connection puctuation. The
							maximum size of a name is 256 bytes when encoded as utf8
	-a ADDRESS, --address ADDRESS
							The address of the socket. When the socket type is 'abstract' this is just a name. When it is 'unix' this is a filename. When it is 'inet' is
							should be in the format 'address:port', eg 'localhost:8080'. Defaults depends on the socket type
	-s {abstract,unix,inet}, --socket {abstract,unix,inet}
							the socket type. 'unix' is unix domain sockets, 'abstract' is abstract unix domain sockets and 'inet' is inet sockets.
	-t SPRITE, --sprite SPRITE
							Player sprite. Format: <colourcode>-<letter>. Letter must be lowercase. The colourcode can be: 'r', 'g', 'b', 'c', 'y', 'm', any of the
							previous prefixed by 'l' or 'a'
	-k KEYBINDINGS, --keybindings KEYBINDINGS
							The file with the keybinding configuration. This file is a JSON file.
	-c CHARACTERS, --characters CHARACTERS
							The file with the character mappings for the graphics. If it is either of these names: ['default', 'halfwidth', 'hw', 'fullwidth', 'fw',
							'emoji'] it will be loaded from the charmaps directory.
	-o LOGFILE, --logfile LOGFILE
							All game messages will be written to this file.
	--reset-style         Reset the style when it changes. Useful on some terminals
	--blink-bright-background
							Use blink attribute to make background brighter. Useful for terminals that don't have bright backgrounds normally. Implies --reset-style
	-b, --nocolours, --nocolors
							disable colours.

