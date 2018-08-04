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
n3 = int(input())
n2 = n3
n = abs(n3)
s = 0
k = 0
if n>0:
    s=1
while n>0:
    n2 = n%10
    s = s*n2
    n = n//10
if n3 >= 0:
    print(s)
else:
    k = -1*s
    print(k)
if __name__ == "__main__":
    main()
