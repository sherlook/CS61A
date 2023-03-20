def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result
    
def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return False

def true_func():
    "*** YOUR CODE HERE ***"
    print("Welcome to")

def false_func():
    "*** YOUR CODE HERE ***"
    print("61A")

# Q4
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x=x+1
    return x / 0

# Q5
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    k = 2
    while k<n :
        if n%k == 0:
            print("False")
            return
        else:
            k+=1 
    print("True")
    return 
    
# Q6
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    k=1
    while k<=n:
        if k%3==0 and k%5==0:
            print("fizzbuzz")
        elif k%3==0:
            print("fizz")
        elif k%5==0:
            print("buzz")
        else:
            print(k)
        k+=1



if __name__ == '__main__':
    # Q3
    # result = with_if_function()
    # print(result)
    # result = with_if_statement()

    # Q4
    # square(so_slow(5))

    # Q5
    # is_prime(15)

    # Q6
    fizzbuzz(16)