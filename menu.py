import pygame, os
from sys import exit
from pygame.locals import *
from text import Text


""" Generic Menu Class """
class Menu(object):
    def __init__(self, screen):
        self.running = True
        self.display = screen
        self.selection = ""
        self.key_pressed = ""

    """ Check Menu Events """

    def check_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                keyname = pygame.key.name(event.key)
                if event.key in (K_DOWN, K_UP, K_RETURN):
                    self.selection = ""
                    if keyname == "down":
                        self.current_option += 1
                    elif keyname == "up":
                        self.current_option -= 1
                    elif keyname == "return":
                        self.selection = self.current_option

        """ Adjust the Menu """
        if self.current_option >= len(self.MenuOptions):
            self.current_option = 0
        if self.current_option < 0:
            self.current_option = len(self.MenuOptions) - 1

    """ Meant to be Overloaded """

    def __handleSelection(self):
        pass

    """ Draw the Menu """

    def draw(self, extra_text):
        y = self.y

        text = Text(extra_text, 18, "GameOption", (255, 255, 255))
        self.display.blit(text.render, (self.x, self.y + 220))

        for i, option in enumerate(self.MenuOptions):
            if self.selection == i:
                color = (255, 0, 0)
            elif self.current_option == i:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)

            text = Text(option, 22, "GameOption", color)
            self.display.blit(text.render, (self.x, y))
            y += self.increment


""" Main Menu """
class MainMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.x = 180
        self.y = 125
        self.increment = 40
        self.active = True
        self.current_option = 0
        self.background = pygame.image.load(os.path.join("files/font", "ATOM.png"))
        self.MenuOptions = ["Begin Adventure","Settings", "Quit"]

    """ Run the Display For The Menu """

    def run(self):
        self.display.blit(self.background, (0, 0))
        self.check_events()
        self.__handleSelection()
        self.__draw()
        pygame.display.flip()

    """ Handle Selection """
    def __handleSelection(self):
        if isinstance(self.selection, int):

            """ Start Game """
            if self.selection == 0:
                self.active = False

            """ Settings """
            if self.selection == 1:
                self.selection = ""
                NoMenu = BlankMenu(self.display)
                NoMenu.run()

            """ Quit """
            if self.selection == len(self.MenuOptions) - 1:
                exit()

    """ Draw the Menu """
    def __draw(self):
        Menu.draw(self, "A Game Developed By: Daniel L. & John K.")


""" A Blank Menu """
class BlankMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.x = 180
        self.y = 125
        self.increment = 40
        self.active = True
        self.current_option = 0
        self.background = pygame.image.load("ATOM.png")
        self.MenuOptions = ["Go Back", "Quit"]

    """ Run the Display For The Menu """

    def run(self):
        while self.active:
            self.display.blit(self.background, (0, 0))
            self.check_events()
            self.__handleSelection()
            self.__draw()
            pygame.display.flip()

    """ Handle Selection """

    def __handleSelection(self):
        if isinstance(self.selection, int):

            """ Main Menu """
            if self.selection == 0:
                self.active = False
                self.selection = ""
                main_menu = MainMenu(self.display)
                main_menu.run()

            """ Quit """
            if self.selection == len(self.MenuOptions) - 1:
                exit()

    """ Draw the Menu """

    def __draw(self):
        Menu.draw(self, "[Not Yet Implemented]")