import fileinput

def run(inputfile):
  input = parse(inputfile)

  bad_ingredients = set()
  for possibilities in input['allergen_possibililities'].values():
    bad_ingredients.update(possibilities)

  count = 0
  for appearance in input['appearances']:
    if appearance not in bad_ingredients:
      count += 1

  print(f"Answer: {count}")

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