import fileinput
import re

containers = {} # dict of bags and list of container parents

def run(inputfile):
  input = fileinput.input(files=inputfile)
  parse_containers(input)
  input.close()

  gold_containers = get_container_recursively('shiny gold')

  print(f"Answer: {len(gold_containers)}")

def parse_containers(input):
  for line in input:
    if "no other bags" in line:
      continue

    match = re.search('^(\w+ \w+) bags contain ', line)
    container = match.group(1)

    matches = re.findall('\d+ (\w+ \w+) bags?', line)
    for match in matches:
      if match not in containers:
        containers[match] = []
      containers[match].append(container)

def get_container_recursively(bag_color):
  if bag_color not in containers:
    return set()
  
  direct_parents = containers[bag_color]
  all_parents = set(direct_parents)
  for direct_parent in direct_parents:
    ancestors = get_container_recursively(direct_parent)
    all_parents.update(ancestors)

  return all_parents
