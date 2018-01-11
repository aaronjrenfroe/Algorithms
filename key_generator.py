# No not that type of key generator
from itertools import combinations
"""
Given number of people who need keys => target
Given number of people required to unlock 
Returns a list of keys to give to each person so that
if number of people required to unlock are present 
they will have a combination of keys to unlock the lock
Example: You have 10 Generals and you need any combination of 6 of them in order to launch a Missile
"""

def answer(num_personel, num_required):
    # creating a list with size of num_personel
    keys = [[] for _ in range(num_personel)]  # xrange returns ints from 0...num_personel
    # number of keys each minion will have
    key_count = num_personel - (num_required - 1)
    # creating the combinations of key positions
    # "you can't just import Essay"
    combos = combinations(range(num_personel), key_count)
    # key_id is the key number: key 0, key 1, key 2..etc
    # minion_idxs are the minions who will get that key
    for key_id, idxs in enumerate(combos): # yes the varable names seem backward but the index of the value in combo is actually the key and the value is the id of the target who gets that key
        # handing out keys
        for idx in minion_idxs:
            keys[idx].append(key_id)

    # fin
    return keys

# 8 people, 2 are required to unlock
print(answer(8, 2))
