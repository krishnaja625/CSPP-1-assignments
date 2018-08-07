"""gcd"""
def gcd_iter(a_1, b_1):
    """gcd"""
    while b_1 > 0:
        r_1 = a_1%b_1
        if r_1 == 0:
            return b_1
            break
        a_1 = b_1
        b_1 = r_1
    return b_1
def main():
    """gcd"""
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
