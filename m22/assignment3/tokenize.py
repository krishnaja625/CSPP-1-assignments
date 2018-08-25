'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def Words_list(doc):

    final_string = ""
    for char in doc:
        if char in '";\n,':
            char = ""
            final_string = final_string+char
        else:
            final_string = final_string+char
    word = final_string.split(" ")
    for w in word:
        words.append(w.strip())
    return word

def tokenize(string):

    dicts = {}
    dicts = {x:string.count(x) for x in string}
    # for i in string:
    #      dicts[i] = 0
    # for i in string:
    #     for j in range(len(line)):
    #         if line[j:j+len(i)] == i:
    #             dicts[i] += 1
    return dicts
def main():
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    # line = string.splitlines()

    print(tokenize(Words_list(string)))

if __name__ == '__main__':
    main()
