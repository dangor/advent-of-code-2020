import fileinput
import itertools

# some thoughts:
# messages min max: 24, 88
# string len of rule 8: 8
# string len of rule 11: 16
# string len of rule 0: 24
# well duh: rule 0 = 8 11
# new rule 8: 42 | 42 8, meaning 8 duplicated 0..n times
# new rule 11: 42 31 | 42 11 31, meaning 8 + 31, or 8 + 8 + 31 + 31, etc.
# string len of 31 is 8 chars
# 0 is basically strings 42 repeated some number of times, and strings 31 repeated some number of times, where the former is repeated at least once more than 31
# forget 8 and 11 (and even 0), and manually manage 42 and 31. i think that's what the hint meant

def run(inputfile):
  input = parse(inputfile)

  rule_31 = set(process_rule(input['rules'], 31))
  rule_42 = set(process_rule(input['rules'], 42))

  count = 0
  for message in input['messages']:
    if is_valid(message, rule_31, rule_42):
      count += 1

  print(f"Answer: {count}")

def parse(inputfile):
  rules = {}
  messages = []
  reading_rules = True
  input = fileinput.input(files=inputfile)
  for line in input:
    stripped = line.strip('\n')
    if stripped == '':
      reading_rules = False
      continue

    if reading_rules:
      split1 = stripped.split(': ')
      index = int(split1[0])
      rule = split1[1]

      if rule[0] == '"':
        rules[index] = rule.strip('"')
        continue

      rule_list = []
      split_rules = rule.split('|')
      for split_rule in split_rules:
        rule_list.append(list(map(int, split_rule.strip(' ').split(' '))))
      rules[index] = rule_list
    else:
      messages.append(stripped)
  input.close()

  return {
    'rules': rules,
    'messages': messages
  }

def process_rule(rules, i, mem={}):
  if i in mem:
    return mem[i]

  strings = []

  rule = rules[i]
  if rule == 'a' or rule == 'b':
    strings.append(rule)
    mem[i] = strings
    return strings

  for r in rule: # [[1 2], [2 1]]
    substrings = []
    for num in r: # [1, 2]
      substrings.append(process_rule(rules, num, mem))

    strings.extend(list(map(''.join, itertools.product(*substrings))))

  return strings

def is_valid(message, rule_31, rule_42):
  if message[-8:] not in rule_31:
    return False

  if message[:8] not in rule_42:
    return False

  if message[8:16] not in rule_42:
    return False

  remaining = message[16:len(message) - 8]
  still_counting_31s = True

  while len(remaining) > 0:
    if len(remaining) % 8 != 0:
      return False
    
    if remaining[:8] not in rule_42:
      return False

    if len(remaining) == 8:
      remaining = ''
      continue

    # len >= 16
    tail = remaining[-8:]

    if still_counting_31s and tail not in rule_31:
      still_counting_31s = False

    if not still_counting_31s and tail not in rule_42:
      return False

    remaining = remaining[8:len(remaining) - 8]

  return True