def run(inputfile):
  file = open(inputfile)
  jolts = file.readlines()
  file.close()

  for i in range(len(jolts)):
    jolts[i] = int(jolts[i])

  differences = {
    1: 0,
    2: 0,
    3: 0
  }

  jolts.sort()

  for i in range(len(jolts)):
    if i == 0:
      differences[jolts[i]] += 1
      continue

    differences[jolts[i] - jolts[i - 1]] += 1
    
  differences[3] += 1
  answer = differences[1] * differences[3]

  print(f"Answer: {answer}")