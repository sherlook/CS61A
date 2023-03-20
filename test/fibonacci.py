from operator import mul

def fibonacci(n):

    pred = 0
    curr = 1
    k = 1

    while k<n:
        pred, curr = curr, pred+curr
        k += 1

    return curr

def fibonacci1(n):

    pred = 1
    curr = 0
    k = 0

    while k<n:
        pred, curr = curr, pred+curr
        k += 1

    return curr

def func(i):
    return i

def generalizing(n):
    i = 1
    sum=0
    while i<=n:
        sum+=func(i)
        i+=1

    return sum

def cube(i):
    return pow(i, 3)

def summation (n, term):
    total, k = 0,1
    while k<=n:
        total ,k = total + term(k), k+1
    return total

def pi_term(i):
    return 8/ mul(4*i-3, 4*i-1)
    
def make_adder(n):
    """Return a function 
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def add(k): 
        return k+n
    return add



if __name__ == '__main__':
    # 0,1,1,2,3,5,8,13,....
    print(fibonacci(0)) # n=0时出错
    print(fibonacci1(0))

    print(generalizing(5))


    # 只需要修改参数term 不需要修改函数内部
    print(summation(5, cube))

    print("pi近似:",summation(1000000, pi_term))

    print("make_adder", make_adder(2000)(23))

    f = make_adder(2000)

    print("f",f(23))








