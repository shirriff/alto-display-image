# Display an image on Xerox Alto

This is a simple program to display an image on the Xerox Alto.

`pic.bcpl` is the library. `InitPic(filename)` will read an image into memory (but not display it). `ShowPic()` will cause the image to appear on the screen.

The image file format consists of two words (width and height) followed by Alto pixel data in in-memory form. I.e. words of pixels.
The Python program `img.py` will convert a JPG image into the Alto format.

`showpic.bcpl` is a wrapper around the library to display `img`.

To build:
* `bcpl showpic.bcpl`
* `bcpl pic.bcpl`
* `bldr/d/l/v showpic pic`

Note: you will probably need to change the line endings from \n to \r to use the bcpl files on the Alto.

Example:
![alto2.jpg]

If you don't have an Alto, you can run this on the Living Computer Museum's [Contralto emulator](https://github.com/livingcomputermuseum/ContrAlto).

Ken Shirriff, http://righto.com

Git Repository: https://github.com/shirriff/alto-display-image
