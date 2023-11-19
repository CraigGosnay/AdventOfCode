from collections import Counter
from dataclasses import dataclass

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

@dataclass
class Range:
  lower: int
  upper: int

@dataclass
class RangePair:
  first: Range
  second: Range

class Solution:

  def parse_input_to_range_pairs(self, input: str) -> list[RangePair]:
    raw_pairs = [x.strip() for x in input.splitlines()]
    pairs = map(lambda x: tuple(x.split(',')), raw_pairs)
    ranges = [RangePair(Range(*map(int, x[0].split('-'))), Range(*map(int, x[1].split('-')))) for x in pairs]
    return ranges

  def check_complete_overlap(self, rangePair: RangePair) -> bool:
    return (rangePair.second.upper <= rangePair.first.upper and \
        rangePair.second.lower >= rangePair.first.lower) or \
          (rangePair.first.upper <= rangePair.second.upper and \
        rangePair.first.lower >= rangePair.second.lower)

  def check_partial_overlap(self, rangePair: RangePair) -> bool:
    return (rangePair.first.lower < rangePair.second.lower and \
      rangePair.first.upper >= rangePair.second.lower and \
      rangePair.first.upper < rangePair.second.upper) or \
      (rangePair.second.lower < rangePair.first.lower and \
      rangePair.second.upper >= rangePair.first.lower and \
      rangePair.second.upper < rangePair.first.upper)


  def solve_p1(self, input: str) -> int:
    ranges = self.parse_input_to_range_pairs(input)
    overlappingCount = 0
    for rangePair in ranges:
      if self.check_complete_overlap(rangePair):
        overlappingCount += 1

    return overlappingCount

  def solve_p2(self, input: str) -> int:
    ranges = self.parse_input_to_range_pairs(input)
    overlappingCount = 0
    for rangePair in ranges:
      if self.check_complete_overlap(rangePair) or self.check_partial_overlap(rangePair):
        overlappingCount += 1
    return overlappingCount

if __name__ == "__main__":
    content = parse_input('./aoc_input.txt')
    solution = Solution()

    test = \
      """2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8"""
   
    assert solution.solve_p1(test) == 2
    print(solution.solve_p1(content))

    assert solution.solve_p2(test) == 4
    print(solution.solve_p2(content))
    