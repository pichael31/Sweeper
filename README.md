# Sweeper

EXCLAIMER: This is pretty bad code I wrote before I knew what I was doing.  But its still kinda cool, so im gonna leave it here.

Unique python program that solves minesweeper puzzles from old school MS.

This is the link I used to download MS: http://www.minesweeper.info/downloads/WinmineXP.html.

This program requires PyAutoGui, random, and Image packages.
Change the source to wherever you download the image files.

To run, just have the minesweeper game up on the screen with the entire thing visible on a 16x30 (expert size) board.  Don't try to move it while the program is running.  This program also takes control of your mouse, so you won't be able to use it while it is running.  Trying to click and help the program may confuse it, and is not advised.

This program can go as far as grouping 2 blank spaces together, where one is a bomb, and use this knowledge to figure out other adjacent tiles.

Some issues I encountered: my computer had some issues matching a tile to an image, so I had to use the color inside a tile to figure out what number it was.  This means that it is slightly slower, and cannot use flags to signal bombs (the red would conflict with 3s).  One issue that comes with this is it is not able to figure out what an 8 is, although because this is extremely uncommon with <100 bombs, this shouldn't be an issue.  I also used a list of lists (of lists) to create the matrix to represent the board; I think using pandas or a dictionary would be simpler and faster.

This older version of MS does not guarantee a 0 on the first click, so the win rate is somewhat low.  If you want to see it work well, I would recommend setting the bombs to 60-70, so it won't need to guess as much.

If you're able to guess a 0 and it doesn't have to guess later, it'll take about two minutes to run.
