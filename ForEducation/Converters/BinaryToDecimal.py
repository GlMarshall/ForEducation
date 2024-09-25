
# This alg is actualy work... but obviously, we give a string type argument into the function, not int
def binaryToDecimal(binary: int) -> int:
    result: int = 0
    power_variable: int = 0
    while (binary > 0):
        remainder: int = binary % 10
        result = result + remainder * myPower(2, power_variable)
        power_variable += 1
        binary //= 10
    return result


# This is mostly right alg
def binaryToDecimalWhitStringArgument(binary: str) -> int:

    if (checkWhitespaceInString(binary)):
        binary = removeWhitespaceInBinaryNumber(binary)

    result: int = 0
    binary_len: int = len(binary)
    i: int = 1
    power_variable: int = 0
    while (i <= binary_len):
        dec = int(binary[-i])
        result = result + dec * myPower(2, power_variable)
        power_variable += 1
        i += 1
    return result


# My power function. Just for fun
def myPower(base: int, power: int) -> int:
    result: int = 1
    for i in range(power):
        result *= base
    return result

def removeWhitespaceInBinaryNumber(binary: str) -> str:
    result: str = ""
    for i in range(0, len(binary)):
        if (binary[i] == ' '):
            result += ''
        else:
            result += binary[i]
    return ''.join(result)

def checkWhitespaceInString(base_str: str) -> bool:
    whitespace_count: int = 0
    for i in range(0, len(base_str)):
         if (base_str[i] == ' '):
             whitespace_count += 1
    if whitespace_count > 0:
        return True
    else: False