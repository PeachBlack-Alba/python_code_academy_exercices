# define a function that takes a list of number and will print the prime numbers


def isPrimeNumber(num):
    if num == 1:
        return True
    if num > 1:
        for i in range(2, num // 2 + 1):
            print("i is:", i)
            if (num % i) == 0:
                return False
        return True     
print(isPrimeNumber(1))


