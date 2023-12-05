

def parse_input(filepath: str) -> str:

  with open(filepath) as f:
    content = f.read()
  
  return content



class Hand:
  id: int
  reds: int
  blues: int
  greens: int
  
  def __init__(self, id: int) -> None:
    self.id = id

class Game:
   id: int
   hands: list[Hand]

   def __init__(self, id: int) -> None:
      self.id = id

class Solution:
  
  def solve_p1(self, input: str, max_red: int, max_green: int, max_blue: int) -> int:
    games = self.preprocess_input(input)
    id_sum = 0
    for game in games:
      if any([hand.reds > max_red for hand in game.hands]) \
        or any([hand.greens > max_green for hand in game.hands]) \
        or any([hand.blues > max_blue for hand in game.hands]):
        continue  
      id_sum += game.id
    return id_sum
  
  def solve_p2(self, input: str) -> int:
    games = self.preprocess_input(input)
    powers = []
    for game in games:
      min_red = max([hand.reds for hand in game.hands])
      min_blue = max([hand.blues for hand in game.hands])
      min_green = max([hand.greens for hand in game.hands])
      powers.append(min_red * min_blue * min_green)
    return sum(powers)

  def preprocess_input(self, input: str) -> list[Game]:
    games = []
    for line in input.splitlines():
       ptr = 5
       while line[ptr] != ':':
          ptr += 1
       id_str = line[5:ptr]
       game = Game(int(id_str))
       hands_str = line[ptr+1:].strip()
       game.hands = self.parse_hands(hands_str)
       games.append(game)
    return games

  def parse_hands(self, hands_str: str) -> list[Hand]:
    hands = []
    hands_list = hands_str.split(';')
    for i,hand_str in enumerate(hands_list):
        hand = self.parse_hand(i, hand_str)
        hands.append(hand)
    return hands

  def parse_hand(self, hand_id: int, hand_str: str) -> Hand:
    hand = Hand(hand_id)
    hand.blues = self.get_color_count(hand_str, 'blue')
    hand.greens = self.get_color_count(hand_str, 'green')
    hand.reds = self.get_color_count(hand_str, 'red')
    return hand
  
  def get_color_count(self, hand_str: str, color: str) -> int:
    idx = hand_str.find(color)

    if idx == -1:
      return 0

    idx = idx - 2
    count_str = ''
    while hand_str[idx].isdigit():
      count_str += hand_str[idx]
      idx -= 1
    return int(count_str[::-1])
  
if __name__ == "__main__":
    example = parse_input('./aoc_input_ex.txt')
    content = parse_input('./aoc_input.txt')
    solution = Solution()
    assert solution.solve_p1(example, 12, 13, 14) == 8
    print('question 1: ', solution.solve_p1(content, 12, 13, 14))
    assert solution.solve_p2(example) == 2286
    print('question 2: ', solution.solve_p2(content))
