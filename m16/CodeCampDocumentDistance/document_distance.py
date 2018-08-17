'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict_1 = {}
    dict_2 = {}
    word_freq = {}
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    list_1 = dict1.split(" ")
    list_2 = dict2.split(" ")
    spl_char = "!@#$%^&*()-_+"
    for i in list_1:
        if i in spl_char:
            list_1.remove(i)
    for i in list_2:
        if i in spl_char:
            list_2.remove(i)
    list_3 = list_1 + list_2
    for i in list_1:
        dict_1[i] = list_1.count(i)
    for i in list_2:
        dict_2[i] = list_2.count(i)
    dict_3 = load_stopwords("stopwords.txt")
    for i in dict_3.keys():
        if i in dict_1.keys():
            del dict_1[i]
    for i in dict_3.keys():
        if i in dict_2.keys():
            del dict_2[i]
    for i in list_3:
        if i in list_1 and list_2:
            word_freq[i]=[list_1.count(i),list_2.count(i)]
        else:
            word_freq[i]=[list_1.count(i),list_2.count(i)]
    numer_n = 0
    for i in word_freq:
        numer_n += word_freq[i][0]*word_freq[i][1]
    denom_n1 = 0
    denom_n2s = 0
    denom_n1s = 0
    denom_n2 = 0
    denom_1 = 0
    for i in word_freq:
        denom_n1 += word_freq[i][0]**2
        denom_n2 += word_freq[i][1]**2
    denom_n1s = math.sqrt(denom_n1)
    denom_n2s = math.sqrt(denom_n2)
    denom_1 = denom_n1s*denom_n2s
    return denom_1

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
