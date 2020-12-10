def run(inputfile):
  file = open(inputfile)
  jolts = file.readlines()
  file.close()

  for i in range(len(jolts)):
    jolts[i] = int(jolts[i])

  jolts.sort()
  jolts.insert(0, 0)
  jolts.append(jolts[-1] + 3)

  # I'm calling the length of a series of differences of 1s a "one_count"
  current_one_count = 0
  one_counts = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
  }

  for i in range(1, len(jolts)):
    if jolts[i] - jolts[i - 1] == 1:
      current_one_count += 1
    elif current_one_count > 0:
      one_counts[current_one_count] += 1
      current_one_count = 0

  # one_count of 1 is 2*0 combos = 1
  # one_count of 2 is 2*1 combos = 2
  # one_count of 3 is 2*2 combos = 4
  # one_count of 4 is 7 combos, i.e.:
  # [1, 2, 3, 4], [2, 3, 4], [1, 3, 4], [1, 2, 4], [3, 4], [2, 4], [1, 4]
  # Didn't see any one_counts of 5

  answer = (2**one_counts[2]) * (4**one_counts[3]) * (7**one_counts[4])

  print(f"Answer: {answer}")