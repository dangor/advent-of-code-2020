import fileinput

def p1(inputfile):
  entries = set()
  input = fileinput.input(files=inputfile)
  for line in input:
    entry = int(line)
    if 2020 - entry in entries:
      answer = (2020 - entry) * entry
      print(f"Answer: {answer}")
      break
    entries.add(entry)
  input.close()