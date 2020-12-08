# unclever /shrug
def run(inputfile):
  file = open(inputfile)
  instructions = file.readlines()
  file.close()

  line_no = 0
  acc = 0
  lines_run = set()

  while True:
    if line_no in lines_run:
      break

    lines_run.add(line_no)
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

  print(f"Answer: {acc}")

