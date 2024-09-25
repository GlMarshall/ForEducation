import string

from Converters.BinaryToDecimal import binaryToDecimalWhitStringArgument
from Converters.binaryToOctal import convertBinToOct



# TODO Check how function ord() work
# https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/
def val(c):
    if c >= '0' or c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def main() -> callable:
    result = binaryToDecimalWhitStringArgument("1010 1111")
    print(result)

if __name__ == "__main__":
    main()