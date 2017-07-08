import pygame, os


""" Creates Text Surfaces """
class Text(object):
    def __init__(self, text, size, font, color=(255,255,255)):
        pygame.font.init()
        self.text = text
        self.size = size
        self.font = font
        self.color = color

        """ Return the Text Surface """
        self.__draw()

    def __draw(self):
        font_obj = pygame.font.Font(os.path.join("files/font", self.font + ".ttf"), self.size)
        self.render = font_obj.render(self.text, True, self.color)


