import fileinput
import itertools

def run(inputfile):
  input = parse(inputfile)

  valid = set(process_rule(input['rules'], 0))

  count = 0
  for message in input['messages']:
    if message in valid:
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