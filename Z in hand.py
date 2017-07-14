from collections import Counter


def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0]

def second_Most_Common(lst):
    data = Counter(lst)
    return (Counter(lst).most_common(2)[1])


def is_flush_Z(h):

    i = Most_Common([x[1] for x in h])
    b = [item for item in h if (i[0]) in item]
    c = Most_Common([x[1] for x in b])
    j = list(item for item in h if c[0] in item)[:5]
    k =  ['Z⦿']
    rh = b + k
    

    if (c[1]) >= 4:
        return True, rh, ("FLUSH")

    else:
        return False, []

def is_four_kind_Z(h):

#Four of a Kind with Z will become "FIVE OF A KIND"
    i = Most_Common([a[:-1] for a in h])
    j = list(item for item in h if i[0] in item)[:5]
    k =  ['Z⦿']
    rh = j + k

    if i[1] == 4:
        return True, rh, ("FIVE OF A KIND")

    else:
        return False, []
    
def is_three_kind_Z(h):

#Three of a Kind with Z will become "FOUR OF A KIND"
    i = Most_Common([a[:-1] for a in h])
    j = list(item for item in h if i[0] in item)[:5]
    k =  ['Z⦿']
    rh = j + k

    if i[1] == 3:
        return True, rh, ("FOUR OF A KIND")

    else:
        return False, []

def is_two_pair_Z(h):

#Two Pair hand with Z will either become "HOUSE" or "FULL HOUSE"

    pair1 = Most_Common([x[0] for x in h])

    pair2 = second_Most_Common([x[0] for x in h])


    if pair1[1] == 2 and pair2[1] == 2:

        e = ['Z⦿']
        f = list(item for item in h if (pair1[0]) in item or (pair2[0]) in item)[:5]
        rh = e + f

        i = Most_Common([x[1] for x in f])
        b = [item for item in f if (i[0]) in item]
        c = Most_Common([x[1] for x in b])

        if c[1] == 1:
            return True, rh, ("FULL HOUSE")

        return True, rh, ("HOUSE")
    return False, []


def is_pair_Z(h):

#Pair hand with Z will become "THREE OF A KIND"
    
    pair = Most_Common([x[0] for x in h])
    if pair[1] == 2:

        z_value = (pair[0])
        e = ['Z⦿']
        c = [item for item in h if (pair[0]) not in item]
        d = sorted((c), reverse=True)[:2]       
        f = list(item for item in h if (pair[0]) in item)[:5]

        rh = d + f + e
        return True, rh, ("THREE OF A KIND")
    return False, []    

h = ['7S', 'KS', '3S', 'JH', '3C', 'QD', '5X']

print (is_pair_Z(h))
