import fileinput

def run(inputfile):
  decks = parse(inputfile)
  
  while len(decks[1]) > 0 and len(decks[2]) > 0:
    card_1 = decks[1].pop(0)
    card_2 = decks[2].pop(0)
    if card_1 > card_2:
      decks[1].extend([card_1, card_2])
    else:
      decks[2].extend([card_2, card_1])

  deck = decks[1]
  if len(decks[2]) > 0:
    deck = decks[2]

  answer = 0
  for i in range(1, len(deck) + 1):
    card = deck.pop()
    answer += i * card

  print(f"Answer: {answer}")

def parse(inputfile):
  decks = {
    1: [],
    2: []
  }
  input = fileinput.input(files=inputfile)
  player_1 = True
  for line in input:
    if line == '\n':
      player_1 = False
    elif line.find('Player') == 0:
      continue
    elif player_1:
      decks[1].append(int(line))
    else:
      decks[2].append(int(line))
  input.close()
  return decks