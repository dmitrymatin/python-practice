import re


def main():
    contents = ""
    with open("sample_file.txt", "r") as file:
        contents = file.read(1000000)
        print(len(contents))
    
    test = "XYZXYZXYXXXYYXXYZXXYXZYX"

    pattern = re.compile(r"((XYZ)+(XYZ|XY|X))", re.M)
    results = pattern.findall(contents)


    max_match = 0
    for res in results:
        for match in res:
            match_length = len(match)
            if match_length > max_match:
                max_match = match_length

    print(max_match)


if __name__ == "__main__":
    main()
