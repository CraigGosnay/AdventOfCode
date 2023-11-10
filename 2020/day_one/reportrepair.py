def parse_input(filepath: str) -> list:

    with open(filepath) as f:
        expenses = f.read().splitlines()

    return [int(i) for i in expenses]

def find_sum_p1(expenses: list) -> int:

    s = set()
    for i in expenses:
        if i > 2020:
            continue
        j = 2020 - i
        if j in s:
            return i*j
        s.add(i)
    return 0

def find_sum_p2(expenses: list) -> int:

    target = 2020
    expenses.sort() # O(n log n)

    # O(n^2)
    for i in range(len(expenses)):
        curr = expenses[i]
        lo = i + 1
        hi = len(expenses) - 1

        while lo < hi and expenses[lo] < target:
            if curr + expenses[lo] + expenses[hi] == target:
                return curr*expenses[lo]*expenses[hi]
            elif expenses[lo] + expenses[hi] + curr> target:
                hi -= 1
            elif expenses[lo] + expenses[hi] + curr < target:
                lo += 1
    
if __name__ == "__main__":
    exps = parse_input('aoc_input.txt')
    print(find_sum_p1(exps))
    print(find_sum_p2(exps))
