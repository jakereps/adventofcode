import itertools
import sys

if __name__ == "__main__":
    with open("input.txt") as fh:
        data = map(lambda item: item.strip(), fh.read().split("\n"))

    combs = itertools.combinations(data, 2)
    for (x, y) in combs:
        if sum([bool(ord(i) ^ ord(j)) for i, j in zip(x, y)]) == 1:
            # sets are unordered and advent order mattered, had to print and compare and remove the differing column
            print(f"{x}\n{y}")
            sys.exit(0)
