'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
	B = ""
	for char in string:
		if char in "!@#$%^&*' '().":
			char = ""
			B = B+char
		else:
			B = B+char
	return B

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
