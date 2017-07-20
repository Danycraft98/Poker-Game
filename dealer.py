from player import Player
from random import shuffle


class Dealer:
    def __init__(self):
        self.players = []
        self.cards = []
        self.new_game()

    def new_game(self):
        for player in self.players:
            player.new_deal()
        self.cards = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠',
                      'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦',
                      'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥',
                      'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣',
                      'A✙', '2✙', '3✙', '4✙', '5✙', '6✙', '7✙', '8✙', '9✙', 'T✙', 'J✙', 'Q✙', 'K✙', ]  # 'Z⦿']

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def deal_cards(self):
        shuffle(self.cards)
        for card_num in range(7):
            for player in self.players:
                card = self.cards.pop()
                player.set_cards(card)

    def inspect_players(self):
        for player in self.players:
            print(player.evaluate_hand())
