import math
def getOp():
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 squaring")
    print("6 absolute value")
    print("7 factorial")
    print("8 exp(x)")
    print("9 ln(x)")
    print("10 all arithmetic operations")
    print("Choose the number of the desired operation: ", end='')
    return int(input())

def inputBinaryOp():
    print("Enter the first number: ", end='')
    n1 = float(input())
    print("Enter the second number: ", end='')
    n2 = float(input())
    return n1, n2

def inputUnaryOp():
    print("Enter a number: ", end='')
    return float(input())

def execOp(op):
    if op >= 1 and op <= 4:
        n1, n2 = inputBinaryOp()
        if op == 1:
            print(f'{n1}+{n2} = {n1+n2}')
        if op == 2:
            print(f'{n1}-{n2} = {n1-n2}')
        if op == 3:
            print(f'{n1}*{n2} = {n1*n2}')
        if op == 4:
            if n2 == 0:
                print("Can't divide by zero!")
                return
            print(f'{n1}/{n2} = {n1/n2}')
    elif op <= 9:
        n = inputUnaryOp()
        if op == 5:
            print(f'{n}^2 = {n*n}')
        if op == 6:
            print(f'|{n}| = {abs(n)}')
        if op == 7:
            if n % 1 != 0:
                print("The number must be an integer for factorial!")
                return
            if n < 0:
                print("The number must be a positive integer!")
                return
            print(f'{int(n)}! = {math.factorial(int(n))}')
        if op == 8:
            print(f'exp({n}) = {math.exp(n)}')
        if op == 9:
            if n <= 0:
                print("The number must be positive for ln!")
                return
            print(f'ln({n}) = {math.log(n)}')
    elif op == 10:
        n1, n2 = inputBinaryOp()
        print(f'{n1}+{n2} = {n1 + n2}')
        print(f'{n1}-{n2} = {n1 - n2}')
        print(f'{n1}*{n2} = {n1 * n2}')
        if n2 == 0:
            print("Can't divide by zero!")
            return
        print(f'{n1}/{n2} = {n1 / n2}')
    else:
        print('No such operation\n')
        op = getOp()
        execOp(op)

op = getOp()
execOp(op)