from collections import Counter

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

class Solution:
  
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
        if c.islower():
          total += ord(c) - 96
        else:
          total += ord(c) - 38
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