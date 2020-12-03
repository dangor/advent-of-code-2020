import fileinput

def run(inputfile):
  tree_count = 0
  current_column = 0
  input = fileinput.input(files=inputfile)
  for line in input:
    if line[current_column] == '#':
      tree_count += 1
    size = (len(line) - 1) # account for \n
    current_column = (current_column + 3) % size
  print(f"Answer: {tree_count}")
  input.close()