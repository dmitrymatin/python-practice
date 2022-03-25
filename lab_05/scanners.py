from sys import byteorder


def main():
    num_scanners = 6
    scanners = []
    for i in range(num_scanners):
        scanners.append(
            {
                "name": f"scanner{i * 10}",
                "price": (i ^ 1) << 1,  # позволяет задать неотсортированную последовательность чисел
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
    sorted_scanners = sort_scanners()

    for s in sorted_scanners:
        print(s)


def sort_scanners():
    scanners = read_scanners()
    scanners.sort(key=lambda scanner: scanner["price"])
    return scanners


def save_scanners(scanners):
    numeric_field_length = 2

    with open(file="data.bin", mode="wb") as file:
        scanners_num = len(scanners)
        scanners_num = scanners_num.to_bytes(
            length=numeric_field_length, byteorder=byteorder, signed=False
        )
        file.write(scanners_num)

        for scanner in scanners:
            name = str(scanner["name"]).encode(encoding="utf-8", errors="strict")
            name_length = len(name)
            name_length = name_length.to_bytes(
                length=numeric_field_length, byteorder=byteorder, signed=False
            )

            file.write(name_length)
            file.write(name)

            for field_key in scanner:
                if field_key == "name":
                    continue

                field_value = int(scanner[field_key]).to_bytes(
                    length=numeric_field_length, byteorder=byteorder, signed=False
                )
                file.write(field_value)


def read_scanners():
    scanner_equal_length_fields = (
        "price",
        "horizontal_surface_scan_size",
        "vertical_surface_scan_size",
        "optical_horizontal_resolution",
        "optical_vertical_resolution",
        "greyscale",
    )

    numeric_field_length = 2
    scanners = []

    with open(file="data.bin", mode="rb") as file:
        scanners_num = file.read(numeric_field_length)
        scanners_num = int.from_bytes(scanners_num, byteorder=byteorder, signed=False)

        for _ in range(scanners_num):
            name_length = file.read(numeric_field_length)
            name_length = int.from_bytes(name_length, byteorder=byteorder, signed=False)

            name = file.read(name_length)
            name = name.decode(encoding="utf-8", errors="strict")

            scanner_dict = {"name": name}
            for field_key in scanner_equal_length_fields:
                field_value = file.read(numeric_field_length)
                field_value = int.from_bytes(
                    field_value, byteorder=byteorder, signed=False
                )

                scanner_dict[field_key] = field_value

            scanners.append(scanner_dict)

    return scanners


if __name__ == "__main__":
    main()
