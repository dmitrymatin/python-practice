from sys import byteorder


def main():
    num_scanners = 6
    scanners = []
    for i in range(num_scanners):
        scanners.append(
            {
                "name": f"scanner{i * 10}",
                "price": (i ^ 1) << 1,
                "horizontal_surface_scan_size": 297,
                "vertical_surface_scan_size": 216,
                "optical_horizontal_resolution": 600,
                "optical_vertical_resolution": 600,
                "greyscale": 1 << 8,  # 256 bit
            }
        )

    for s in scanners:
        print(s)

    save_scanners(scanners)
    print("after writing")
    scanners = read_scanners()


def save_scanners(scanners):
    with open(file="data.bin", mode="wb") as file:
        scanners_num = len(scanners)
        scanners_num = scanners_num.to_bytes(
            length=2, byteorder=byteorder, signed=False
        )
        for scanner in scanners:
            file.write(scanners_num)

            name = str(scanner["name"]).encode(encoding="utf-8", errors="strict")
            file.write(name)

            for fieldKey in scanner:
                if fieldKey == "name":
                    continue

                fieldValue = int(scanner[fieldKey]).to_bytes(
                    length=2, byteorder=byteorder, signed=False
                )
                file.write(fieldValue)


def read_scanners():
    with open(file="data.bin", mode="rb") as file:
        scanners_num_ = file.read(2)
        scanners_num = int.from_bytes(scanners_num, byteorder=byteorder, signed=False)
'''

        scanners_num = len(scanners)
        scanners_num = scanners_num.to_bytes(
            length=2, byteorder=byteorder, signed=False
        )
        for scanner in scanners:
            file.write(scanners_num)

            name = scanner["name"].to_bytes(length=2, byteorder=byteorder, signed=False)
            file.write(name)

            for fieldKey in scanner:
                if fieldKey == "name":
                    continue

                fieldValue = scanner[fieldKey].to_bytes(
                    length=2, byteorder=byteorder, signed=False
                )
                file.write(fieldValue)
                
'''


if __name__ == "__main__":
    main()
