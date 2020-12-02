import re
import fileinput

def run(inputfile):
  valid_passwords = 0
  input = fileinput.input(files=inputfile)
  for line in input:
    match = re.search('(\d+)-(\d+) (\w): (\S+)', line)
    low_bound = int(match.group(1))
    high_bound = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    count = password.count(letter)
    if count >= low_bound and count <= high_bound:
      valid_passwords += 1
  print (f"Answer: {valid_passwords}")
  input.close()