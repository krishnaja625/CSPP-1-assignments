"""gcd"""
def gcd_recur(a_1, b_1):
    """gcd"""
    r_1 = a_1%b_1
    if r_1 == 0:
        return b_1
    return gcd_recur(b_1, r_1)
def main():
    """gcd"""
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
