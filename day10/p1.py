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
  jolts.insert(0, 0)
  jolts.append(jolts[-1] + 3)

  for i in range(1, len(jolts)):
    differences[jolts[i] - jolts[i - 1]] += 1
    
  answer = differences[1] * differences[3]

  print(f"Answer: {answer}")