# Prime Checker
import sys


def isPrime(number: int) -> bool:

    if (number == 2):
        return True

    if (number < 2 or number % 2 == 0):
        return False

    for i in range(3, (number // 2)+1):
        if (number % i == 0):
            return False

    return True

def printPrimeCheckerPrineResult() -> callable:
    while True:
        n = int(input("Enter a number: "))
        if (n == 0):
            sys.exit(0);
        if (isPrime(n)):
            print(n, "is Prime")
        else:
            print(n, "is't prime")