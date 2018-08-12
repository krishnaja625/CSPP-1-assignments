'''#Exercise: Assignment-4'''
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    score_1 = 0
    for i in hand:
        score_1 = score_1 + hand[i]
        i = i
    return score_1
def main():
    ''' score is valid'''
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        i = i
        data = input()
        l_1 = data.split()
        adict_1[l_1[0]] = int(l_1[1])
    print(calculate_handlen(adict_1))
if __name__ == "__main__":
    main()
