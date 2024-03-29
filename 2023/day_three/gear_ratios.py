from collections import defaultdict
from dataclasses import dataclass


def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

@dataclass
class GridNum:
  row: int
  col_start: int
  col_end: int
  val: int

@dataclass
class Gear:
  row: int
  col: int
  ratio: int

class Solution:
  
  def solve_p1(self, input: str) -> int:
    rows = input.splitlines()
    line_len = len(rows[0])

    included = []

    curr_row = 0
    while curr_row < len(rows):
      curr_col = 0
      curr_num = []
      has_symbol = False

      while curr_col < line_len:
        if rows[curr_row][curr_col].isdigit():
          curr_num.append(rows[curr_row][curr_col])
          #check surrounding cells
          for dir in DIRS:
            if 0 <= curr_row + dir[0] < len(rows) and 0 <= curr_col + dir[1] < line_len:
              if rows[curr_row + dir[0]][curr_col + dir[1]] != '.' and not rows[curr_row + dir[0]][curr_col + dir[1]].isdigit():
                has_symbol = True
        if not rows[curr_row][curr_col].isdigit() or curr_col == line_len - 1 and len(curr_num) > 0:
          if has_symbol:
            included.append(int(''.join(curr_num)))
          curr_num = []
          has_symbol = False
        curr_col += 1
      curr_row += 1

    return sum(included)
    
  def solve_p2(self, input: str) -> int:
    rows = input.splitlines()
    line_len = len(rows[0])
    nums = []
    gears = []
    ratios = []

    curr_row = 0
    while curr_row < len(rows):
      curr_col = 0
      curr_num = []

      while curr_col < line_len:
        if rows[curr_row][curr_col].isdigit():
          curr_num.append(rows[curr_row][curr_col])
        if (not rows[curr_row][curr_col].isdigit() or curr_col == line_len - 1) and len(curr_num) > 0:
            nums.append(GridNum(curr_row, curr_col-len(curr_num), curr_col-1, int(''.join(curr_num))))
            curr_num = []
        if rows[curr_row][curr_col] == '*':
          gears.append(Gear(curr_row, curr_col, 0))
        curr_col += 1
      curr_row += 1

    gmap = defaultdict(GridNum)
    for num in nums:
      for i in range(num.col_start, num.col_end + 1):
        gmap[(num.row, i)] = num
    
    for gear in gears:
      gearnums = []
      for dir in DIRS:
        if (gear.row + dir[0], gear.col + dir[1]) in gmap:
          if gmap[(gear.row + dir[0], gear.col + dir[1])] not in gearnums:
            gearnums.append(gmap[(gear.row + dir[0], gear.col + dir[1])])
      if len(gearnums) == 2:
        gear.ratio = gearnums[0].val * gearnums[1].val
        ratios.append(gear.ratio)

    return sum(ratios)

if __name__ == "__main__":
    example = parse_input('./aoc_input_ex.txt')
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    assert solution.solve_p1(example) == 4361
    print('question 1: ', solution.solve_p1(content))
    assert solution.solve_p1(content) == 521515

    print('question 2: ', solution.solve_p2(content))
    assert solution.solve_p2(example) == 467835
    assert solution.solve_p2(content) == 69527306
    
