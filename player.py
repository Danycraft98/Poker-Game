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

    def is_top_straight_Z(self):
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            sorted(self.tuple_hand, key=lambda card: card[0], reverse=True)
            potential_sf = self.most_frequent(self.get_suits(self.tuple_hand ))
            
            if potential_sf[1] >= 5:
                potential_sf_hand_set = [item for item in list_without_15 if (potential_sf[0]) in item]
                potential_sf_hand = sorted(set([x[0] for x in potential_sf_hand_set]))

                rh = [] 
                es = [11, 12, 13, 14]
                bs = [2, 3, 4, 5, 14]


                if (all(x in (potential_sf_hand) for x in es)) is True:
                    
                    for x in range (0, 4):
                        true_hand = [item for item in potential_sf_hand_set if (es[x]) in item]
                        rh.append(true_hand)

                    rh = [val for sublist in rh for val in sublist]
                    rh = rh + [(15, '⦿')]
                    return True, rh
                
                if (all(x in (potential_sf_hand) for x in bs)) is True or sum(map(lambda x: x in potential_sf_hand, bs)) == 4:

                    result = []
                    
                    for x in range (0, 5):
                        true_hand = [item for item in potential_sf_hand_set if (bs[x]) in item]
                        result.append(true_hand)


                    last = [elem if elem else [('Z', '⦿')] for elem in result]
                    rh = [val for sublist in last for val in sublist]
                    return True, rh               

                else:
                    missing_numbers = [item for item in set(range(1, 15)) if item not in potential_sf_hand]
                    list_of_potential_straights = []
                    list_of_potential_straight_hands = []
                    list_of_straight_sets = []

                    for x in reversed(range(len(missing_numbers))):
                        missing_individual_numbers = [(missing_numbers[x])]
                        potential_straights = list(sorted(missing_individual_numbers + potential_sf_hand))
                        list_of_potential_straights.append(potential_straights)

                    for list_of_potential_straights in list_of_potential_straights:
                        for start_index in range(len(list_of_potential_straights) - 4):
                            end_index = start_index + 5
                            sublist = list_of_potential_straights[start_index:end_index]
                            list_of_potential_straight_hands.append(sublist)
                    
                    for n in range(2, 11):
                        straight_set = list(set(range(n, n+5)))
                        list_of_straight_sets.append(straight_set)

                    straight_hands = [x for x in list_of_potential_straight_hands if x in list_of_straight_sets]

                    if len(straight_hands) >= 1:
                        highest_hand = (max(map(lambda x: x, straight_hands)))

                        result = []
                        
                        for x in range (0, 5):
                            true_hand = [item for item in potential_sf_hand_set if (highest_hand[x]) in item]
                            result.append(true_hand)

                        last = [elem if elem else [('Z', '⦿')] for elem in result]
                        rh = [val for sublist in last for val in sublist]

                        return True, rh
                    return False, []
            else:
                return False, []           
        return False, []

    def is_straight_Z(self):
        if ([x[0] for x in self.tuple_hand if (15) in x]):
            list_without_15 = [item for item in self.tuple_hand if (15) not in item]
            pure_list = sorted(set([x[0] for x in list_without_15]))
            #because straight doesn't go up to 15
            rh = []

            # back_straight_check
            bs = [2, 3, 4, 5, 14]
            if (all(x in (pure_list) for x in bs)) is True or sum(map(lambda x: x in pure_list, bs)) == 4:
                seen = set()
                keep = []
                for num, suit in self.tuple_hand:
                    if num in seen:
                        continue
                    else:
                        seen.add(num)
                        keep.append((num, suit))

                self.tuple_hand = keep
                
                for x in range (0, 5):
                    true_hand = [item for item in self.tuple_hand if (bs[x]) in item]
                    rh.append(true_hand)
            
                rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                rh = [val for sublist in rh for val in sublist]
                return True, rh
            
                suits = [x[-1] for x in rh]
                data = Counter(suits)
                potential_sf = self.most_frequent(1)[0]

                if potential_sf[1] == 5:
                    return True, rh
                
                if potential_sf[1] == 4:
                    sf_hand = [item for item in rh if (potential_sf[0]) in item]
                    rh = []
                    for x in range (0, 5):
                        true_hand = [item for item in sf_hand if (bs[x]) in item]
                        rh.append(true_hand)

                    rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                    rh = [val for sublist in rh for val in sublist]
    
            else:
                missing_numbers = [item for item in set(range(1, 15)) if item not in pure_list]
                
                list_of_potential_straights = []
                result = []
                list_of_potential_straight_hands = []
                list_of_straight_sets = []

                for x in reversed(range(len(missing_numbers))):
                    missing_individual_numbers = [(missing_numbers[x])]
                    potential_straights = list(sorted(missing_individual_numbers + pure_list))
                    list_of_potential_straights.append(potential_straights)

                for list_of_potential_straights in list_of_potential_straights:
                    for start_index in range(len(list_of_potential_straights) - 4):
                        end_index = start_index + 5
                        sublist = list_of_potential_straights[start_index:end_index]
                        list_of_potential_straight_hands.append(sublist)
                
                for n in range(2, 11):
                    straight_set = list(set(range(n, n+5)))
                    list_of_straight_sets.append(straight_set)

                straight_hands = [x for x in list_of_potential_straight_hands if x in list_of_straight_sets]

                if len(straight_hands) >= 1:
                    highest_hand = (max(map(lambda x: x, straight_hands)))
                    seen = set()
                    keep = []
                    for num, suit in self.tuple_hand:
                        if num in seen:
                            continue
                        else:
                            seen.add(num)
                            keep.append((num, suit))
                            
                    self.tuple_hand = keep
                
                    for x in range (0, 5):
                        true_hand = [item for item in self.tuple_hand if (highest_hand[x]) in item]
                        rh.append(true_hand)

                    rh = [elem if elem else [('Z', '⦿')] for elem in rh]
                    rh = [val for sublist in rh for val in sublist]
                    return True, rh
                return False, []
        return False, []



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
            

    def is_top_straight(self):

        sorted(self.tuple_hand, key=lambda card: card[0], reverse=True)
        is_sf = self.most_frequent(self.get_suits(self.tuple_hand))

        if is_sf[1] >= 5:
            is_sf_hand_set = [item for item in self.tuple_hand if (is_sf[0]) in item]
            is_sf_hand = sorted(set([x[0] for x in is_sf_hand_set]))

            rh = [] 
            bs = [2, 3, 4, 5, 14]
            
            if (all(x in (is_sf_hand) for x in bs)) is True:
                
                for x in range (0, 5):
                    true_hand = [item for item in is_sf_hand_set if (bs[x]) in item]
                    rh.append(true_hand)

                rh = [val for sublist in rh for val in sublist]
                return True, rh               

            else:
                list_of_is_straight_hands = []
                list_of_straight_sets = []

                for start_index in range(len(is_sf_hand) - 4):
                        end_index = start_index + 5
                        sublist = is_sf_hand[start_index:end_index]
                        list_of_is_straight_hands.append(sublist)
                
                for n in range(2, 11):
                    straight_set = list(set(range(n, n+5)))
                    list_of_straight_sets.append(straight_set)

                straight_hands = [x for x in list_of_is_straight_hands if x in list_of_straight_sets]

                if len(straight_hands) >= 1:
                    
                    highest_hand = (max(map(lambda x: x, straight_hands)))
                    
                    for x in range (0, 5):
                        true_hand = [item for item in is_sf_hand_set if (highest_hand[x]) in item]
                        rh.append(true_hand)

                    rh = [val for sublist in rh for val in sublist]

                    return True, rh
                return False, []
        return False, []           

    def is_straight(self):
        pure_list = sorted(set([x[0] for x in self.tuple_hand]))

        rh = []

        # back_straight_check
        bs = [2, 3, 4, 5, 14]
        if (all(x in (pure_list) for x in bs)) is True:
            seen = set()
            keep = []
            for num, suit in self.tuple_hand:
                if num in seen:
                    continue
                else:
                    seen.add(num)
                    keep.append((num, suit))
                
            self.tuple_hand = keep
            for x in range (0, 5):
                true_hand = [item for item in self.tuple_hand if (bs[x]) in item]
                rh.append(true_hand)

            rh = [val for sublist in rh for val in sublist]
            return True, rh
    
        else:
            list_of_is_straight_hands = []
            list_of_straight_sets = []

            for start_index in range(len(pure_list) - 4):
                    end_index = start_index + 5
                    sublist = pure_list[start_index:end_index]
                    list_of_is_straight_hands.append(sublist)
            
            for n in range(2, 11):
                straight_set = list(set(range(n, n+5)))
                list_of_straight_sets.append(straight_set)

            straight_hands = [x for x in list_of_is_straight_hands if x in list_of_straight_sets]

            if len(straight_hands) >= 1:
                seen = set()
                keep = []
                for num, suit in self.tuple_hand:
                    if num in seen:
                        continue
                    else:
                        seen.add(num)
                        keep.append((num, suit))
                    
                self.tuple_hand = keep
                
                highest_hand = (max(map(lambda x: x, straight_hands)))
                
                for x in range (0, 5):
                    true_hand = [item for item in self.tuple_hand if (highest_hand[x]) in item]
                    rh.append(true_hand)

                rh = [val for sublist in rh for val in sublist]

                return True, rh
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

        e_straight = [11, 12, 13, 14, 15]
        r_straight = [10, 11, 12, 13, 14]
        b_straight = [2, 3, 4, 5, 14]

        is_top_straight_Z, top_straight_Z = self.is_top_straight_Z()
        if is_top_straight_Z:
            if (list(x[0] for x in  top_straight_Z)) == e_straight:
                return "EMPEROR STRAIGHT FLUSH", top_straight_Z, 15          
            if (list(x[0] for x in  top_straight_Z)) == r_straight or sum(map(lambda x: x in (list(x[0] for x in  top_straight_Z)), r_straight)) == 4:
                return "ROYAL STRAIGHT FLUSH", top_straight_Z, 14
            if (list(x[0] for x in  top_straight_Z)) == b_straight or sum(map(lambda x: x in (list(x[0] for x in  top_straight_Z)), b_straight)) == 4:
                return "BACK STRAIGHT FLUSH", top_straight_Z, 12
            else:
                return "STRAIGHT FLUSH", top_straight_Z, 11          
        
        is_straight_Z, straight_Z = self.is_straight_Z()
        if is_straight_Z:
            if (list(x[0] for x in  straight_Z)) == r_straight or sum(map(lambda x: x in (list(x[0] for x in  straight_Z)), r_straight)) == 4:
                return "ROYAL STRAIGHT", straight_Z, 9
            if (list(x[0] for x in  straight_Z)) == b_straight or sum(map(lambda x: x in (list(x[0] for x in  straight_Z)), b_straight)) == 4:
                return "BACK STRAIGHT", straight_Z, 8
            else:
                return "STRAIGHT", straight_Z, 7

                
        is_4_kind_Z, four_of_a_kind_Z = self.is_4_kind_Z()
        if is_4_kind_Z:
            return "FIVE OF A KIND", four_of_a_kind_Z, 13

        is_two_pair_Z, two_pair_Z = self.is_two_pair_Z()
        if is_two_pair_Z:
            return "FULL HOUSE", two_pair_Z, 8
            
        is_3_kind_Z, three_kind_Z = self.is_3_kind_Z()
        if is_3_kind_Z:
            return "FOUR OF A KIND", three_kind_Z, 10

        is_flush_Z, flush_hand = self.is_flush_Z()
        if is_flush_Z:
            return "FLUSH", flush_hand, 9

        is_pair_Z, pair_Z = self.is_pair_Z()
        if is_pair_Z:
            return "THREE OF A KIND", pair_Z, 4

        is_high_Z, high_Z = self.is_high_Z()
        if is_high_Z:
            return "ONE PAIR", high_Z, 1


        is_top_straight, top_straight = self.is_top_straight()
        if is_top_straight:          
            if (list(x[0] for x in  top_straight)) == r_straight:
                return "ROYAL STRAIGHT FLUSH", top_straight, 14
            if (list(x[0] for x in  top_straight)) == b_straight:
                return "BACK STRAIGHT FLUSH", top_straight, 12
            else:
                return "STRAIGHT FLUSH", top_straight, 11
            
        is_five_of_a_kind, five_of_a_kind = self.is_num_of_a_kind(5)
        if is_five_of_a_kind:
            return "FIVE OF A KIND", five_of_a_kind, 13
        
        is_straight, straight_hand = self.is_straight()
        if is_straight:
            if (list(x[0] for x in  straight_hand)) == r_straight:
                return "ROYAL STRAIGHT", straight_hand, 9
            if (list(x[0] for x in  straight_hand)) == b_straight:
                return "BACK STRAIGHT", straight_hand, 8
            else:
                return "STRAIGHT", straight_hand, 7           
        
        is_four_of_a_kind, four_of_a_kind = self.is_num_of_a_kind(4)
        if is_four_of_a_kind:
            return "FOUR OF A KIND", four_of_a_kind, 10

        is_flush, flush_hand = self.is_flush()
        if is_flush:
            return "FLUSH", flush_hand, 9

        is_house, house_hand = self.is_house()
        
        if is_house:
            return "FULL HOUSE", house_hand, 8

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
