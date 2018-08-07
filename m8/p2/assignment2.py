"""sum"""
def sum_of_digits(n):
    """sum"""
    while n_1>0:
        r_1 = n_1%10
        return r_1+sum_of_digits(n_1//10)
    return 0
def main():
    a_1 = input()
    print(sum_of_digits(int(a_1)))  
if __name__ == "__main__":
    main()
