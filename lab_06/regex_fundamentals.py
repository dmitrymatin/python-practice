import re


def main():
    p = re.compile("#[ABCDEF01234567890]")
    m = p.findall("#AA00FF")
    print(m)


if __name__ == "__main__":
    main()