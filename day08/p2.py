# brute force change one instruction and try again
def run(inputfile):
  file = open(inputfile)
  instructions = file.readlines()
  file.close()

  initial_run = run_instructions(instructions)
  initial_lines_run = initial_run['lines_run']

  for line_no in range(len(initial_lines_run)):
    instruction = instructions[line_no]
    if instruction[:3] == 'acc':
      continue

    mutated_instructions = instructions.copy()
    if instruction[:3] == 'jmp':
      mutated_instructions[line_no] = mutated_instructions[line_no].replace('jmp', 'nop')
    else:
      mutated_instructions[line_no] = mutated_instructions[line_no].replace('nop', 'jmp')

    new_run = run_instructions(mutated_instructions)

    if new_run['loop']:
      continue
    else:
      print(f"Answer: {new_run['acc']}")
      return

def run_instructions(instructions):
  line_no = 0
  acc = 0
  lines_run = []

  while line_no < len(instructions):
    if line_no in lines_run:
      return {
        'acc': acc,
        'lines_run': lines_run,
        'loop': True
      }

    lines_run.append(line_no)
    instruction = instructions[line_no]

    if instruction[:3] == 'nop':
      line_no += 1
      continue
    elif instruction[:3] == 'acc':
      acc += int(instruction[4:])
      line_no += 1
      continue
    else: # jmp
      line_no += int(instruction[4:])
      continue

  return {
    'acc': acc,
    'lines_run': lines_run,
    'loop': False
  }
