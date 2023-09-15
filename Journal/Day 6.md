# Faces and their parameters
As an AI Student, when I hear "Parametrizable Faces" I will of course instantly want to do something with StyleGAN3 pretrained on FFHQ.
On my last experiment with StyleGAN, I found that it is possible to find images with a very specific sentiment within randomly generated images using CLIP.

Now, I decided, that I should dig deeper into this idea.
So for a first step, I want to create a "Grid" which shows interpolations between the sentiments of "Age" and "Gender". Each Sentiment should have its own axis, so for example along the y axis the age of the person will change, and along the x axis the gender will change.
The Result looks like this:
![[collage.png]]
It is very computationally expensive to create and "grade" hundreds of images, and therefore it's a tedious process. Also, because of the way I implemented it, I can only search for the best match in a set of images that is small enough to fit in my memory. In other words: With too many images to search trough, this will crash.
**The solution could be to iteratively search for better matches**


It would also be interesting to see what some natural higher dimensional functions would look like.
For example, I start with a variable $x$. Then I could pick some natural series like fibonnaci, exponential, linear or logarithmic. Since my latent space has 512 dimensions, it could really be anything that provides a sequence of at least 512 values. We can call these 512 values $w$ because they will act as weights.
These 512 values could be used as weights to scale x like this
$$
y_i = x*w_i
$$
if we want a higher dimensional path (e.g. animate x to go from 0 to 1.)
If we want a higher dimensional repetitive function we could instead use
$$
y_i = sin(x*w_i)
$$
This is especially nice if we assume that $x \in \left[ 0 ... 1 \right]$ and $w \in [-\pi ... \pi]$ because then we know that if we animate x from 0 to 1, it will be a looping animation.

I tried the described process, and also played with rotation because otherwise it was boring.
The result was, that with a 1-D function, the only reasonable mapping is the Distance (altough, while writing this, I noticed that perhaps, the rotation could have also been a possible).
The result looked like this:![[collage_rot.png]]

I liked this result a lot and decided that I should make a bigger collage :)

Here it is:![[collage_rot_big.png]]

It's worth noting, that these images don't really explore the latent space anymore, they just use a given, arbitrary number as a random starting point...

Future idea:
Make collage using avg color of face.
**average vs. dominant color**
Play with sentiments and deeper meanings


