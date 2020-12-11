def parse_input(filepath: str) -> list:

    with open(filepath) as f:
        data = f.read().splitlines()

    return data


def treeimpacts(data: list, right: int, down: int) -> int:

    row = 0
    col = 0

    repeat = len(data[0])
    limit = len(data)
    trees = 0

    while row < limit:
        
        if data[row][col] == '#':
            trees += 1
        col = (col + right) % repeat
        row += down
    return trees


if __name__ == "__main__":
    data = parse_input('aoc_input.txt')
    print(treeimpacts(data, 1, 1))
    print(treeimpacts(data, 3, 1))
    print(treeimpacts(data, 5, 1))
    print(treeimpacts(data, 7, 1))
    print(treeimpacts(data, 1, 2))
