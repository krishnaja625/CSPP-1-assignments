# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    """cube root"""
    s_1 = int(input("enter any number"))
    s_2 = abs(s_1)
    for guess in range(1, S_2+1):
        if(guess**3 >= s_2):
            break
        if(guess**3 == s_2):
            print("cube root is possible")
        else:
            print("cube root is not possible")
	
if __name__== "__main__":
    main()
	