import fileinput

def run(inputfile):
  total_sum = 0
  current_set = set()

  input = fileinput.input(files=inputfile)
  for line in input:
    if line == '\n':
      total_sum += len(current_set)
      current_set.clear()
      continue

    for question in line:
      if question != '\n':
        current_set.add(question)

  # last one
  total_sum += len(current_set)

  print(f"Answer: {total_sum}")

  input.close()
