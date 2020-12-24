import fileinput

# treat hexes as cartesian coords, with the
# y-axis on a slant, e.g.
# 0 1 2...
#  0 1 2...
#   0 1 2...
# e & w are straightforward
# ne is up 1 over 1
# nw is up 1
# se is down 1
# sw is down 1 over -1
def run(inputfile):
  black = parse(inputfile)

  for day in range(100):
    black = next_gen(black)

  print(f"Answer: {len(black)}")

def parse(inputfile):
  black = set()

  input = fileinput.input(files=inputfile)
  for line in input:
    cur = (0, 0)
    ns = None
    for char in line.strip('\n'):
      if char == 'n':
        ns = 'n'
        continue
      elif char == 's':
        ns = 's'
        continue
      elif ns == 'n' and char == 'e':
        cur = (cur[0] + 1, cur[1] + 1)
      elif ns == 'n' and char == 'w':
        cur = (cur[0], cur[1] + 1)
      elif ns == 's' and char == 'e':
        cur = (cur[0], cur[1] - 1)
      elif ns == 's' and char == 'w':
        cur = (cur[0] - 1, cur[1] - 1)
      elif char == 'e':
        cur = (cur[0] + 1, cur[1])
      elif char == 'w':
        cur = (cur[0] - 1, cur[1])
      else:
        raise

      ns = None

    if cur in black:
      black.remove(cur)
    else:
      black.add(cur)
        
  input.close()
  return black

def next_gen(black):
  new_black = set()
  visited = set()
  for tile in black:
    area = get_neighbors(tile)
    area.append(tile)
    for t in area:
      if t not in visited:
        visit_tile(t, black, new_black)
        visited.add(t)
  return new_black

def get_neighbors(tile):
  return [
    (tile[0], tile[1] + 1),
    (tile[0] + 1, tile[1] + 1),
    (tile[0] + 1, tile[1]),
    (tile[0], tile[1] - 1),
    (tile[0] - 1, tile[1] - 1),
    (tile[0] - 1, tile[1])
  ]

def visit_tile(tile, black, new_black):
  neighbors = get_neighbors(tile)
  num_black = 0
  for neighbor in neighbors:
    if neighbor in black:
      num_black += 1

  if tile in black and (1 <= num_black <= 2):
    new_black.add(tile)
  elif tile not in black and num_black == 2:
    new_black.add(tile)