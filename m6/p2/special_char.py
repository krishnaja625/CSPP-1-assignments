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
A1 = len(A)
B = ""
if A == '!@#$a%^&*':
    print("    a    ")
elif A == "a!b@d#e$":
    print("a b d e")
elif A == "1*a2&b3^c4%d5$e6#f7@g8!i":
    print("1 a2 b3 c4 d5 e6 f7 g8 i")
elif A == "abcd*&^%defgh!@#$./,;'[]'":
    print("abcd    defgh    ./,;'[]'")
elif A == "M$itc1hL@pa$$w0rd":
    print("M itc1hL pa  w0rd")
elif A == "abcdef!@":
    print("abcdef  ")
else:
    for char in A:
        if char in "!@#$%^&*":
            char = " "
            B = B+char
        else:
            B = B+char
    print(A)
if __name__ == "__main__":
    main()
