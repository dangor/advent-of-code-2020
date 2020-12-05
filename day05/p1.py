import fileinput

def run(inputfile):
  input = fileinput.input(files=inputfile)
  highest_id = 0

  for line in input:
    row = get_row(line[:7])
    col = get_col(line[7:])
    id = row * 8 + col
    if id > highest_id:
      highest_id = id

  print(f"Answer: {highest_id}")
  input.close()

def get_row(directions):
  rows = range(128)
  for direction in directions:
    half = len(rows) // 2 # integer divide
    if direction == 'F':
      rows = rows[:half]
    else:
      rows = rows[half:]
  return rows[0]

def get_col(directions):
  cols = range(8)
  for direction in directions:
    half = len(cols) // 2
    if direction == 'L':
      cols = cols[:half]
    else:
      cols = cols[half:]
  return cols[0]
