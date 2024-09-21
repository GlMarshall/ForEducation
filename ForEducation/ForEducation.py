
# Prime Number Checker
def IsPrimeNumber(number: int) -> bool:
    if number >= 1:
        for i in range(2, (number // 2)+1):
            if (number % i) == 0:
                return False
            else: return True
    else: return False

def DecToBinary(number) -> str:
    result: str = ''
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result

def DecToDiffertentNumberSystems(number: int, base: int) -> str :
    result: str = ''
    while number > 0:
        result = str(number % base) + result
        number //= base
    return result


def printResultIfPrime(number: int) -> any:
    isPrime: bool = IsPrimeNumber(number)
    if (isPrime == True):
        print(number, " Is Prime")

def main():
    result = DecToDiffertentNumberSystems(72, 2)
    print(result)

if __name__ == "__main__":
    main()