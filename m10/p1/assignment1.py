'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    var_1 = list(string.ascii_lowercase)
    var_2 = list(letters_guessed)
    keys_1 = []
    keys_2 = []
    a = ""
    for i in var_1:
        keys_1.append(ord(i))
    dict_1 = dict(zip(keys_1, var_1))
    for i in var_2:
        keys_2.append(ord(i))
    dict_2 = dict(zip(keys_2, var_2))
    for i in dict_2:
        del dict_1[i]
    list1 = []
    for i in dict_1.values():
        list1.append(i)
    return a.join(list1)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char)
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
