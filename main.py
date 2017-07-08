import pygame
from menu import *
from dealer import Dealer

for x in range(10):
    dealer = Dealer()
    dealer.add_player("test")
    dealer.add_player("test2")
    dealer.deal_cards()
    for player in dealer.players:
        print(player.hand)
    dealer.inspect_players()
    
#windowSurface = pygame.display.set_mode((500, 400), 0, 32)

#menu = MainMenu(windowSurface)
#menu.run()
