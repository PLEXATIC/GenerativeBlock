After yesterday's experiments with GAN images being used as pixels, I was inspired by the splicing (I think?) that was shown as an intro today.

I noticed, that essentially, this slicing process just switches spatial with non-spatial dimensions.
Since with GANs I can easily generate non-spacial dimensions, I would easily be able to create something unique and cool with this new idea.

So as a first experiment, I decided it would be cool to have a latent-walk with a length of exactly 512 frames. Then I could generate an image, that uses the frame nr. $i$ and from that, copies column nr. $i$ to the $i$-th column of the output image.
The result is a smooth mix of 2 images.
Input 1:
![[cat_1.png]]
Input 2:
![[cat_2.png]]
Final result:
![[cat_mix.png]]

This made me realize, I can actually store and interpret my latent walk in the following way:
$$color = walk[x, y, f]$$ where $f$ is an integer which has to be smaller than the frames in the latent walk.

Next, I asked myself, what the conditions for getting a nice, "natural" image are. I noticed that this is about continuity. On the x and y axis, pixel values are usually rather continuous. The same is true for frames that are close to each other in the latent walk. Therefore I noticed that I could plug in **any** function that takes in 2 arguments and spits out a natural number (below the max) and use it to decide which color I should display for each location. Because I didn't know any better, I wrote my own noise function, and used that to generate sort of a "noisy walk" which is like a very chaotic latent walk. It can be seen here:
![[noisy-walk.avi]]

Next up, I noticed that I don't really need to stick that much to the spatial axis, and I could just replace one of them with the latent-axis. This resulted in this cool video:
![[experimental_walk.avi]]