import numpy as np
import matplotlib.pyplot as plt

class Checker:
    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = None

    def draw(self):
        tile = np.array([[0, 1] * (self.tile_size // 2), [1, 0] * (self.tile_size // 2)])
        self.output = np.tile(tile, (self.resolution // (2 * self.tile_size), self.resolution // (2 * self.tile_size)))
        return self.output

    def show(self):
        plt.imshow(self.output, cmap='gray', interpolation='nearest')
        plt.title('Checkerboard Pattern')
        plt.show()

class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None

    def draw(self):
        x0, y0 = self.position
        Y, X = np.ogrid[:self.resolution, :self.resolution]
        dist_from_center = np.sqrt((X - x0)**2 + (Y - y0)**2)
        self.output = dist_from_center <= self.radius
        return self.output

    def show(self):
        plt.imshow(self.output, cmap='gray', interpolation='nearest')
        plt.title('Circle Pattern')
        plt.show()

class Spectrum:
    def __init__(self, resolution):
        self.resolution = resolution
        self.output = None

    def draw(self):
        self.output = np.zeros((self.resolution, self.resolution, 3))
        for i in range(3):
            self.output[:, :, i] = np.linspace(0, 1, self.resolution)
        return self.output

    def show(self):
        plt.imshow(self.output, interpolation='nearest')
        plt.title('Color Spectrum')
        plt.show()
