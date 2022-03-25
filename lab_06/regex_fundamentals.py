import re


def main():
    p = re.compile("#[A-F0-9]+")
    m = p.findall("#AA00FF")
    print(m)


if __name__ == "__main__":
    main()