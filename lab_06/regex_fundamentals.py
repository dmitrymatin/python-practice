import re


def main():
    p = re.compile("#?[A-F0-9]{6}")
    m = p.findall("AA00AB")
    print(m)


if __name__ == "__main__":
    main()