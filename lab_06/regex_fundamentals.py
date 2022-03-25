import re


def main():
    p = re.compile("#?([A-F0-9]{6}|[A-F0-9]{3})")
    m = p.findall("#B63")
    print(m)

    p = re.compile(r'\d+')
    m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    print(m)


if __name__ == "__main__":
    main()