from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    while x > 0:
        last, x = x % 10, x // 10
        if x % 10 > last:
            return False
        x = x // 10
    return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = 1
    while i < k + 1:
        while n % 10 > (n // 10) % 10 and n > 10:
            n = n // 10
        print("DEBUG:",n)
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    def repeat(x):
        i = 0
        while i < n:
            x = func(x)
            i = i + 1
        return x
    return repeat


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    def repeat(x):
        return func(func(x))
    return repeat


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i: lambda x: (x%i==0 or f(x)) and print(x,i))(checker, i)
        i = i+1
    return checker

    '''
    这道题第一次做没做出来
    注意调用关系 还挺复杂的
    我们的目的是在2-n找一个数字既能模n，又能模k，还要是质数
    最后返回的是只接受一个参数（k）的checker，他是通过fx层层嵌套出来的
    因为是一路累加上去的 所以不需要看是否为质数
    还是画个调用图比较方便看
    来自gpt当检查到一个新的质数 i 时，它将 checker 作为参数传递给一个新的 lambda 函数，该函数接受一个函数 f 和一个数字 i 作为参数，并返回一个新的 lambda 函数，该函数接受一个参数 x，并将 (x % i == 0 or f(x)) and print(x, i) 作为结果返回。换句话说，新的 lambda 函数将 f 应用于 x，并检查 x 是否为 i 的倍数。如果是，则返回 True，否则返回 f(x) 的结果。此外，它还将 (x, i) 打印到屏幕上，以便在调试时进行跟踪。
    有点递归
    '''


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = ____________________________
    while ____________________________:
        if not checker(i):
            def outer(____________________________):
                def inner(____________________________):
                    return ____________________________
                return ____________________________
            checker = ____________________________
        i = ____________________________
    return ____________________________
