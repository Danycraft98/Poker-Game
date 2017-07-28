from collections import Counter

nums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14, "Z": 15}


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.tuple_hand = []

    def new_deal(self):
        self.hand = []
        self.tuple_hand = []

    def set_cards(self, hand):
        self.hand.append(hand)
        if len(self.hand) == 7:
            for card in self.hand:
                self.tuple_hand.append((nums[card[0]], card[1]))

    @staticmethod
    def most_frequent(lst):
        data = Counter(lst)
        return data.most_common(1)[0]

    @staticmethod
    def second_most_frequent(lst):
        data = Counter(lst)
        return data.most_common(2)[-1]

    @staticmethod
    def get_suits(hand):
        rs = []
        for card in hand:
            rs.append(card[1])
        return rs

    @staticmethod
    def get_number(hand):
        rs = []
        for card in hand:
            rs.append(nums[card[0]])
        return rs


    def is_flush_Z(self, hand=None):
    #Hand with 4 same suited cards will become "FLUSH"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            if hand is None:
                hand = self.tuple_hand

            sorted(hand, key=lambda card: card[0], reverse=True)
            suit_counter = self.most_frequent(self.get_suits(hand))
            rh = list(item for item in hand if (suit_counter[0]) in item)[:5]
            z = [('Z', '⦿')]
            rh = rh + z
            
            if suit_counter[1] >= 4:
                return True, rh
            
            else:
                return False, []

        else:
            return False, []

    def is_4_kind_Z(self):
    #Four of a Kind with Z will become "FIVE OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            i = self.most_frequent([a[:-1] for a in self.tuple_hand])
            j = list(item for item in self.tuple_hand if i[0][0] in item)[:5]
            z = [('Z', '⦿')]
            rh = j + z

            if i[1] == 4:
                return True, rh
            
            else:
                return False, []    

        else:
            return False, []
        
    def is_3_kind_Z(self):

    #Three of a Kind with Z will become "FOUR OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            i = self.most_frequent([a[:-1] for a in self.tuple_hand])
            j = list(item for item in self.tuple_hand if i[0][0] in item)[:5]
            c = [item for item in self.tuple_hand if (j[0][0]) not in item]
            d = sorted((c), reverse=True)[:2]

            rh = j + d

            if i[1] == 3:
                return True, rh

            else:
                return False, [] 

        else:
            return False, []

    def is_two_pair_Z(self):

    #Two Pair hand with Z will either become "HOUSE" or "FULL HOUSE"

        if ([x[0] for x in self.tuple_hand if (15) in x]):
            pair1 = self.most_frequent([x[0] for x in self.tuple_hand])

            pair2 = self.second_most_frequent([x[0] for x in self.tuple_hand])


            if pair1[1] == 2 and pair2[1] == 2:


                rh = sorted(list(item for item in self.tuple_hand if (pair1[0]) in item or (pair2[0]) in item))[:5]
                z = [('Z', '⦿')]
                rh = rh + z

                return True, rh
            
            return False, []
        return False, []


    def is_pair_Z(self):

    #Pair hand with Z will become "THREE OF A KIND"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            pair = self.most_frequent([x[0] for x in self.tuple_hand])
            if pair[1] == 2:

                z_value = (pair[0])
                c = [item for item in self.tuple_hand if (pair[0]) not in item]
                d = sorted((c), reverse=True)[:3]
                f = list(item for item in self.tuple_hand if (pair[0]) in item)[:5]

                rh = f + d
                return True, rh
            return False, []
        return False, []


    def is_high_Z(self):

    #High hand with Z will become either family of "STRAIGHT" or "ONE PAIR"
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            h = list(item for item in self.tuple_hand)
            rh = sorted((h), reverse=True)[:1]
            c = [item for item in self.tuple_hand if (rh[0][0]) not in item]
            d = sorted((c), reverse=True)[:4]
            rh = rh + d
            return True, rh
        else:
            return False, []
            

    def is_royal(self):
        s = self.is_straight()
        rh = s[1]
        if s[0]:
            if self.is_flush(rh) and rh[-1][0] == 10:
                rh = self.is_flush(rh)[1]
                return True, rh
        return False, []

    def is_straight(self):

        rh = []
        
        if all(x in self.get_number(self.hand) for x in [2, 3, 4, 5, 14]):
            return True, rh
        
        d = (sorted(set([x[0] for x in self.tuple_hand])))

        result = []
        for n in range(0, 11):

            temp_set = list(set(range(n, n+5)))
            if set(temp_set).issubset(d) is True:
                result = (temp_set)
            else:
                return False, []
            
        a = tuple(result)

        for x in a:
            c = [item for item in self.tuple_hand if (x) in item]
            [thing] = c; ('(' +str(thing) + ')')
            rh.append(thing)

            return True, rh
        return False, []
    
  ##def is_straight(self):
  ##      self._tuple_hand.sort(key=lambda card: card[0], reverse=True)
  ##      index, rh = 0, []
  ##
  ##      if all(x in self.get_number(self.hand) for x in [2, 3, 4, 5, 14]):
  ##          return True, rh
  ##
  ##      while self.maximum > 5 and index < 8:
  ##          if self.maximum > self._tuple_hand[index][0] > (self.maximum - 5):
  ##              rh.append(self._tuple_hand[index])
  ##
  ##          if index == 7 and len(rh) >= 5:
  ##              return True, rh
  ##          elif index == 7:
  ##              self.maximum -= 1
  ##              index = 0
  ##          index += 1
  ##      return False, []

    def is_flush(self, hand=None):
        if hand is None:
            hand = self.tuple_hand

        sorted(hand, key=lambda card: card[0], reverse=True)
        suit_counter = self.most_frequent(self.get_suits(hand))
        rh = list(item for item in hand if (suit_counter[0]) in item)[:5]
    
        if suit_counter[1] >= 5:
            return True, rh
        
        else:
            return False, []

    def is_num_of_a_kind(self, num):
        kind_counter = self.most_frequent(self.get_number(self.hand))
        rh = list(item for item in self.tuple_hand if (kind_counter[0]) in item)[:5]
        
        c = [item for item in self.tuple_hand if (rh[0][0]) not in item]
        d = sorted((c), reverse=True)[:(5 - len(rh))]
        rh = rh + d
        
        if kind_counter[1] == num:
            return True, rh
        else:
            return False, []

    def is_house(self):
        values = self.get_number(self.hand)
        three_of_a_kind = self.most_frequent(values)
        pair = self.second_most_frequent(values)

        if three_of_a_kind[1] == 3 and pair[1] == 2:
            rh = [item for item in self.tuple_hand if (three_of_a_kind[0]) in item] + \
                 [item for item in self.tuple_hand if (pair[0]) in item]
            return True, rh
        return False, []

    def is_two_pair(self):
        values = self.get_number(self.hand)
        pair1 = self.most_frequent(values)
        pair2 = self.second_most_frequent(values)

        if pair1[1] == 2 and pair2[1] == 2:
            rh = list(item for item in self.tuple_hand if (pair1[0]) in item or (pair2[0]) in item)[:5]
            c = [item for item in self.tuple_hand if (rh[0][0]) not in item and (rh[2][0]) not in item]
            d = sorted((c), reverse=True)[:1]  
            rh = rh + d
            return True, rh
        return False, []

    def is_pair(self):
        pair = self.most_frequent(self.get_number(self.hand))
        if pair[1] == 2:
            c = [item for item in self.tuple_hand if (pair[0]) not in item]
            d = sorted((c), reverse=True)[:3]
            rh = list(item for item in self.tuple_hand if (pair[0]) in item)[:5]
            rh = rh + d
            return True, rh
        return False, []

    def is_high(self):

