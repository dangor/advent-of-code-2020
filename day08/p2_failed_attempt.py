# failed attempt to work backward. gave up
def run(inputfile):
  file = open(inputfile)
  instructions = file.readlines()
  file.close()

  lines_run = get_lines_run(instructions)

  line_to_change = path_to_goal(len(instructions) - 1, instructions, lines_run)
  
  print((line_to_change, instructions[line_to_change]))

def get_lines_run(instructions):
  line_no = 0
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
      line_no += 1
      continue
    else: # jmp
      line_no += int(instruction[4:])
      continue

  return lines_run

def path_to_goal(goal_line, instructions, lines_run):
  cur_line = goal_line - 1
  while instructions[cur_line][:3] != 'jmp':
    cur_line -= 1
  
  if cur_line in lines_run:
    return cur_line # this 'jmp' should be changed to nop

  jmp_line = jmp_to_line_range(range(cur_line + 1, goal_line + 1), instructions, lines_run)

  if jmp_line in lines_run:
    return jmp_line # this 'nop' should be changed to jmp
  
  return path_to_goal(jmp_line, instructions, lines_run)

def jmp_to_line_range(line_range, instructions, lines_run):
  print(line_range)
  # inefficient but meh?
  for i in range(len(instructions)):
    instruction = instructions[i]
    if (instruction[:3] == 'nop' or instruction[:3] == 'jmp') and i + int(instruction[4:]) in line_range:
      if instruction[:3] == 'nop' and i in lines_run:
        return i
      elif instruction[:3] == 'jmp':
        return i