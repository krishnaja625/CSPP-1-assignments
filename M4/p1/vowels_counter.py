
"""Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:"""

def main():
	s = input("enter any string")
num = 0
for letter in s:
    if letter in ('a', 'e', 'i','o', 'u', 'A', 'E', 'I','O', 'U') :
        num += 1
print('Number of vowels: ' + str(num))
if __name__== "__main__":
	main()
