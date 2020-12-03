def parse_input(filepath: str) -> list:

    with open(filepath) as f:
        expenses = f.read().splitlines()

    return [int(i) for i in expenses]

def find_sum(expenses: list) -> int:

    s = set()
    for i in expenses:
        if i > 2020:
            continue
        j = 2020 - i
        if j in s:
            return i*j
        s.add(i)
    return 0
    
if __name__ == "__main__":
    print(find_sum(parse_input('aoc_input.txt')))
