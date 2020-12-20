import fileinput
import math

def run(inputfile, monsterfile):
  input = parse(inputfile)
  monster = parse_monster(monsterfile)

  aligned_image = align_image(input['borders'], input['tiles'])
  
  actual_image = extract_actual_image(aligned_image)

  monster_coords = get_monster_coords(actual_image, monster)

  sum = 0
  for row, line in enumerate(actual_image):
    for col, char in enumerate(line):
      if char == '#' and (row, col) not in monster_coords:
        sum += 1
  
  print(f"Answer: {sum}")

# parse set of offsets from 0,0 (row, col), starting from
# top left
def parse_monster(monsterfile):
  monster = []
  input = fileinput.input(files=monsterfile)
  for row, line in enumerate(input):
    stripped = line.strip('\n')
    for col, char in enumerate(stripped):
      if char == '#':
        monster.append((row, col))

  input.close()
  return monster

# parse borderpattern->tile_id dict of lists of ints
# and tile_id->tile dict of lists of strings
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

# add tile_id to borders dict
def add_tile_id(borders, string, tile_id):
  temp = borders.get(string, [])
  temp.append(tile_id)
  borders[string] = temp

# align tiles into an image as defined by aoc
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

# tile ids of corner tiles of image
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

# rotate/flip the tile to the orientation where the
# passed in is_aligned(tile) func returns true
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

# generate an is_aligned check based on having
# a left border that matches the input border
def is_left_aligned(border):
  def is_aligned(tile):
    left = ''.join(x[0] for x in tile)
    return left == border
  return is_aligned

# generate an is_aligned check based on having
# a top border that matches the input border
def is_top_aligned(border):
  def is_aligned(tile):
    return tile[0] == border
  return is_aligned

# generate an is_aligned check based on the tile
# being in an orientation with no neighbors above
# or to the left, i.e. is a top-left corner tile
def is_top_left_corner(borders):
  def is_aligned(tile):
    top = tile[0]
    left = ''.join(x[0] for x in tile)
    return len(borders[top]) == 1 and len(borders[left]) == 1
  return is_aligned

# produce one list of strings to represent the
# "actual" image without borders and gaps
def extract_actual_image(image):
  actual_image = []
  for tile_row in image:
    strings = ['']*8
    for tile in tile_row:
      for i, string in enumerate(tile):
        if i == 0 or i == 9:
          continue
        strings[i-1] += string[1:-1]
    actual_image.extend(strings)
  return actual_image

# get a set of coords that matched a monster
def get_monster_coords(image, monster):
  coords = set()
  orientations = monster_orientations(monster)
  
  for row in range(len(image)):
    for col in range(len(image[0])):
      for offsets in orientations:
        valid = set()
        for offset in offsets:
          offset_row = row + offset[0]
          offset_col = col + offset[1]
          if not (0 <= offset_row < len(image)):
            break
          if not (0 <= offset_col < len(image[0])):
            break
          if image[offset_row][offset_col] != '#':
            break
          valid.add((offset_row, offset_col))
        if len(valid) == len(offsets):
          coords.update(valid)

  return coords

# get a list of monster offsets, for all 8 orientations
def monster_orientations(monster):
  orientations = []
  orientation = monster
  for i in range(4):
    orientation = rotate_offsets(orientation)
    orientations.append(orientation)

  # flip, then rotate again
  orientation = list((-x[0], x[1]) for x in monster)
  for i in range(4):
    orientation = rotate_offsets(orientation)
    orientations.append(orientation)

  return orientations

def rotate_offsets(offsets):
  return list((x[1], -x[0]) for x in offsets)