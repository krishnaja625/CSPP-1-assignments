'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''cleaning the string
    '''
    final_string = ""
    for char in string:
        if char in "!@#$%^&*' '().":
            char = ""
            final_string = final_string+char
        else:
            final_string = final_string+char
    return final_string

def main():
    ''' take the input
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
