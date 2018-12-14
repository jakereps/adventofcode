import collections
import re


def main():
    with open("input.txt") as fh:
        data = fh.read()

    fabric = collections.defaultdict(list)
    sizes = {}
    pattern = re.compile(r"#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)")
    for (_id, xpos, ypos, w, h) in map(lambda i: map(int, i), pattern.findall(data)):
        sizes[_id] = w * h
        for y in range(ypos, ypos + h):
            for x in range(xpos, xpos + w):
                if not fabric[(x, y)]:
                    fabric[(x, y)] = [0, []]
                fabric[(x, y)][0] += 1
                fabric[(x, y)][1].append(_id)
    print(f"Overlapping claims: {len(list(filter(lambda claim: claim[1][0] >= 2, fabric.items())))}")
    gross = list(map(lambda claim: claim[1][1][0], list(filter(lambda claim: claim[1][0] == 1 and len(claim[1][1]) == 1, fabric.items()))))
    still_gross = collections.Counter(gross)
    print(f"(ID, size) of last sheet standing: {list(filter(lambda item: sizes[item[0]] == item[1], still_gross.items()))}")



if __name__ == "__main__":
    main()
