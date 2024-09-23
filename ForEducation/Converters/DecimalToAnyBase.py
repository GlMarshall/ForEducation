# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!

# I was going to wrote alg for any base, but i don't know at all
# How work numeral systems greater than sixty four base.
# The count of the all char. available for us is 62


# As far as i understand, this alg can with any base when it's less than 62

import string

# Constants
MAX_BASE: int = 62
CHAR_LIST: str = string.digits + string.ascii_uppercase + string.ascii_lowercase


def decimalToSixtyTowAndLess(number: int, base: int) -> str:
    # Checking the base value cuz base cannot be greater than sixty two.
    # Elnglish alphabet with digits have 62 char
    if (base > MAX_BASE):
        return "Base cannot be larger than 62"

    # Check sign. I don't know why i using this check, but... why not
    # Someone did it... Why i'am worse? LOL
    if number < 0:
        sign: int = -1
    elif number == 0:
        return CHAR_LIST[0]
    else:
        sign = 1

    number *= sign

    # Initialize list for results
    # I use data type 'list' cuz it's more confortable for me
    digits_result_list: list[str] = []

    # Base logic is the same as with the other converters
    while number > 0:
        digits_result_list.append(CHAR_LIST[number % base])
        number //= base

    # Add sign if necessary
    if sign < 0:
        digits_result_list.append('-')

    # Reverse
    digits_result_list.reverse()

    # And return result
    return ''.join(digits_result_list)