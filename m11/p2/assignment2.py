"""Exercise: Assignment-2"""
def update_hand(hand_1, word_1):
    """a2"""
    h_2 = hand_1
    for i in word_1:
        if i in h_2:
            h_2[i] = h_2[i]-1
    return h_2
def main():
    """string"""
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        data = input()
        l_1 = data.split(" ")
        adict_1[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict_1, data1))
if __name__ == "__main__":
    main()
