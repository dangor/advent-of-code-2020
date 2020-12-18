def run(inputfile):
  file = open(inputfile)
  equations = list(x.strip('\n').replace(' ', '') for x in file.readlines())
  file.close()

  sum = 0
  for equation in equations:
    result = evaluate(equation)
    sum += result

  print(f"Answer: {sum}")

def evaluate(equation):
  terms = []
  operators = []

  # parse and collapse groups
  for char in equation:
    if char == '(':
      operators.insert(0, char)
    elif char == ')':
      first = operators.index('(')
      op_group = operators[:first]
      operators = operators[first + 1:]

      term_group = terms[:first + 1]
      terms = terms[first + 1:]

      group_result = evaluate_group(term_group, op_group)
      terms.insert(0, group_result)

    elif char in ['+', '*']:
      operators.insert(0, char)
    else:
      terms.insert(0, int(char))
  return evaluate_group(terms, operators)

def evaluate_group(terms, operators):
  terms.reverse()
  operators.reverse()

  while '+' in operators:
    first = operators.index('+')
    operators.pop(first)
    sum = terms.pop(first) + terms.pop(first)
    terms.insert(first, sum)

  product = 1
  for factor in terms:
    product *= factor

  return product