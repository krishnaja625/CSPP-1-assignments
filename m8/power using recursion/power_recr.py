# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def recurPower(base_, exp_1):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp_1 == 0:
        return 1
    #if exp_1 == 1:
        #return base_
    else:
        return base_*recurPower(base_, exp_1-1)
    

def main():
    data = input()
    data = data.split( )
    print(recurPower(float(data[0]),int(data[1])))   

if __name__== "__main__":
    main()