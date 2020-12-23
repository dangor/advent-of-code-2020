import fileinput

def run(inputfile):
  decks = parse(inputfile)
  
  decks = play_game(decks)

  deck = decks[1]
  if len(decks[2]) > 0 and len(decks[1]) == 0:
    deck = decks[2]

  answer = 0
  for i in range(1, len(deck) + 1):
    card = deck.pop()
    answer += i * card

  print(f"Answer: {answer}")

def play_game(decks):
  past_games = set()
  while len(decks[1]) > 0 and len(decks[2]) > 0:
    # infinite loop protection
    game_hash = hash_game(decks)
    if game_hash in past_games:
      return decks
    else:
      past_games.add(game_hash)

    # draw
    card_1 = decks[1].pop(0)
    card_2 = decks[2].pop(0)

    winner = 1 # default

    if len(decks[1]) >= card_1 and len(decks[2]) >= card_2:
      # recurse
      new_decks = {
        1: decks[1][:card_1],
        2: decks[2][:card_2]
      }

      new_decks = play_game(new_decks)

      if len(new_decks[2]) > 0 and len(new_decks[1]) == 0:
        winner = 2
    elif card_1 < card_2:
      winner = 2

    if winner == 1:
      decks[1].extend([card_1, card_2])
    else:
      decks[2].extend([card_2, card_1])

  return decks

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

def hash_game(decks):
  string_1 = ','.join(map(str, decks[1]))    
  string_2 = ','.join(map(str, decks[2]))
  return hash(string_1 + '|' + string_2)
