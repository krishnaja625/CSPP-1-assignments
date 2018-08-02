'''Write a program that prints the number of times the string 'bob' occurs in s.'''

def main():
    '''Main function'''
    str1 = input()
    str2 = 'bob'
    cnt = 0
    for i in range(len(str1)-2):
        if str1[i]+str1[i+1]+str1[i+2] == str2:
            cnt = cnt+1
    print(cnt)
if __name__ == "__main__":
    main()
