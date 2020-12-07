import fileinput
import re

containees = {} # dict of bags and list of containees, duplicates mean the container contains multiple of that containee

def run(inputfile):
  input = fileinput.input(files=inputfile)
  parse_containees(input)
  input.close()

  gold_containees = get_containees_recursively('shiny gold')

  print(f"Answer: {len(gold_containees)}")

def parse_containees(input):
  for line in input:
    match = re.search('^(\w+ \w+) bags contain ', line)
    container = match.group(1)
    containees[container] = []

    if "no other bags" in line:
      continue

    matches = re.findall('(\d+) (\w+ \w+) bags?', line)
    for match in matches:
      count, name = match
      containees[container].extend([name]*int(count)) # add the name 'count' times

def get_containees_recursively(bag_color):
  direct_children = containees[bag_color]
  all_children = direct_children.copy()
  for direct_child in direct_children:
    descendants = get_containees_recursively(direct_child)
    all_children.extend(descendants)
  return all_children
