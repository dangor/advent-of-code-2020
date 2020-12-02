import fileinput

def p2(inputfile):
  entries = set()
  input = fileinput.input(files=inputfile)
  for line in input:
    entry = int(line)
    for other in entries:
      if other + entry > 2020:
        continue
      elif 2020 - other - entry in entries:
        answer = (2020 - other - entry) * other * entry
        print(f"Answer: {answer}")
        input.close()
        return
    entries.add(entry)
  input.close()