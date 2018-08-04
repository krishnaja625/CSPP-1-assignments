'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
N = int(input())
n1 = N
n2 = 0
n3 = abs(N)
s = 1
while n3>=0:
    n1 = N//10
    n2 = n1%10
    s = s*n2
if N>=0:
    print(s)
else:
    print("-",s)
if __name__ == "__main__":
    main()
