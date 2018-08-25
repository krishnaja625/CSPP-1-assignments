'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    ''' to take input
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
