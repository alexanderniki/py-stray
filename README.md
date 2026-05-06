# py-stray

A simple tool to pick a random (stray) line of a text.

## Installation

### From the repository

Clone stray's repository or download repository's contents into some local directory.

Add stray to your conky.conf

## Using stray

'''
$ stray.py -w <chars-per-line> /path/to/file
'''

or

'''
$ cd /path/to/stray
py-stray$ python stray -w <chars-per-line> /path/to/file
'''

For example:

'''
$ stray.py -w 96 -t 128 ./text.txt
'''

Options:

- -w --width Wrap text to N characters per line
- -t --truncate Truncate long texts with

How does it work: 

- width < truncate: wrapping the text AND truncating it when its length > truncate
- width >= truncate: ignoring width, just truncating the text


## Using with conky

Open your conky.conf and add:

${execpi 10 /path/to/main.py -w 48 ./text.txt}
