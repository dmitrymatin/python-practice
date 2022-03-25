import re


def main():
    p = re.compile("#?[A-F0-9]{6}|[A-F0-9]{3}")
    m = p.findall("#B63")
    print(m)


if __name__ == "__main__":
    main()