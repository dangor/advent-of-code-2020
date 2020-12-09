import fileinput

def run(inputfile):
  i = 0
  preamble = []

  input = fileinput.input(files=inputfile)
  for line in input:
    num = int(line)
    if i < 25:
      preamble.append(num)
      i += 1
      continue

    if not is_valid(num, preamble):
      print(f"Answer: {num}")
      break

    preamble.pop(0)
    preamble.append(num)

  input.close()

def is_valid(num, preamble):
  for previous in preamble:
    if previous * 2 == num:
      continue

    if (num - previous) in preamble:
      return True

  return False