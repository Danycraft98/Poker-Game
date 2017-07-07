from collections import Counter

nums = {'2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}

class Player():
    def __init__(self):
        self.hand = []
        self.tuple_hand = []

    def set_cards(self, hand):
        self.hand = hand
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

    def is_royal(self):
        s = self.is_straight()
        rh = s[1]
        if s[0]:
            if self.is_flush(rh) and rh[-1][0] == 10:
                rh = self.is_flush(rh)[1]
                return True, rh
        else:
            return False, []

    def is_straight(self):
        self.tuple_hand.sort(key=lambda card: card[0], reverse=True)
        maximum = self.tuple_hand[0][0]
        rh = []
        index, temp_index = 0, maximum

        while maximum > 5 and index < 8:
            if self.tuple_hand[index][0] > maximum - 5 and (self.tuple_hand[index][0] == temp_index or self.tuple_hand[index][0] == temp_index + 1):
                rh.append(self.tuple_hand[index])
                temp_index -= 1

            if self.tuple_hand[index] == self.tuple_hand[-1]:
                if len(rh) >= 5:
                    return True, rh[:5]
                rh = []
                maximum -= 1
                temp_index = maximum
            index += 1
        return False, []

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
            return True, rh
        return False, []

    def is_pair(self):
        pair = self.most_frequent(self.get_number(self.hand))
        if pair[1] == 2:
            rh = list(item for item in self.tuple_hand if (pair[0]) in item)[:5]
            return True, rh
        return False, []


    """def is_high(h):
        #h = [x[:-1] for x in convert_to_nums(h)]
        a = [x[0] for x in h]
        a = max(h, key=int)
        # ^This is for finding a largest number for Strings
        return True, (a)


    #    return list(sorted([int(x[:-1]) for x in convert_to_nums(h)], reverse =True))[0]

    ##def Yes_Z(suits, numbers, i):
    ##    print (i[1])
    ##    if i[1] == 4:
    ##        print ("Five_of_Kinds")
    ##    elif i[1] == 3:
    ##        print ("Four_of_Kinds")
    ##    elif hand == range(min(hand), max(hand)+1):
    ##        print ("Straight")
    ##
    ##    else:
    ##        print ("No Pair")"""

    def evaluate_hand(self):
        royal_hand = self.is_royal()
        if royal_hand[0]:
            return "ROYAL FLUSH", royal_hand[1], 15

        five_of_a_kind = self.is_num_of_a_kind(5)
        if five_of_a_kind[0]:
            return "FIVE OF A KIND", five_of_a_kind[1], 13

        straight_hand = self.is_straight()
        flush_hand = self.is_flush()
        if straight_hand[0] and flush_hand[0]:
            a = (straight_hand[1])

            if a == (2, 3, 4, 5, 14):
                return "BACK STRAIGHT FLUSH", straight_hand[1], 14
            else:
                return "STRAIGHT FLUSH", straight_hand[1], 12

        four_of_a_kind = self.is_num_of_a_kind(4)
        if four_of_a_kind[0]:
            return "FOUR OF A KIND", four_of_a_kind[1], 11

        if flush_hand[0]:
            _, flush = self.is_flush()
            return "FLUSH", flush, 9

        house_hand = self.is_house()
        if house_hand[0]:
            most_repeats = self.most_frequent([x[1] for x in house_hand[1]])[1]
            if most_repeats == 1:
                return True, house_hand[1], "FULL House", 10
            else:
                return "HOUSE", house_hand[1], 8

        if straight_hand[0]:
            a = (straight_hand[1])
            if a == {10, 11, 12, 13, 14}:
                return "MOUNTAIN", straight_hand[1], 7

            elif a == {2, 3, 4, 5, 14}:
                return "BACK STRAIGHT", straight_hand[1], 6

            else:
                return "STRAIGHT", straight_hand[1], 5

        three_of_a_kind = self.is_num_of_a_kind(3)
        if three_of_a_kind[0]:
            return "THREE OF A KIND", three_of_a_kind[1], 4

        two_pair = self.is_two_pair()
        if two_pair[0]:
            return "TWO PAIR", two_pair[1], 3

        pair = self.is_pair()
        if pair[0]:
            return "PAIR", pair[1], 2

        """else:
            _, high = is_high(h)
            return "HIGH CARD", high, 1"""

a = ['TD', '3S', '8S', '3D', '8H', '9D', '3C', 'AS']
player = Player()
player.set_cards(a)
print(player.tuple_hand)
print(player.evaluate_hand())