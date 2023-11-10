from dataclasses import dataclass

WIN = 6
LOSE = 0
DRAW = 3

RESULT_MAP = {
  'lose': LOSE,
  'draw': DRAW,
  'win': WIN
}

ROCK = 'r'
PAPER = 'p'
SCIS = 's'

SHAPE_VAL = {
  ROCK : 1,
  PAPER : 2,
  SCIS : 3
}

MOVE_MAP_P1 = {
  'X': ROCK,
  'Y': PAPER,
  'Z': SCIS,
  'A': ROCK,
  'B': PAPER,
  'C': SCIS
}

MOVE_MAP_P2 = {
  'X': 'lose',
  'Y': 'draw',
  'Z': 'win',
  'A': ROCK,
  'B': PAPER,
  'C': SCIS
}

BEATS = {
  ROCK: SCIS,
  PAPER: ROCK,
  SCIS: PAPER
}

LOSES = {
  SCIS: ROCK,
  ROCK: PAPER,
  PAPER: SCIS
}


def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content

class Solution:
  
  def solve_p1(self, input: str) -> int:
    score = 0
    for move in input.splitlines():
      oppo, mine = move[0], move[2]
      score += SHAPE_VAL[MOVE_MAP_P1[mine]]
      score += self.calc_result(oppo, mine)
    
    return score
  
  def solve_p2(self, input: str) -> int:
    score = 0
    for move in input.splitlines():
      oppo, target = move[0], move[2]
      score += RESULT_MAP[MOVE_MAP_P2[target]]
      score += SHAPE_VAL[self.move_to_play(oppo, target)]
    return score

  def move_to_play(self, oppo: str, target: str) -> str:
    if MOVE_MAP_P2[target] == 'lose':
      return BEATS[MOVE_MAP_P2[oppo]]
    elif MOVE_MAP_P2[target] == 'win':
      return LOSES[MOVE_MAP_P2[oppo]]
    else:
      return MOVE_MAP_P2[oppo]

  def calc_result(self, oppo_move: str, my_move: str) -> int:
    oppo_shape = MOVE_MAP_P1[oppo_move]
    my_shape = MOVE_MAP_P1[my_move]

    if oppo_shape == my_shape:
      return DRAW
    
    if my_shape in BEATS[oppo_shape]:
      return LOSE
    
    return WIN

if __name__ == "__main__":
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    
    test_input = "A Y\nB X\nC Z"
    assert solution.solve_p1(test_input) == 15
    assert solution.solve_p2(test_input) == 12

    print(solution.solve_p2(content))