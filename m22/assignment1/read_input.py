'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    # N_1 = int(input())
    # while N_1 > 0:
    # 	Inp_1 = input()
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
