def run(cups):
  current = cups[0]

  for move in range(100):
    i = cups.index(current)

    removed = cups[i+1:i+4]
    cups = cups[:i+1] + cups[i+4:]
    if len(removed) < 3:
      diff = 3 - len(removed)
      removed += cups[:diff]
      cups = cups[diff:]

    marker = None
    for j in range(int(current) - 1, 0, -1):
      if str(j) in cups:
        marker = str(j)
        break

    if marker == None:
      marker = str(max(map(int, cups)))

    split = cups.split(marker)
    cups = split[0] + marker + removed + split[1]

    i = cups.index(current) # may have changed
    current = cups[(i + 1) % len(cups)]

  i = cups.index('1')
  answer = cups[i + 1:] + cups[:i]

  print(f"Answer: {answer}")