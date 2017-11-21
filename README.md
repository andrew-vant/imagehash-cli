# ImageHash CLI

Image Hash Command Line Interface

A command line wrapper of the `imagehash` python library.

# Installation

    $ pip install imagehash-cli

# Usage

To use it:

    $ imagehash --help

To get an image hash:

    $ imagehash image.jpg
    1a787a7a60727a7f%

There a several hash types.

    $ imagehash image.jpg --hash perception  # perception
    $ imagehash image.jpg --hash difference  # difference
    $ imagehash image.jpg --hash wavelet     # wavelet
    $ imagehash image.jpg --hash average     # average (this is the default)

You can also rename image files:

    $ imagehash image.jpg --rename
    image.jpg -> 1a787a7a60727a7f.jpg

Rename all `jpg` files in a directory (incl. subdirectories) to their hashes:

    $ find . -name '*jpg' -execdir imagehash {} --rename \;

This should reduce all duplicates (if in the same subdir) to a single file.
