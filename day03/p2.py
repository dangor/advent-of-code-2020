import fileinput

def run(inputfile):
  input = fileinput.input(files=inputfile)
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  columns = [0] * len(slopes) # i.e. [0, 0, 0, 0, 0]
  tree_counts = [0] * len(slopes)

  # one pass, baby
  for line in input:
    line_index = input.lineno()
    size = (len(line) - 1) # account for \n
    for i in range(len(slopes)):
      if (line_index - 1) % slopes[i][1] != 0:
        # skip line, i.e for (1, 2) slope
        continue
      if line[columns[i]] == '#':
        tree_counts[i] += 1
      columns[i] = (columns[i] + slopes[i][0]) % size

  tree_product = 1
  for tree_count in tree_counts:
    tree_product *= tree_count

  print(f"Answer: {tree_product}")
  input.close()