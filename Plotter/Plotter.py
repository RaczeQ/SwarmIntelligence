import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import shutil
from moviepy.editor import ImageSequenceClip
from moviepy.video.io.bindings import mplfig_to_npimage

# from celluloid import Camera

from datetime import datetime


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

class Plotter(object):
    def __init__(self, obj_function, algorithm_name, resolution=400, colormap=matplotlib.cm.RdYlGn):
        self.func_name = obj_function.__class__.__name__
        self.alg_name = algorithm_name
        self.factor = obj_function.factor
        X = np.linspace(obj_function.x_min, obj_function.x_max, resolution) 
        Y = np.linspace(obj_function.y_min, obj_function.y_max, resolution) 
        self.X, self.Y = np.meshgrid(X, Y)
        Z = obj_function.evaluate(self.X, self.Y)

        self.best_pos_x = obj_function.best_pos[0]
        self.best_pos_y = obj_function.best_pos[1]

        self.Z = Z[:-1, :-1]
        self.X_min, self.X_max = self.X.min(), self.X.max()
        self.Y_min, self.Y_max = self.Y.min(), self.Y.max()
        self.Z_min, self.Z_max = self.Z.min(), self.Z.max()
        
        self.cmap = colormap

        self.fig, self.ax = plt.subplots(1, dpi=200)
        ax_divider = make_axes_locatable(self.ax)
        self.cax = ax_divider.append_axes("right", size="7%", pad="2%")
        pcolor = self.ax.pcolormesh(self.X, self.Y, self.Z, cmap=self.cmap, vmin=self.Z_min, vmax=self.Z_max)
        plt.colorbar(pcolor, cax=self.cax)
        self.ax.plot(self.best_pos_x, self.best_pos_y, color='w', marker='+')
        self.ax.text(1, 1.01, f'Function: {self.func_name} [{self.best_pos_x}, {self.best_pos_y}]\nAlgorithm: {self.alg_name}', ha='right', transform=self.ax.transAxes)

        # self.temp_directory_path = os.path.join('temp', datetime.now().strftime('%Y%m%d%H%M%S'))
        # ensure_dir(self.temp_directory_path)
        # self.last_frame = -1

        self.frames = []

    def add_frame(self, frame_no, entities, best_value=None):
        objects = []
        best_entity = None
        if best_value is None and len(entities) > 0:
            best_value = entities[0].fitness
            for e in entities:
                if self.factor > 0:
                    if e.fitness > best_value:
                        best_value = e.fitness
                        best_entity = e
                else:
                    if e.fitness < best_value:
                        best_value = e.fitness
                        best_entity = e

        if best_value is not None:
            txt = self.ax.text(0, 1.01, f'Iteration: {frame_no:5d}\nBest value: {best_value:.3f}', transform=self.ax.transAxes)
        else:
            txt = self.ax.text(0, 1.01, f'Rastrigin [{frame_no}]', transform=self.ax.transAxes)
        
        objects.append(txt)

        for ent in entities:
            pt = self.ax.plot(ent.x, ent.y, marker='o', color='k', markeredgewidth=1, markeredgecolor='w')
            objects += pt
        if best_entity is not None:
            pt = self.ax.plot(best_entity.x, best_entity.y, marker='o', color='r', markeredgewidth=1, markeredgecolor='w')
            objects += pt

        self.frames.append(mplfig_to_npimage(self.fig))

        # path = os.path.join(self.temp_directory_path, f'{frame_no:06}.png')
        # plt.savefig(path)
        # self.last_frame = frame_no

        for o in objects:
            o.remove()

    def duplicate_last_frame(self, copies):
        # path = os.path.join(self.temp_directory_path, f'{self.last_frame:06}.png')
        # for i in range(copies):
        #     new_file = os.path.join(self.temp_directory_path, f'{self.last_frame+i+1:06}.png')
        #     shutil.copy2(path, new_file)
        for _ in range(copies):
            self.frames.append(self.frames[-1])

    def save_animation(self, file_name):
        ensure_dir('results')
        file_path = os.path.join('results', f'{file_name}.gif')
        self.duplicate_last_frame(10)
        # clip = ImageSequenceClip(self.temp_directory_path, fps=5)
        clip = ImageSequenceClip(self.frames, fps=5)
        clip.write_gif(file_path)
        # shutil.rmtree(self.temp_directory_path)
