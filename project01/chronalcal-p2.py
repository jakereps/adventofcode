import sys

if __name__ == "__main__":
    with open("inputs.txt", "rt") as fh:
        data = list(
            filter(
                lambda line: line != "", map(lambda line: line.strip(), fh.readlines())
            )
        )

    freqs = set()
    frequency = 0
    loop = 1
    while True:
        print(f"loop: {loop}")
        for change in data:
            frequency += int(change)
            if freqs.intersection((frequency,)):
                print(f"found on loop {loop}: {frequency}")
                sys.exit(0)
            freqs.add(frequency)
        loop += 1
