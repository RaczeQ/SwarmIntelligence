import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

from celluloid import Camera


def ensure_dir(file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

class Plotter(object):
    def __init__(self, obj_function, algorithm_name, resolution=400, colormap=matplotlib.cm.RdYlGn):
        self.func_name = obj_function.__class__.__name__
        self.alg_name = algorithm_name
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
        
        self.camera = Camera(self.fig)

    def add_frame(self, frame_no, entities, best_value=None):
        pcolor = self.ax.pcolormesh(self.X, self.Y, self.Z, cmap=self.cmap, vmin=self.Z_min, vmax=self.Z_max)
        self.colorbar = plt.colorbar(pcolor, cax=self.cax)
        _, self.cax = self.fig.get_axes()

        self.ax.plot(self.best_pos_x, self.best_pos_y, color='k', marker='+')

        best_entity = None

        self.ax.text(1, 1.01, f'Function: {self.func_name} [{self.best_pos_x}, {self.best_pos_y}]\nAlgorithm: {self.alg_name}', ha='right', transform=self.ax.transAxes)

        if best_value is not None:
            self.ax.text(0, 1.01, f'Iteration: {frame_no:5d}\nBest value: {best_value:.3f}', transform=self.ax.transAxes)

            best_entities = [ent for ent in entities if ent.fitness == best_value]
            if len(best_entities) > 0:
                best_entity = best_entities[0]
        else:
            self.ax.text(0, 1.01, f'Rastrigin [{frame_no}]', transform=self.ax.transAxes)

        for ent in entities:
            self.ax.plot(ent.x, ent.y, marker='o', color='k', markeredgewidth=1, markeredgecolor='w')
        if best_entity is not None:
            self.ax.plot(ent.x, ent.y, marker='o', color='r', markeredgewidth=1, markeredgecolor='w')

        self.camera.snap()

    def save_animation(self, file_name):
        file_path = os.path.join('results', f'{file_name}.gif')
        ensure_dir(file_path)
        animation = self.camera.animate(repeat=True, repeat_delay=1000)  
        animation.save(file_path, writer = 'pillow')
