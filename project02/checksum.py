import collections

if __name__ == "__main__":
    with open("input.txt") as fh:
        data = map(lambda item: item.strip(), fh.read().split("\n"))

    counts = list(map(collections.Counter, data))
    twos, threes = 0, 0
    for code in counts:
        twos += int(2 in code.values())
        threes += int(3 in code.values())
    print(twos * threes)
