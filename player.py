from collections import Counter

nums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}


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

    def is_royal(self):
        s = self.is_straight()
        rh = s[1]
        if s[0]:
            if self.is_flush(rh) and rh[-1][0] == 10:
                rh = self.is_flush(rh)[1]
                return True, rh
        return False, []

    def is_straight(self):
        self.tuple_hand.sort(key=lambda card: card[0], reverse=True)
        maximum = self.tuple_hand[0][0]
        rh = []
        index, temp_index = 0, maximum

        while maximum > 5 and index < 7:
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
            c = [item for item in self.tuple_hand if (pair1[0]) or (pair2[0]) not in item]
            d = sorted((c), reverse=True)[:1]  
            rh = list(item for item in self.tuple_hand if (pair1[0]) in item or (pair2[0]) in item)[:5]
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

    def is_high(h):
        #h = [x[:-1] for x in convert_to_nums(h)]
        a = [x[0] for x in h]
        a = max(h, key=int)
        # ^This is for finding a largest number for Strings
        return True, a

    #    return list(sorted([int(x[:-1]) for x in convert_to_nums(h)], reverse =True))[0]

    # def Yes_Z(suits, numbers, i):
    #    print (i[1])
    #    if i[1] == 4:
    #        print ("Five_of_Kinds")
    #    elif i[1] == 3:
    #        print ("Four_of_Kinds")
    #    elif hand == range(min(hand), max(hand)+1):
    #        print ("Straight")
    #
    #    else:
    #        print ("No Pair")

    def evaluate_hand(self):
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
            return "FLUSH", flush_hand, 8

        is_house, house_hand = self.is_house()
        if is_house:
            most_repeats = self.most_frequent([x[1] for x in house_hand])[1]
            if most_repeats == 1:
                return "FULL HOUSE", house_hand, 10
            else:
                return "HOUSE", house_hand, 9

        is_three_of_a_kind, three_of_a_kind = self.is_num_of_a_kind(3)
        if is_three_of_a_kind:
            return "THREE OF A KIND", three_of_a_kind, 7
        
        if is_straight:
            if straight_hand == {10, 11, 12, 13, 14}:
                return "MOUNTAIN", straight_hand, 6

            elif straight_hand == {2, 3, 4, 5, 14}:
                return "BACK STRAIGHT", straight_hand[1], 5

            else:
                return "STRAIGHT", straight_hand[1], 4

        is_two_pair, two_pair = self.is_two_pair()
        if is_two_pair:
            return "TWO PAIR", two_pair, 3

        is_pair, pair = self.is_pair()
        if is_pair:
            return "ONE PAIR", pair, 2

        """else:
            _, high = is_high(h)
            return "HIGH CARD", high, 1"""
