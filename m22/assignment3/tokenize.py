'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    line_1 = []
    line_2 = []
    list_3 = []
    dict_1 = {}
    for line in string:
        line_1 = line.split()
        line_2.append(line_1)
        for line in line_2:
            for word in line:
                if word not in list_3:
                    dict_1.keys().append(word)
                    dict_1[word] += line.count(word) 
                else:
                    dict_1[word] += line.count(word)  
    return dict_1
def main():
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    line = string.splitlines()
    print(tokenize(line))

if __name__ == '__main__':
    main()
