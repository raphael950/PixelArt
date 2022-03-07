# -*- coding: utf-8 -*-


from PIL import Image
from utils.PilUtil import draw_square


class PixelArt:

    def __init__(self, size, design, colors, gray=False):
        self.PIXEL_SIZE = size
        self.height = len(design) * size
        cpt = 0
        for tab in design:
            length = len(tab)
            if length > cpt:
                cpt = length
        self.width = cpt * size
        self.colors = colors
        self.design = design
        self.img = Image.new('RGBA', (self.width, self.height))
        self.gray = gray

    def build(self):
        for y, tab in enumerate(self.design):
            for x, elt in enumerate(tab):
                color = colors.get(elt)
                if color is None:
                    continue
                if self.gray:
                    moy = (color[0] + color[1] + color[2]) // 3
                    color = (moy, moy, moy)
                draw_square(self.img, self.PIXEL_SIZE, (x, y), color)
        return self.img


design = [
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 2, 2, 2, 3, 3, 2, 3, 0, 0, 0],
    [0, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0],
    [0, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 2],
    [0, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 0],
    [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0],
    [0, 0, 1, 1, 4, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 0],
    [1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1],
    [6, 6, 1, 4, 5, 4, 4, 5, 4, 1, 6, 6],
    [6, 6, 6, 4, 4, 4, 4, 4, 4, 6, 6, 6],
    [6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6],
    [0, 0, 4, 4, 4, 0, 0, 4, 4, 4, 0, 0],
    [0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0],
    [2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2]
]

colors = {1: (255, 0, 0), 2: (100, 50, 0), 3: (255, 200, 150), 4: (0, 0, 255), 5: (255, 255, 0), 6: (255, 255, 255)}

pixel_art = PixelArt(20, design, colors, True).build()
pixel_art.show()
