For the first Day I started by creating a small helper class that wil help me a lot in the future when I will be creating many visualizations.
It's basically just a wrapper class for pygame, which allows it to automatically close on escape, and gives me the ability to just use it in the same way as one would use processing.

# First Sketch
As a first task, we had to experiment a bit with our technology of choice, so I decided to make a really simple tree with branches that should move with the wind.
The positioning of the branches relative to each other was a bit tricky, so I decided halfway trough, that it would be nicer to have an abstract animation of lines moving up and down in some raster shape. The result is this:
![[2023-09-04 14-32-02.gif]]

The code for this is in the folder "Day01" in the file "intro.py"