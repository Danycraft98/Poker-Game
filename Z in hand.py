from collections import Counter


def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0]

def second_Most_Common(lst):
    data = Counter(lst)
    return (Counter(lst).most_common(2)[1])


def is_flush_Z(h):

#Hand with 4 same suited cards will become "FLUSH"
    i = Most_Common([x[1] for x in h])
    b = [item for item in h if (i[0]) in item]
    c = Most_Common([x[1] for x in b])
    j = list(item for item in h if c[0] in item)[:5]
    z =  ['Z⦿']
    rh = b + z
    

    if (c[1]) >= 4:
        return True, rh, ("FLUSH")

    else:
        return False, []

def is_four_kind_Z(h):

#Four of a Kind with Z will become "FIVE OF A KIND"
    i = Most_Common([a[:-1] for a in h])
    j = list(item for item in h if i[0] in item)[:5]
    z =  ['Z⦿']
    rh = j + z

    if i[1] == 4:
        return True, rh, ("FIVE OF A KIND")

    else:
        return False, []
    
def is_three_kind_Z(h):

#Three of a Kind with Z will become "FOUR OF A KIND"
    i = Most_Common([a[:-1] for a in h])
    j = list(item for item in h if i[0] in item)[:5]
    c = [item for item in h if (j[0][0]) not in item]
    d = sorted((c), reverse=True)[:1]
    z =  ['Z⦿']
    rh = j + z + d

    if i[1] == 3:
        return True, rh, ("FOUR OF A KIND")

    else:
        return False, []

def is_two_pair_Z(h):

#Two Pair hand with Z will either become "HOUSE" or "FULL HOUSE"

    pair1 = Most_Common([x[0] for x in h])

    pair2 = second_Most_Common([x[0] for x in h])


    if pair1[1] == 2 and pair2[1] == 2:


        rh = sorted(list(item for item in h if (pair1[0]) in item or (pair2[0]) in item))[:5]
        z =  ['Z⦿']
        rh = rh + z
        
        if (len(list(item for item in rh if (rh[0][1]) in item))) == 1:
            return True, rh, ("FULL HOUSE")

        return True, rh, ("HOUSE")
    return False, []


def is_pair_Z(h):

#Pair hand with Z will become "THREE OF A KIND"
    
    pair = Most_Common([x[0] for x in h])
    if pair[1] == 2:

        z_value = (pair[0])
        z = ['Z⦿']
        c = [item for item in h if (pair[0]) not in item]
        d = sorted((c), reverse=True)[:2]
        f = list(item for item in h if (pair[0]) in item)[:5]

        rh = f + z + d
        return True, rh, ("THREE OF A KIND")
    return False, []


def is_high_Z(h):

#High hand with Z will become either family of "STRAIGHT" or "ONE PAIR"
    h = list(item for item in h)
    rh = sorted((h), reverse=True)[:1]
    z = ['Z⦿']
    c = [item for item in h if (rh[0]) not in item]
    d = sorted((c), reverse=True)[:3]
    rh = rh + z + d
    return True, rh, ("ONE PAIR")

h = ['9H', '3S', '8S', 'QS', '2D', '4D', 'AX']

print (is_high_Z(h))
