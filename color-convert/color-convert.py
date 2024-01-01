import re

file_path = "color-convert/simple.css"


def read_file(fp: str) -> str:
    return open(fp, "r").read()


def hex_digit_to_dec(hex_digit, place_value=0):
    """
    convert hex digit to decimal
    """
    mappings = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    if hex_digit.isdigit():
        return int(hex_digit) * 16 ** place_value
    elif hex_digit in ["A", "B", "C", "D", "E", "F"]:
        return int(mappings[hex_digit]) * 16 ** place_value


def hex_to_dec(hex_str: str) -> int:
    """
    convert hex string to decimal
    """
    hex_str = hex_str.upper()
    hex_digits = list(hex_str)
    hex_digits.reverse()
    return sum([hex_digit_to_dec(hex_digits[i], i) for i in range(len(hex_digits))])


def hex_3_to_6(hex_str: str) -> str:
    """
    convert 3-digit hex color to 6-digit hex color
    """
    return "".join([hex_str[i]*2 for i in range(len(hex_str))])


def color_convert(re_match: re.Match) -> str:
    """
    convert color from hex to rgb
    """
    hex_str = re_match.group()[1:]
    if len(hex_str) == 3:
        hex_str = hex_3_to_6(hex_str)
    r = str(hex_to_dec(hex_str[:2]))
    g = str(hex_to_dec(hex_str[2:4]))
    b = str(hex_to_dec(hex_str[4:6]))
    return f"rgb({r}, {g}, {b})"


def main():
    css_str = read_file(file_path)
    return re.sub(pattern="#[0-9a-fA-F]+", repl=color_convert, string=css_str)


if __name__=="__main__":
    print(main())







