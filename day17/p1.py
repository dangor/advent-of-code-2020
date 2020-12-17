def run(inputfile):
  file = open(inputfile)
  initial = list(x.strip('\n') for x in file.readlines())
  file.close()

  xlen = len(initial)
  ylen = len(initial[0])

  cube = initialize(initial)

  for n in range(1, 7):
    cube = cycle(cube, n, xlen, ylen)

  count = count_all_active(cube)
  print(f"Answer: {count}")

def initialize(initial):
  cube = {}
  for x, line in enumerate(initial):
    for y, char in enumerate(line):
      if char == '#':
        activate(cube, x, y, 0)
  return cube

def cycle(cube, n, xlen, ylen):
  new_cubes = {}
  for x in range(0 - n, xlen + n):
    for y in range(0 - n, ylen + n):
      for z in range(0 - n, 1 + n):
        active_neighbors = count_active_neighbors(cube, x, y, z)
        if is_active(cube, x, y, z) and 2 <= active_neighbors <= 3:
          activate(new_cubes, x, y, z)
        elif not is_active(cube, x, y, z) and active_neighbors == 3:
          activate(new_cubes, x, y, z)
  return new_cubes
          
def activate(cube, x, y, z):
  plane = cube.get(x, {})
  line = plane.get(y, {})
  line[z] = True
  plane[y] = line
  cube[x] = plane
        
def is_active(cube, x, y, z):
  return x in cube and y in cube[x] and z in cube[x][y]

def count_active_neighbors(cube, x, y, z):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1, 2):
        if i == 0 and j == 0 and k == 0:
          continue

        if is_active(cube, x + i, y + j, z + k):
          count += 1

  return count

def count_all_active(cube):
  count = 0
  for plane in cube.values():
    for line in plane.values():
      count += len(line)
  return count