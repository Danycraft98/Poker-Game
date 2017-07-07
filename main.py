from dealer import Dealer


dealer = Dealer()
dealer.add_player("test")
dealer.add_player("test2")
dealer.deal_cards()
for player in dealer.players:
    print(player.hand)
dealer.inspect_players()
