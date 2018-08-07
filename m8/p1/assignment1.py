"""er and returns one number."""
def factorial(n_1):
    '''
    fact
    '''
    # Your code here
    if n_1 in (0, 1):
        return 1
    return n_1*factorial(n_1-1)
def main():
    ''' fact '''
    a_1 = input()
    print(factorial(int(a_1)))
if __name__ == "__main__":
    main()
    