"""# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube"""

def main():
    """cube root"""
    s_1 = int(input())
    s_2 = abs(s_1)
    guess = 1
    for guess in range(1, s_2+1):
        if guess**3 >= s_2:
            break
    if guess**3 == s_2:
        print(s_2, "is a perfect cube")
    else:
        print(s_2, "is not a perfect cube")
if __name__ == "__main__":
    main()
	