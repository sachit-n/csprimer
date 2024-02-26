def convert_to_roman(n):
    """
    convert number to roman numeral, e.g. 243 -> CCXLIII
    """

    units_map = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens_map = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds_map = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "DM"]
    thousands_map = ["", "M", "MM", "MMM"]

    if n >= 4000:
        return "out of bound"

    roman_table = [units_map, tens_map, hundreds_map, thousands_map]

    out = ""
    curr_dig_pos = 0
    while n > 0:
        curr_digit = n % 10
        out += roman_table[curr_dig_pos][curr_digit]
        curr_dig_pos += 1
        n = n // 10

    return out[::-1]


print(convert_to_roman(123))


