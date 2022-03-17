def main():
    num_scanners = 4
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


if __name__ == "__main__":
    main()
