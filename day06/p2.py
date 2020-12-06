import fileinput

def run(inputfile):
  total_sum = 0
  current_set = set()
  group_start = True

  input = fileinput.input(files=inputfile)
  for line in input:
    if line == '\n':
      total_sum += len(current_set)
      current_set.clear()
      group_start = True
      continue

    new_set = set()

    for question in line:
      if question != '\n':
        if question in current_set or group_start:
          new_set.add(question)
    
    current_set = new_set
    group_start = False

  # last one
  total_sum += len(current_set)

  print(f"Answer: {total_sum}")

  input.close()
