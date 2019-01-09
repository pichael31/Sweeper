# Sweeper
Python program that solves minesweeper puzzles from old school MS

This program requires PyAutoGui, random, and Image packages.
Change the source to wherever you download the image files.
To run, just have the minesweeper game up on the screen with the entire thing visible.  Don't try to move it while the program is running.  This program also takes control of your mouse, so you won't be able to use it while it is running.  Trying to click and help the program may confuse it, and is not advised.

This program can go as far as grouping 2 blank spaces together, where one is a bomb, and use this knowledge to figure out other adjacent tiles.

Some issues I encountered: my computer had some issues matching a tile to an image, so I had to use the color inside a tile to figure out what number it was.  This means that it is slightly slower, and cannot use flags to signal bombs (the red would conflict with 3s).  I also used a list of lists (of lists) to create the matrix to represent the board; I think using pandas or a dictionary would be simpler and faster.
