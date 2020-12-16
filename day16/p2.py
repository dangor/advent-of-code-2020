import re

# i laugh in the face of cyclomatic complexity
def run(inputfile):
  file = open(inputfile)
  data = list(x.strip('\n') for x in file.readlines())
  file.close()

  valid = set()
  rules = {}
  your_ticket = None

  for i, line in enumerate(data):
    if line == '' or line == 'your ticket:':
      continue
    elif ',' in line:
      your_ticket = list(map(int, line.split(',')))
      break
    
    # still in validity area
    match = re.search('(\d+)-(\d+) or (\d+)-(\d+)', line)
    first_range = range(int(match.group(1)), int(match.group(2)) + 1)
    second_range = range(int(match.group(3)), int(match.group(4)) + 1)
    valid.update(first_range)
    valid.update(second_range)

    rules[i] = set(first_range)
    rules[i].update(second_range)

  nearby = False
  possibilities = { key: set(range(len(your_ticket))) for key in rules.keys() }

  for line in data:
    if line == "nearby tickets:":
      nearby = True
      continue
    if not nearby:
      continue

    # nearby
    valid_ticket = True
    nums = list(map(int, line.split(',')))
    for num in nums:
      if num not in valid:
        valid_ticket = False

    if not valid_ticket:
      continue

    # nearby valid
    for pos, num in enumerate(nums):
      for i, possible_positions in possibilities.items():
        if pos not in possible_positions:
          continue # already eliminated
        
        if num not in rules[i]:
          possible_positions.remove(pos)

  deduped = dedupe(possibilities)

  answer = 1
  for i, line in enumerate(data):
    if line.find('departure') == 0:
      pos = deduped[i]
      answer *= your_ticket[pos]

  print(f"Answer: {answer}")

def dedupe(possibilities):
  deduped = {}
  for i in range(len(possibilities)):
    claim_value = None
    claim_key = None
    for key, value in possibilities.items():
      if len(value) == 1:
        claim_value = list(value)[0]
        claim_key = key
        deduped[claim_key] = claim_value
        possibilities.pop(claim_key)
        break

    for key, value in possibilities.items():
      if key != claim_key and claim_value in value:
        value.remove(claim_value)

  return deduped