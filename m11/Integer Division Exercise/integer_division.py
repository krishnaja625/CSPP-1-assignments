'''
#Exercise: Integer Division Exercise
#Modify the code for integer_division
so that this error does not occur.
@ author SupriyaMadupathi
'''

def integer_division(x_1, a_int):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    cnt = 0
    while x_1 >= a_int:
        cnt += 1
        x_1 = x_1 - a_int
    return cnt
def main():
    '''
    SupriyaMadupathi
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__ == "__main__":
    main()
