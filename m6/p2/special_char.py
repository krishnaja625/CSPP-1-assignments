'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
	A = input()
	A1 = len(A)
	B = ""

	for char in A:
		if char in "!@#$%^&*' '()":
			char = " "
			B = B+char
		else:
			B = B+char
	print(B)
if __name__ == "__main__":
	main()
