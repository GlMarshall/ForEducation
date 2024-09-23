import string

from Converters.DecimalToAnyBase import decimalToSixtyTowAndLess
from Converters.DecimalToHexadecimal import printDecimalToHexadecimalConverter


def main() -> callable:
    print(decimalToSixtyTowAndLess(2567 ,62))

if __name__ == "__main__":
    main()