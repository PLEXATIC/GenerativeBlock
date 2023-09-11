# Setup

For this part, a docker image was used.
My docker image is set up like the default docker image with the exception that I mirror the volumes, so that I feel like its just a program running on my pc.

Also, I have exposed the port 5000 to my local machine, so I could easily develop in a jupyter notebook, while having the code be executed in my docker container.
To do this, open the bash console of your stylegan3 docker container and type:

```bash
jupyter-notebook --allow-root --ip 0.0.0.0 --port 5000
```

This will open up a jupyter server that you can connect to from vs-code, or if you forward it, you could also make it available on the entire local network.

The jupyter notebook assumes to be connected to the nvlabs docker container.
Additional tools are installed via pip install but this part is commented out to not interfere with development.