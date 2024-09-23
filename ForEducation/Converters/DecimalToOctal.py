# Converting for Decimal to Octal
# This Converter uses Difault logic but with list
def decimalToOctalConveter(number: int) -> str:
    if (number == 0):
        return str(0)

    ocatalNum_list: list[str] = []

    k: int = 1
    # Result variable
    a: int = 0

    # Base logic with int variable
    while number > 0:
        a: int = a + (number % 8) * k
        k *= 10
        number //= 8

    return str(a)

def printDecimalToOctalConveter() -> callable:
    for i in range(0, 16+1):
        res = decimalToOctalConveter(i)
        print(f"Dec: {i} -> Octal: {res}")