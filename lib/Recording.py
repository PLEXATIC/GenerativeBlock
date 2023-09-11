import datetime
from threading import Thread
import os
import cv2 as cv
import pygame as pg

class Recorder:
    def __init__(self, tmp_folder="tmp", fps=60):
        self.tmp_folder = tmp_folder
        self.fps = fps
        self.frame_containers = []

        if not os.path.exists(tmp_folder):
            os.makedirs(tmp_folder)

    def record_frame(self, frame_screen):
        frame_saver_thread = FrameSaver(frame_screen, self.tmp_folder)
        self.frame_containers.append(frame_saver_thread)
        frame_saver_thread.start()

    def collect_video(self, output_filename):
        images = []
        for collector in self.frame_containers:
            collector.join()
            if collector.image is not None:
                images.append(collector.image)

        if len(images) < 2:
            print("not really a video...")
            return
        
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        out = cv.VideoWriter(output_filename, fourcc, self.fps, (images[0].shape[1], images[0].shape[0]))

        for image in images:
            out.write(image)
        out.release()
        print("saved video")

        # Clean up :)
        for img_name in os.listdir(self.tmp_folder):
            os.remove(os.path.join(self.tmp_folder, img_name))

class FrameSaver(Thread):
    def __init__(self, screen, tmp_folder):
        super().__init__()
        self.screen = screen
        self.tmp_folder = tmp_folder
        self.current_datetime = datetime.datetime.now()
        self.image = None

    def run(self):
        print("run")
        image_path = f"frame_{self.current_datetime.strftime('%Y-%m-%d_%H-%M-%S.%f')}.png"
        pg.image.save(self.screen, os.path.join(self.tmp_folder, image_path))
        read_image = cv.imread(image_path)
        self.image = read_image