'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

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
    lines = [line.split() for line in string.split('\n')]

    for i in range(len(lines)):
        for word in lines[i]:
            # if the word is not in the dictionary, create the entry
            # word = word.lower()
            if word not in words:
                words[word] = {'count':0, 'lines':set()}

            # update the count and add the line number to the set
            words[word]['count'] += 1
            words[word]['lines'].add(i+1)
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
