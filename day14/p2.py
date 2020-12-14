import fileinput
import re

def run(inputfile):
  mask_one = None
  mask_bits = []
  memory = {}

  input = fileinput.input(files=inputfile)
  for line in input:
    if line[:4] == 'mask':
      mask_bits.clear()
      mask_string = line[7:43]
      mask_one = int(mask_string.replace('X', '0'), 2)
      mask_bits = [(35 - i) for i, x in enumerate(mask_string) if x == 'X']
      continue
    
    match = re.search('mem\[(?P<index>\d+)\] = (?P<value>\d+)', line)

    base_index = int(match.group('index'))
    value = int(match.group('value'))

    masked_index = int(base_index) | mask_one
    indices = mask_indices(masked_index, mask_bits)

    for index in indices:
      memory[index] = value

  sum = 0
  for index, value in memory.items():
    sum += value

  print(f"Answer: {sum}")
  input.close()

def mask_indices(index, remaining_mask_bits):
  if len(remaining_mask_bits) == 0:
    return [index]

  indices = []
  mask_bit_index = remaining_mask_bits[0]

  masked_1 = index | (1 << mask_bit_index)
  indices.extend(mask_indices(masked_1, remaining_mask_bits[1:]))

  masked_0 = index & ~(1 << mask_bit_index)
  indices.extend(mask_indices(masked_0, remaining_mask_bits[1:]))

  return indices