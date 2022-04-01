import re


def main():
    contents = ""
    with open("sample_file.txt", "r") as file:
        contents = file.read(1000000)
        print(len(contents))
    
    pattern = re.compile(r"(XYZ)+(XYZ|XY|X)")
    results = pattern.findall(contents)
    longest = max(results, key=len)

    print(longest)

if __name__ == "__main__":
    main()
