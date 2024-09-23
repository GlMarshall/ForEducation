# Default Converter for decimal to binary base
def decimalToBinaryConverter(number: int) -> str:
    result: str = ''
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result

# Printing Result of "decimalToBinaryConverter" function
def printDecimalToBinaryConverterResult() -> callable:
    for i in range(0, 16):
        res = decimalToBinaryConverter(i)
        print("Dec: ", i, "Bin: ", res)