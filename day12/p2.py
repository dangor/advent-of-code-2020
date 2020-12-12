def run(inputfile):
  file = open(inputfile)
  directions = list(x.strip('\n') for x in file.readlines())
  file.close()

  waypoint = [10, 1]
  ship = [0, 0]

  for direction in directions:
    letter = direction[0]
    value = int(direction[1:])

    if letter == 'S':
      waypoint[1] -= value
    elif letter == 'N':
      waypoint[1] += value
    elif letter == 'E':
      waypoint[0] += value
    elif letter == 'W':
      waypoint[0] -= value
    elif letter == 'F':
      ship[0] += value * waypoint[0]
      ship[1] += value * waypoint[1]
    # either L or R
    elif value == 180:
      waypoint[0] = -waypoint[0]
      waypoint[1] = -waypoint[1]
    elif (letter == 'L' and value == 90) or (letter == 'R' and value == 270):
      x = waypoint[0]
      waypoint[0] = -waypoint[1]
      waypoint[1] = x
    else:
      x = waypoint[0]
      waypoint[0] = waypoint[1]
      waypoint[1] = -x

  answer = abs(ship[0]) + abs(ship[1])
  print(f"Answer: {answer}")