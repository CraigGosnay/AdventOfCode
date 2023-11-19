from collections import Counter

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

class Solution:

  def calculate_prio_value(self, c: str) -> int:
    if c.islower():
      return ord(c) - 96
    else:
      return ord(c) - 38

  def solve_p1(self, input: str) -> int:
    total = 0
    for backpack in input.splitlines():
      if len(backpack.strip()) == 0:
          continue
      midpoint = int(len(backpack) / 2)
      left_set = set(backpack[:midpoint])
      overlap = set[str]()
      for i in range(midpoint, len(backpack)):
        if backpack[i] in left_set:
          overlap.add(backpack[i])

      for c in overlap:
        total += self.calculate_prio_value(c)
    return total
  
  def solve_p2(self, input: str) -> int:
    total = 0
    backpacks = input.splitlines()
    backpacks = list(filter(lambda x: len(x.strip()) > 0, backpacks))
    while len(backpacks) > 2:
      a,b,c = backpacks.pop(0), backpacks.pop(0), backpacks.pop(0)
      overlap = set(a).intersection(set(b)).intersection(set(c))
      for c in overlap:
        total += self.calculate_prio_value(c)
    return total


if __name__ == "__main__":
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    
    test = """vJrwpWtwJgWrhcsFMMfFFhFp
    \njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    \nPmmdzqPrVvPwwTWBwg
    \nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    \nttgJtRGJQctTZtZT
    \nCrZsJsPPZsGzwwsLwLmpwMDw"""

    assert solution.solve_p1(test) == 157
    print(solution.solve_p1(content))

    assert solution.solve_p2(test) == 70
    print(solution.solve_p2(content))