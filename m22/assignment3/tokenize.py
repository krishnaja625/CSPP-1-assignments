'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def Words_list(doc):

    word = doc.lower()
    word = word.split(" ")
    words =[]
    for w in word:
        words.append(w.strip())
    words1 =[]
    regex = re.compile('[^a-z]')    
    for w in words:
        words1.append(regex.sub("", w))
    return words1

def tokenize(string):
    # line_1 = []
    # line_2 = []
    # list_3 = []
    # dict_1 = {}
    # for line in string:
    #     line_1 = line.split()
    #     line_2.append(line_1)
    #     for line in line_2:
    #         for word in line:
    #             if word not in list_3:
    #                 dict_1.append(word)
    #                 dict_1[word] += line.count(word) 
    #             else:
    #                 dict_1[word] += line.count(word)  
    # return dict_1
    dicts = {}
    word_list = Words_list(string)
    for i in word_list:
         dicts[i] = 0
    for i in words_list:
        for j in range(len(text)):
            if text[j:j+len(i)] == i:
                dicts[i] += 1
    return dicts
def main():
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    # line = string.splitlines()
    print(tokenize(string))

if __name__ == '__main__':
    main()
