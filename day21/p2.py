import fileinput

def run(inputfile):
  input = parse(inputfile)

  allergen_possibilities = input['allergen_possibililities']
  claimed_ingredients = set()
  allergen_map = {}

  while len(allergen_possibilities) > 0:    
    for allergen, possibilities in allergen_possibilities.items():
      possibilities = possibilities.difference(claimed_ingredients)
      if len(possibilities) == 1:
        claimed_ingredients.add(list(possibilities)[0])
        allergen_map[allergen] = list(possibilities)[0]
        allergen_possibilities.pop(allergen)
        break

  ordered_keys = list(allergen_map.keys())
  ordered_keys.sort()

  answer = ''
  for allergen in ordered_keys:
    answer += allergen_map[allergen] + ','
  
  print(f"Answer: {answer.strip(',')}")

def parse(inputfile):
  appearances = []
  allergen_possibililities = {}

  input = fileinput.input(files=inputfile)
  for line in input:
    components = line.strip('\n').strip(')').split(' (contains ')
    
    words = components[0].split(' ')
    appearances.extend(words)
    
    allergens = components[1].split(', ')
    for allergen in allergens:
      if allergen not in allergen_possibililities:
        allergen_possibililities[allergen] = set(words)
      else:
        allergen_possibililities[allergen] = set(words).intersection(allergen_possibililities[allergen])

  input.close()

  return {
    'appearances': appearances,
    'allergen_possibililities': allergen_possibililities
  }