import re

file_path = "color-convert/simple.css"


def read_file(fp: str) -> str:
    return open(fp, "r").read()


def color_convert(string: str) -> str:
    return "foo"


def main():
    css_str = read_file(file_path)
    return re.sub(pattern="#[0-9a-fA-F]+", repl=color_convert, string=css_str)


if __name__=="__main__":
    print(main())







