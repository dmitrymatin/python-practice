import re


def main():
    p = re.compile("^\s*#?([A-F0-9]{6}|[A-F0-9]{3})\s*$", re.I)
    print(p.findall("#b63"))
    print(p.findall("  #aBCd84  ")) # should match even with whitespace
    print(p.findall("3F")) # no match
    print(p.findall("blue")) # no match
    print(p.findall("xYz87k")) # no match
    print(p.findall("test # ab12587")) # matches found
    print(p.findall("#ABCDEF123456 test")) # matches found
    print(p.findall("<script style=\"color: #005599;\"> ... </script>")) # matches found


if __name__ == "__main__":
    main()