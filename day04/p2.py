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
  if not all(key in passport for key in required):
    return False

  if not 1920 <= int(passport['byr']) <= 2002:
    return False

  if not 2010 <= int(passport['iyr']) <= 2020:
    return False

  if not 2020 <= int(passport['eyr']) <= 2030:
    return False

  if not is_height_valid(passport['hgt']):
    return False

  if re.match('^#[0-9a-f]{6}$', passport['hcl']) == None:
    return False

  valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  if passport['ecl'] not in valid_ecl:
    return False

  if re.match('^\d{9}$', passport['pid']) == None:
    return False

  return True

def is_height_valid(height):
  m = re.match('^(\d+)(cm|in)$', height)
  if m == None:
    return False
  
  (num, unit) = m.groups()

  if unit == 'cm' and not 150 <= int(num) <= 193:
    return False

  if unit == 'in' and not 59 <= int(num) <= 76:
    return False

  return True