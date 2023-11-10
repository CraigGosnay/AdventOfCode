from dataclasses import dataclass

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

class Elf:
  calorie_list: list[int]
  
  def total_calories(self):
    return sum(self.calorie_list)

  def __init__(self):
    self.calorie_list = list()

class Solution:
  content: str

  def __init__(self, content: str):
    self.content = content
  
  def grok_content(self) -> list[Elf]:
    elves = list()
    elf = Elf()
    for line in self.content.splitlines():
      if line:
        elf.calorie_list.append(int(line))
      elif not line:
        elves.append(elf)
        elf = Elf()
    
    return elves

  def solve_p1(self):
    elves = self.grok_content()
    max_calories_elf = max(elves, key=lambda elf : elf.total_calories())
    return max_calories_elf.total_calories()

  def solve_p2(self):
    elves = self.grok_content()
    elves.sort(key=lambda elf : elf.total_calories(), reverse=True)
    top_three = elves[:3]
    return sum([elf.total_calories() for elf in top_three])

if __name__ == "__main__":
    content = parse_input('aoc_input.txt')
    solution = Solution(content)
    print(solution.solve_p1())
    print(solution.solve_p2())
    