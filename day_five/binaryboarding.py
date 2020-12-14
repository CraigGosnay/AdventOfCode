def parse_input(filepath: str) -> list:

    with open(filepath) as f:
        data = f.read().splitlines()

    return data


def decodeseatid(code: str) -> int:
    
    c = 8 
    frow = lambda x: '1' if x == 'B' else '0'
    fcol = lambda x: '1' if x == 'R' else '0'

    row = code[:7:]
    rowB = int(''.join([frow(x) for x in row]), 2)
    col = code[7::]
    colB = int(''.join([fcol(x) for x in col]), 2)
    return (rowB*c) + colB

# What is the highest seat ID on a boarding pass in the list
def part1(data: list) -> int:

    highest = 0
    for i in data: 
        highest = max(decodeseatid(i), highest)
    return highest

# Find the missing seat ID not at the missing 'ends' of the plane
def part2(data: list, highest: int) -> int:

    res = [decodeseatid(x) for x in data]
    res.sort()
    sm = res[0] # the actual starting seat    
    i = highest - 2
    i -= sm # adjust the indexing

    while i > 0:
        if res[i - 1] != res[i] - 1: 
            return res[i] - 1
        i -= 1

if __name__ == "__main__":
    d = parse_input('aoc_input.txt')
    mx = part1(d)
    print(part2(d, mx))