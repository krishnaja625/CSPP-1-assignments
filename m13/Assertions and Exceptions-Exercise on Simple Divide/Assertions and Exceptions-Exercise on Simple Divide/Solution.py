#define the simple_divide function here
# def simple_divide(item, denom):

def fancy_divide(list_of_numbers, index):
    li = []
    denom = list_of_numbers[index]
    for i in range(len(list_of_numbers)):
        try:
            li.append(list_of_numbers[i]/float(denom))
        except ZeroDivisionError:
            li.append(0)
    return li

def main():
    data = int(input())
    l1=[]
    for i in range(data):
        j = float(input())
        l1.append(float(j))
    s=input()
    index=int(s)
    print(fancy_divide(l1, index))

if __name__== "__main__":
    main()
    