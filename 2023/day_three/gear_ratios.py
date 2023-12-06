def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

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

if __name__ == "__main__":
    example = parse_input('./aoc_input_ex.txt')
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    assert solution.solve_p1(example) == 4361
    print('question 1: ', solution.solve_p1(content))
    assert solution.solve_p1(content) == 521515
