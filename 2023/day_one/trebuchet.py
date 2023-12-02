

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

WORD_TO_NUM = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

WORDS = set(WORD_TO_NUM.keys())
REVERSED_WORDS = set([word[::-1] for word in WORDS])

def is_word(s: str) -> bool:
  return s in WORD_TO_NUM

def is_reversed_word(s: str) -> bool:
  return s in REVERSED_WORDS

class Solution:
  
  # 95btwo
  def solve_p1(self, input: str) -> int:
    total = 0
    for line in input.splitlines():
      left = 0
      right = len(line) - 1
      left_val = None
      right_val = None

      while left <= right and (left_val is None or right_val is None):
        if line[left].isdigit() and left_val is None:
          left_val = line[left]

        if line[right].isdigit() and right_val is None:
          right_val = line[right]

        # not digits so need to check words
        if left_val is None:
          word = ''
          new_left = left
          while new_left <= right and new_left <= left + 4 and line[new_left].isalpha():
            word += line[new_left]
            new_left += 1
            if is_word(word):
              left_val = WORD_TO_NUM[word]
              break

        if right_val is None:
          word = ''
          new_right = right
          while new_right >= left and new_right >= right - 4 and line[new_right].isalpha():
            word += line[new_right]
            new_right -= 1
            if is_word(word[::-1]):
              right_val = WORD_TO_NUM[word[::-1]]
              break

        if left_val is None:
          left += 1

        if right_val is None:
          right -= 1

      if left_val is None or right_val is None:
        concat = left_val + left_val if right_val is None else right_val + right_val
      else:
        concat = left_val + right_val

      print(int(concat))
      total += int(concat)
      
    return total

if __name__ == "__main__":
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    print(solution.solve_p1(content))