def run(inputfile):
  file = open(inputfile)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  compass = ['N', 'E', 'S', 'W']

  facing = 'E'
  x, y = 0, 0

  for direction in directions:
    letter = direction[0]
    value = int(direction[1:])
    if letter == 'S' or (letter == 'F' and facing == 'S'):
      y -= value
    elif letter == 'N' or (letter == 'F' and facing == 'N'):
      y += value
    elif letter == 'E' or (letter == 'F' and facing == 'E'):
      x += value
    elif letter == 'W' or (letter == 'F' and facing == 'W'):
      x -= value
    elif letter == 'L':
      diff = value // 90
      new_index = compass.index(facing) - diff
      facing = compass[new_index]
    elif letter == 'R':
      diff = value // 90
      new_index = (compass.index(facing) + diff) % 4
      facing = compass[new_index]

  answer = abs(x) + abs(y)
  print(f"Answer: {answer}")