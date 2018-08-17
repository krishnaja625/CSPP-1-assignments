'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
dic = {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6\
, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    dic = {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6\
, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    list_1 = []
    cont = 0
    for card in hand:
        list_1.append(dic[card[0]])
    list_1.sort()
    for i in range(len(list_1)-1):
        l_1 = list_1[i+1]-list_1[i]
        if l_1 == 1:
            cont = cont + 1
    if cont == (len(list_1) - 1):
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand isa flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suits = []
    for i in hand:
        suits.append(i[1])
    for i in range(len(suits)-1):
        if suits[i] != suits[i+1]:
            return False
    return True
def is_onepair(hand):
    dict1={'A':14, 'K':13, 'Q':12, 'J':11,'T':10}
    b=[]
    for i in hand:
        #print (i)
        a=i[0]
        #print(a)
        if a in dict1.keys():
            a=dict1[a]
        #print (a)
        a=int(a)
        b.append(a)
    #print(b)
    c=0
    for i in b:
        if b.count(i)==2:
            c=c+1
    if c==2:
        return True
    else:
        return False
def is_fourkind(hand):
    dict1= {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6\
, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    list_1 = []
    cont = 0
    maxhand = 0
    for card in hand:
        list_1.append(dict1[card[0]])
    list_1.sort()
    for i in list_1:
        if list_1.count(i)==4:
            cont = 1
    if cont == 1:
        if list_1[0]<list_1[4]:
            if list_1[4] > maxhand:
                return True
            else:
                maxhand = list_1[4]
                return False
        else:
            if list_1[0] > maxhand:
                return True
            else:
                maxhand = list_1[0]
                return False    

def is_fullhouse(hand):
    dict1={'A':14, 'K':13, 'Q':12, 'J':11,'T':10}
    b=[]
    for i in hand:
        #print (i)
        a=i[0]
        #print(a)
        if a in dict1.keys():
            a=dict1[a]
        #print (a)
        a=int(a)
        b.append(a)
    #print(b)
    c=0
    d=0
    for i in b:
        if b.count(i)==3:
            c=1
        if b.count(i)==2:
            d=1
    if c==1 and d==1:
        return True
    else:
        return False
def is_threekind(hand):
    dict1= {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6\
, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    list_1 = []
    cont = 0
    maxhand = 0
    for card in hand:
        list_1.append(dict1[card[0]])
    list_1.sort()
    for i in list_1:
        if list_1.count(i)==3:
            cont = 1
    c=set(list_1)
    e=len(c)
    c=0
    if cont == 1 and e==3:
        return True
    else:
        return False
def is_twopair(hand):
    dict1= {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6\
, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    list_1 = []
    cont = 0
    maxhand = 0
    for card in hand:
        list_1.append(dict1[card[0]])
    list_1.sort()
    c=set(list_1)
    d=len(c)
    c=0
    for i in list_1:
        if list_1.count(i)==2:
            c += 1
    if c == 4 and d==3:
        return True
    else:
        return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    max_1 = 0
    if is_straight(hand) and is_flush(hand):
        max_1 = 8
    elif is_fourkind(hand):
        max_1 = 7
    elif is_fullhouse(hand):
        max_1 = 6
    elif is_flush(hand):
        max_1 = 5
    elif is_straight(hand):
        max_1 = 4
    elif is_threekind(hand):
        max_1 = 3
    elif is_twopair(hand):
        max_1 = 2
    elif is_onepair(hand):
        max_1 = 1    
    else:
        max_1 = 0
    return max_1
        

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand


def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    # return max(hands, key=hand_rank)
    lst = list(map(hand_rank,hands))
    print(lst)
    maxTemp = max(lst)
    countMAx = lst.count(maxTemp)
    if countMAx == 1 :  
        return hands[lst.index(maxTemp)]
    else :
        temp_hands =[]
        for i in lst:
            if i == maxTemp:
                temp_hands.append(hands[lst.index(i)])
        # T=map(sortedList,temp_hands,)
        Temp_hands2=hands.copy()
        Temp_Ranks
        k=0
        for i in temp_hands:
            Temp_hands2[k] = sorted(i, reverse = True)
            k+=1
        TempMax = max(Temp_hands2)
        Max_index=Temp_hands2.index(TempMax)
        print(Temp_hands2[i])



if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
