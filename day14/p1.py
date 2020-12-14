import fileinput
import re

def run(inputfile):
  mask_one = None
  mask_zero = None
  memory = {}

  input = fileinput.input(files=inputfile)
  for line in input:
    if line[:4] == 'mask':
      mask_string = line[7:43]
      mask_one = int(mask_string.replace('X', '0'), 2)
      mask_zero = int(mask_string.replace('X', '1'), 2)
      continue
    
    match = re.search('mem\[(?P<index>\d+)\] = (?P<value>\d+)', line)

    index = int(match.group('index'))
    value = int(match.group('value'))

    memory[index] = (value & mask_zero) | mask_one

  sum = 0
  for index, value in memory.items():
    sum += value

  print(f"Answer: {sum}")
  input.close()