'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
A = input()
a= len(A)
for i in range(0, a):
    if A[i] == "!@#$%^&*":
        A = A[0:i-1]+" "+A[i+1:a]
print(A)
if __name__ == "__main__":
    main()
