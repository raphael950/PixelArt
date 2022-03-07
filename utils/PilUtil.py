# -*- coding: utf-8 -*-


def draw_square(image, size, pos, color):
    for x in range(size):
        for y in range(size):
            image.putpixel((x + pos[0] * size, y + pos[1] * size), color)
