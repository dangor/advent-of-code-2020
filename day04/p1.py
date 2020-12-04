import fileinput
import re

def run(inputfile):
  valid_count = 0
  current_passport = {}
  input = fileinput.input(files=inputfile)
  for line in input:
    if line == '\n':
      if is_valid(current_passport):
        valid_count += 1
      current_passport.clear()
      continue

    matches = re.findall('(\S+):(\S+)', line)
    for match in matches:
      current_passport[match[0]] = match[1]

  # check last one too
  if is_valid(current_passport):
    valid_count += 1

  print(f"Answer: {valid_count}")

  input.close()

def is_valid(passport):
  required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  return all(key in passport for key in required)