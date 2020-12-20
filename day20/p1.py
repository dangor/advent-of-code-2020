import fileinput

def run(inputfile):
  borders = parse(inputfile)

  edges = {}
  corners = set()

  for border, ids in borders.items():
    if len(ids) > 1:
      continue

    id = ids[0]
    if id in edges and border != edges[id][::-1]:
      corners.add(id)
    else:
      edges[id] = border

  product = 1
  for corner in list(corners):
    product *= corner

  print(f"Answer: {product} (product of {corners})")

def parse(inputfile):
  tile_id = None
  strings = []
  borders = {}

  input = fileinput.input(files=inputfile)
  for line in input:
    stripped = line.strip('\n')

    if stripped == '':
      # reset
      strings = []
      continue

    if stripped[0] == 'T':
      tile_id = int(stripped[5:9])
      continue

    strings.append(stripped)

    if len(strings) == len(strings[0]):
      # square
      add_tile_id(borders, strings[0], tile_id)
      add_tile_id(borders, strings[0][::-1], tile_id)

      add_tile_id(borders, strings[9], tile_id)
      add_tile_id(borders, strings[9][::-1], tile_id)

      left = ''.join(x[0] for x in strings)

      add_tile_id(borders, left, tile_id)
      add_tile_id(borders, left[::-1], tile_id)

      right = ''.join(x[-1] for x in strings)

      add_tile_id(borders, right, tile_id)
      add_tile_id(borders, right[::-1], tile_id)

  input.close()

  return borders

def add_tile_id(borders, string, tile_id):
  temp = borders.get(string, [])
  temp.append(tile_id)
  borders[string] = temp
