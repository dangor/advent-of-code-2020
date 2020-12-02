import fileinput

def p1(inputfile):
  entries = set()
  for line in fileinput.input(files=inputfile):
    entry = int(line)
    if 2020 - entry in entries:
      answer = (2020 - entry) * entry
      print(f"Answer: {answer}")
      break
    entries.add(entry)