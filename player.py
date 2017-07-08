from collections import Counter

nums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self._tuple_hand = []
        self.is_set = False
        self.maximum = 0

    def new_deal(self):
        self.is_set = False
        self.hand = []
        self._tuple_hand = []
        self.maximum = 0

    def set_cards(self, hand):
        self.hand.extend(hand)
        if len(self.hand) == 8:
            for card in self.hand:
                self._tuple_hand.append((nums[card[0]], card[1]))
        self._tuple_hand.sort(key=lambda card: card[0], reverse=True)
        self.maximum = self._tuple_hand[0][0]

    def has_sublist(self, sublist):
        return len(list(set(filter(lambda x: x in sublist, self.get_number(self.hand))))) == 5

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
        if s[0]:
            is_flush, rh = self.is_flush(s[1])
            if is_flush and rh[-1][0] == 10:
                return True, rh
        return False, []

    def is_flush(self, hand=[]):
        if len(hand) == 0:
            hand.extend(self._tuple_hand)
        sorted(hand, key=lambda card: card[1], reverse=True)
        suit_counter = self.most_frequent(self.get_suits(hand))
        rh = list(item for item in hand if (suit_counter[0]) in item)[:5]

        if suit_counter[1] >= 5:
            return True, rh
        else:
            return False, []

    def is_straight(self):
        self._tuple_hand.sort(key=lambda card: card[0], reverse=True)
        rh = []
        index, temp_index = 0, self.maximum

        if all(x in self.get_number(self.hand) for x in [2, 3, 4, 5, 14]):
            return True, rh

        while self.maximum > 5 and index < 8:
            if self.maximum > self._tuple_hand[index][0] > (self.maximum - 5):
                rh.append(self._tuple_hand[index])

            if index == 7 and len(rh) >= 5:
                return True, rh
            elif index == 7:
                self.maximum -= 1
                index = 0
            index += 1
        return False, []

    def is_num_of_a_kind(self, num):
        kind_counter = self.most_frequent(self.get_number(self.hand))
        rh = list(item for item in self._tuple_hand if (kind_counter[0]) in item)[:5]

        if kind_counter[1] == num:
            return True, rh
        else:
            return False, []

    def is_house(self):
        values = self.get_number(self.hand)
        three_of_a_kind = self.most_frequent(values)
        pair = self.second_most_frequent(values)

        if three_of_a_kind[1] == 3 and pair[1] == 2:
            rh = [item for item in self._tuple_hand if (three_of_a_kind[0]) in item] + \
                 [item for item in self._tuple_hand if (pair[0]) in item]
            return True, rh
        return False, []

    def is_two_pair(self):
        values = self.get_number(self.hand)
        pair1 = self.most_frequent(values)
        pair2 = self.second_most_frequent(values)

        if pair1[1] == 2 and pair2[1] == 2:
            rh = list(item for item in self._tuple_hand if (pair1[0]) in item or (pair2[0]) in item)[:5]
            return True, rh
        return False, []

    def is_pair(self):
        pair = self.most_frequent(self.get_number(self.hand))
        if pair[1] == 2:
            rh = list(item for item in self._tuple_hand if (pair[0]) in item)[:5]
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
        self.is_set, royal_hand = self.is_royal()
        if self.is_set:
            return "ROYAL FLUSH", royal_hand, 15

        self.is_set, five_of_a_kind = self.is_num_of_a_kind(5)
        if self.is_set:
            return "FIVE OF A KIND", five_of_a_kind, 13

        self.is_set, four_of_a_kind = self.is_num_of_a_kind(4)
        if self.is_set:
            return "FOUR OF A KIND", four_of_a_kind, 11

        is_flush, flush_hand = self.is_flush()
        if is_flush:
            is_straight, straight_hand = self.is_straight()
            if is_straight:
                if self.has_sublist([14, 5, 4, 3, 2]):
                    return "BACK STRAIGHT FLUSH", flush_hand, 14
                elif all(flush_hand[i][0] == (flush_hand[i + 1][0] + 1) for i in range(len(flush_hand) - 1)):
                    return "STRAIGHT FLUSH", flush_hand, 12
            return "FLUSH", flush_hand, 9

        self.is_set, house_hand = self.is_house()
        if self.is_set:
            most_repeats = self.most_frequent([x[1] for x in house_hand])[1]
            if most_repeats == 1:
                return True, house_hand, "FULL House", 10
            else:
                return "HOUSE", house_hand, 8

        is_straight, straight_hand = self.is_straight()
        if is_straight:
            if self.has_sublist([10, 11, 12, 13, 14]):
                return "MOUNTAIN", straight_hand[:5], 7

            elif self.has_sublist([2, 3, 4, 5, 14]):
                return "BACK STRAIGHT", straight_hand, 6

            else:
                return "STRAIGHT", straight_hand, 5

        #self.is_set, three_of_a_kind = self.is_num_of_a_kind(3)
        #if self.is_set:
        #    return "THREE OF A KIND", three_of_a_kind, 4

        """self.is_set, two_pair = self.is_two_pair()
        if self.is_set:
            return "TWO PAIR", two_pair, 3

        self.is_set, pair = self.is_pair()
        if self.is_set:
            return "PAIR", pair, 2

        else:
            _, high = is_high(h)
            return "HIGH CARD", high, 1"""