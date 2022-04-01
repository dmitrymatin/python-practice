import re


def main():
    contents = ""
    with open("sample_file.txt", "r") as file:
        contents = file.read(1000000)
        
    pattern = re.compile(r"((XYZ)+(XYZ|XY|X))", re.M)
    results = pattern.findall(contents)


    max_match = 0
    max_match_value = ""
    for res in results:
        for match in res:
            match_length = len(match)
            if match_length > max_match:
                max_match = match_length
                max_match_value = match

    print(f'longest match: {max_match}')
    print(f'the match is: {max_match_value}')


if __name__ == "__main__":
    main()