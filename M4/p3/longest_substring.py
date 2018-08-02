"""length"""
def main():
    """Count the occurence of the substring in a string"""
    str_ = input()
    max_str = ''
    for i in range(0, len(str_)):
        sub_str = str_[i]
        while i + 1 < len(str_) and str_[i] <= str_[i+1]:
            i += 1
            sub_str += str_[i]
        if len(sub_str) > len(max_str):
            max_str = sub_str
    print(max_str)
if __name__ == "__main__":
    main()