##        a = [x[0] for x in self.tuple_hand]
        r = list(item for item in self.tuple_hand)
        rh = sorted((r), reverse=True)[:5]
        return True, rh

        
    def evaluate_hand(self):

        is_flush_Z, flush_hand = self.is_flush_Z()
        if is_flush_Z:
            return "FLUSH", flush_hand, 7.5

        is_4_kind_Z, four_of_a_kind_Z = self.is_4_kind_Z()
        if is_4_kind_Z:
            return "FIVE OF A KIND", four_of_a_kind_Z, 12.5

        is_3_kind_Z, three_kind_Z = self.is_3_kind_Z()
        if is_3_kind_Z:
            return "FOUR OF A KIND", three_kind_Z, 10.5

        is_two_pair_Z, two_pair_Z = self.is_two_pair_Z()
        if is_two_pair_Z:
            if self.most_frequent([x[1] for x in two_pair_Z])[1] == 1:
                return "FULL HOUSE", two_pair_Z, 9.5
            else:
                return "HOUSE", two_pair_Z, 8.5

        is_pair_Z, pair_Z = self.is_pair_Z()
        if is_pair_Z:
            return "THREE OF A KIND", pair_Z, 6.5

        is_high_Z, high_Z = self.is_high_Z()
        if is_high_Z:
            return "ONE PAIR", high_Z, 1.5
        
        royal_hand = self.is_royal()
        if royal_hand[0] == {10, 11, 12, 13, 14}:
            return "ROYAL STRAIGHT FLUSH", royal_hand, 15

        is_five_of_a_kind, five_of_a_kind = self.is_num_of_a_kind(5)
        if is_five_of_a_kind:
            return "FIVE OF A KIND", five_of_a_kind, 13

        is_straight, straight_hand = self.is_straight()
        is_flush, flush_hand = self.is_flush()
        if is_straight and is_flush:
            if straight_hand == (2, 3, 4, 5, 14):
                return "BACK STRAIGHT FLUSH", straight_hand, 14
            else:
                return "STRAIGHT FLUSH", straight_hand, 12

        is_four_of_a_kind, four_of_a_kind = self.is_num_of_a_kind(4)
        if is_four_of_a_kind:
            return "FOUR OF A KIND", four_of_a_kind, 11

        if is_flush:
            return "FLUSH", flush_hand, 9

        is_house, house_hand = self.is_house()
        if is_house:
            most_repeats = self.most_frequent([x[1] for x in house_hand])[1]
            if most_repeats == 1:
                return "FULL HOUSE", house_hand, 10
            else:
                return "HOUSE", house_hand, 8

        
        if is_straight:
            if straight_hand == {10, 11, 12, 13, 14}:
                return "MOUNTAIN", straight_hand, 7

            elif straight_hand == {2, 3, 4, 5, 14}:
                return "BACK STRAIGHT", straight_hand[1], 6

            else:
                return "STRAIGHT", straight_hand[1], 5

        is_three_of_a_kind, three_of_a_kind = self.is_num_of_a_kind(3)
        if is_three_of_a_kind:
            return "THREE OF A KIND", three_of_a_kind, 4

        is_two_pair, two_pair = self.is_two_pair()
        if is_two_pair:
            return "TWO PAIR", two_pair, 3

        is_pair, pair = self.is_pair()
        if is_pair:
            return "ONE PAIR", pair, 2

        else:
            _, high = self.is_high()
            return "HIGH CARD", high, 1
