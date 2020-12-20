import fileinput
import math

def run(inputfile):
  input = parse(inputfile)
  aligned_image = align_image(input['borders'], input['tiles'])

  print(aligned_image)

def parse(inputfile):
  tile_id = None
  strings = []
  borders = {}
  tiles = {}

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

      tiles[tile_id] = strings

  input.close()

  return {
    'borders': borders,
    'tiles': tiles
  }

def add_tile_id(borders, string, tile_id):
  temp = borders.get(string, [])
  temp.append(tile_id)
  borders[string] = temp

def align_image(borders, tiles):
  first = get_corners(borders)[0]
  oriented = orient_tile(tiles[first], is_top_left_corner(borders))
  image_row = [oriented]
  right = ''.join(x[-1] for x in oriented)
  visited = set([first])
  length = int(math.sqrt(len(tiles)))
  image = []

  for i in range(length):
    for j in range(1, length):
      next_id = list(x for x in borders[right] if x not in visited)[0]
      visited.add(next_id)
      oriented = orient_tile(tiles[next_id], is_left_aligned(right))
      right = ''.join(x[-1] for x in oriented)
      image_row.append(oriented)

    image.append(image_row)

    if i < length - 1:
      bottom = image_row[0][9]
      first = list(x for x in borders[bottom] if x not in visited)[0]
      visited.add(first)
      oriented = orient_tile(tiles[first], is_top_aligned(bottom))
      image_row = [oriented]
      right = ''.join(x[-1] for x in oriented)

  return image

def get_corners(borders):
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

  return list(corners)

def orient_tile(tile, is_aligned):
  oriented = tile
  for i in range(4):
    if is_aligned(oriented):
      return oriented
    oriented = list(map(''.join, zip(*oriented[::-1]))) # rotate

  oriented = tile[::-1]
  for i in range(4):
    if is_aligned(oriented):
      return oriented
    oriented = list(map(''.join, zip(*oriented[::-1])))

  raise
    
def is_left_aligned(border):
  def is_aligned(tile):
    left = ''.join(x[0] for x in tile)
    return left == border
  return is_aligned

def is_top_aligned(border):
  def is_aligned(tile):
    return tile[0] == border
  return is_aligned

def is_top_left_corner(borders):
  def is_aligned(tile):
    top = tile[0]
    left = ''.join(x[0] for x in tile)
    return len(borders[top]) == 1 and len(borders[left]) == 1
  return is_aligned
