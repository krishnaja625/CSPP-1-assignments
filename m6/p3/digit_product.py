'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    N3 = int(input())
    N2 = N3
    N = abs(N3)
    S = 0
    K = 0
    if N > 0:
        S = 1
    while N > 0:
        N2 = N%10
        S = S*N2
        N = N//10
    if N3 >= 0:
        print(S)
    else:
        K = -1*S
        print(K)
if __name__ == "__main__":
    main()
