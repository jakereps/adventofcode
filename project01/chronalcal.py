if __name__ == "__main__":
    with open("input.txt", "rt") as fh:
        data = filter(
            lambda line: line != "", map(lambda line: line.strip(), fh.readlines())
        )
    print(sum(map(int, data)))
