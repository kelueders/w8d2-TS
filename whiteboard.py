# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine 
# the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, 
# assuming that only gloves of the same color can form pairs. 

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# output = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# output = 3 (3 red pairs)


def solution(arr):
    gloves_dict = {}
    num_pairs = 0

    if len(arr) == 0:
        return 0
    
    for glove in arr:
        if glove not in gloves_dict:
            gloves_dict[glove] = 1
        else:
            gloves_dict[glove] += 1

    for num in gloves_dict.values():
        num_pairs += num // 2

    return num_pairs

# arr = ["red", "green", "red", "blue", "blue"]

# print(solution(arr))


