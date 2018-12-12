import collections
import re


def main():
    with open("input.txt") as fh:
        data = fh.read()

    fabric = collections.defaultdict(int)
    pattern = re.compile(r"#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)")
    for (xpos, ypos, w, h) in map(lambda i: map(int, i), pattern.findall(data)):
        for y in range(ypos, ypos + h):
            for x in range(xpos, xpos + w):
                fabric[(x, y)] += 1
    print(len(list(filter(lambda claim: claim[1] >= 2, fabric.items()))))


if __name__ == "__main__":
    main()
