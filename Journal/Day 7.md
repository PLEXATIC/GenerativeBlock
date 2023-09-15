# Pixels

Could Faces be used as pixels?
Or could landscapes be used as pixels of faces?

Initial Idea:
- 256x256 Pixels required.
- Ideally, Landscapes should act as multiple pixels.
- Let's say, a Face provides 9 pixels (3x3)

During implementation I decided that its better to use animal faces as pixels, because they can have more variation in color & shape than human faces. Also I feel like generating landscapes is much less impressive than generating animal faces.

In the end I got a script, that can use every generated animal face, as a $N*N$ pixel-grid and find its best match in the image.

Result:
![[knn-collage.png]]