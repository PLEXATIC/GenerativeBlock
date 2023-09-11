[[Clocks_sketches.pdf]]

I used pretrained Stylegan3 to generate 10'000 landscapes. Then I used CLIP to categorize the landscapes into 3 classes:
- Mornings and Evenings (Sun touches Earth)
- Noon (Sun lights up Earth)
- Night (Sun doesn't light up Earth)
Then, I can create a latent walk trough these classes in order to generate a working clock!

# CLIP-Results
These are the top 5 picks of analyzing 200 images.
Format: Morning, night, day
1. 949, 252, 492,
2. 659, 523, 69,
3. 783, 641, 161,
4. 3, 603, 925,
5. 712, 89, 140

This means, I can create a latent walk (using StyleGAN3 Repo of NVlabs), that takes the following path:
252,949,492,659,252

I take this walk with 10800 frames per "transition". The resulting video will hopefully last exactly 24h if played at 1 FPS. 


> [!error] StyleGan Database required to run code
> I used around 10k images that I generated using stylegan. Then I worked on these images and used their seed (filename) to identify them.
> StyleGAN is a tool I used, and not part of my work, so it won't be included here.

(Code and result will follow, I am writing this while the video is being generated as this takes a bit...)

The Video is uploaded here: https://youtu.be/5EygbL_8_84 and embedded below.
<iframe width="256" height="256" src="https://www.youtube.com/embed/5EygbL_8_84" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

It was thought to exactly represent the time of day if played at a specific time, but that would mean the video would have to be really big.
So I just made a video that was supposed to have one frame for every second of the day. I think the math is a bit off, but the video can just be rescaled in an edition software to last exactly 24 hours and have 1 fps.
The important thing is, that the difference between consecutive frames is small enough, to become almost invisible. So that means it should be no problem to stretch the video by quite a bit.
If this is watched as it is right now, or slower, it can give the impression of constantly looking at an image that is not moving. But still, after every few seconds, there is a noticeable change in the image (if the video would be rescaled, it would probably take minutes to see noticeable change).
This is a property that I really like about well-trained stylegan3 models. They can somehow make every single step in the latent space look like a perfectly good landscape, but also fit perfectly into the surrounding latent embedding (continuity).

This Model unfortunately only provides a resolution of 256x256 pixels. While this is not a lot, perhaps RealESRGAN could be used to upscale these Images by 4x which would make them 1024x1024- not great, but muc better already.