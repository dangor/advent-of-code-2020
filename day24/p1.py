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

  print(f"Answer: {len(black)}")