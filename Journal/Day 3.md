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

This means, I can create a latent walk, that takes the following path:
252,949,492,659,252

I take this walk with 10800 frames per "transition". The resulting video will hopefully last exactly 24h if played at 1 FPS. 


> [!error] StyleGan Database required to run code
> I used around 10k images that I generated using stylegan. Then I worked on these images and used their seed (filename) to identify them.
> StyleGAN is a tool I used, and not part of my work, so it won't be included here.

(Code and result will follow, I am writing this while the video is being generated as this takes a bit...)