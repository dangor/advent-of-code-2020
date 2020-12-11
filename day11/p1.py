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
      elif seats[i][j] == '#' and num_adj_occupied(i, j, seats) >= 4:
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
    if is_occupied(i + direction[0], j + direction[1], seats):
      num += 1
  return num

def is_occupied(i, j, seats):
  if i not in range(len(seats)):
    return False
  if j not in range(len(seats[i])):
    return False
  
  return seats[i][j] == '#'