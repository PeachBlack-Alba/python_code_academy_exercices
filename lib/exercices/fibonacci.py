# fibonacci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 .....
# 1. Create a class
# 2. Take variable into class initializer
# 3. Create a method for fibonacci series which takes a range of numbers.
# i.e input  = 10 , output = first 10 numbers in fibonacci series.

class FibonacciClass:
    # This line defines a class named FibonacciFunction.
    # It will be used to create instances that can generate Fibonacci series.
    def __init__(self):
        # __innit__ is a method that gets called when an instance of the class is created
        # self.limit attribute is created to store the limit value within the instance
        pass
        # pass remove functionality of method


    @staticmethod
    def generate_series(limit):
        fib_series = list()
        # fib_series is an empty list that will store the generated series
        # fib_series = [] => instead use fib_series = list()
        # dictionary_values = dict()
        # set_values = set()
        # tuple_values = tuple()
        a, b = 0, 1
        # a and b are variables used to compute the Fibonacci series
        for i in range(limit):
            fib_series.append(a)
            a, b = b, a + b
            #  We are doing tuple unpacking.
            #  The value of b is assigned to a, and the new value of a + b is assigned to b.
        return fib_series


# fib = FibonacciClass()
# fib2 = FibonacciClass()

# series = fib.generate_series(10)
# series2 = fib2.generate_series(10)
series = FibonacciClass.generate_series(10)
print(series)


# instance function => depends on the instance object of the class
# Class Function
# static function => function which do not depends on objects or class