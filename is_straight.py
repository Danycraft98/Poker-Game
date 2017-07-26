h = [(4 , '✙'), (7, '✙'), (6, '⦿'), (2, '✙'), (8, '♣'), (5 , '♥'), (3 , '♦')]


def is_straight(h):

    d = (sorted(set([x[0] for x in h])))
    rh = []

        
    for n in range(0, 10):
        temp_set = list(set(range(n, n+5)))
        if set(temp_set).issubset(d) is True:
            result = (temp_set)

    result = tuple(result)

    for x in result:
        c = [item for item in h if (x) in item]
        [thing] = c; ('(' +str(thing) + ')')
        rh.append(thing)

    if len(rh) == 5:
        return rh
    else:
        return False, []

print (is_straight(h))
