import copy

def run(inputfile):
  file = open(inputfile)
  seats = list(list(x.strip('\n')) for x in file.readlines())
  file.close()

  new_seats = next_gen(seats)
  while seats != new_seats:
    seats = new_seats
    new_seats = next_gen(seats)
  
  print(f"Answer: {total_occupied(seats)}")

def total_occupied(seats):
  count = 0
  for row in seats:
    for seat in row:
      if seat == '#':
        count += 1
  return count

def next_gen(seats):
  new = copy.deepcopy(seats)
  for i in range(len(seats)):
    for j in range(len(seats[i])):
      if seats[i][j] == 'L' and num_adj_occupied(i, j, seats) == 0:
        new[i][j] = '#'
      elif seats[i][j] == '#' and num_adj_occupied(i, j, seats) >= 5:
        new[i][j] = 'L'
  return new

def num_adj_occupied(i, j, seats):
  directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
  ]
  num = 0

  for direction in directions:
    x, y = i, j
    while True:
      x = x + direction[0]
      y = y + direction[1]
      if not in_bounds(x, y, seats):
        break
      elif seats[x][y] == '#':
        num += 1
        break
      elif seats[x][y] == 'L':
        break
  return num

def in_bounds(i, j, seats):
  return 0 <= i < len(seats) and 0 <= j < len(seats[i])
