import re

def run(inputfile):
  file = open(inputfile)
  data = list(x.strip('\n') for x in file.readlines())
  file.close()

  valid = set()

  for line in data:
    if line == '':
      break
    
    match = re.search('(\d+)-(\d+) or (\d+)-(\d+)', line)
    valid.update(range(int(match.group(1)), int(match.group(2)) + 1))
    valid.update(range(int(match.group(3)), int(match.group(4)) + 1))

  sum = 0
  nearby = False

  for line in data:
    if line == "nearby tickets:":
      nearby = True
      continue
    if not nearby:
      continue
  
    nums = line.split(',')
    for num in nums:
      i = int(num)
      if i not in valid:
        sum += i

  print(f"Answer: {sum}")
