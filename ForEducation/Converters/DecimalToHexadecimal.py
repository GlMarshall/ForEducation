import string

# Char list for char value
CHAR_LIST: str = string.digits + string.ascii_uppercase
def decimalToHexadecimalConverter(number: int) -> str:
    
    # list for result
    result_list: list[str] = []

    # Base logic
    while number > 0:
        result_list.append(CHAR_LIST[ number % 16])
        number //= 16

    # I can use result_list[::-1] but it is not interesting
    rev_list = reverseList(result_list)
    
    return ''.join(rev_list)

# This handmade reverse function
def reverseList(baseList: list[any]) -> list[any]:
    left: int = 0
    right: int = len(baseList) - 1

    # Default alg with the third variable
    while (left < right):
        temp: any = baseList[left]
        baseList[left] = baseList[right]
        baseList[right] = temp
        left += 1
        right -= 1
    return baseList


def printDecimalToHexadecimalConverter() -> callable:
    for i in range(9, 26+1):
        res = decimalToHexadecimalConverter(i)
        print(f"Dec: {i} -> Octal: {res}")