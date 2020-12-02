import re
import fileinput

def run(inputfile):
  valid_passwords = 0
  input = fileinput.input(files=inputfile)
  for line in input:
    match = re.search('(\d+)-(\d+) (\w): (\S+)', line)
    first_index = int(match.group(1)) - 1
    second_index = int(match.group(2)) - 1
    letter = match.group(3)
    password = match.group(4)
    match_count = 0
    if password[first_index] == letter:
      match_count += 1
    if password[second_index] == letter:
      match_count += 1
    if match_count == 1:
      valid_passwords += 1
  print (f"Answer: {valid_passwords}")
  input.close()