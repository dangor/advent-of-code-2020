def run():
  input = [2,20,0,4,1,17]
  tracker = {}

  for i in range(len(input) - 1):
    tracker[input[i]] = i

  current = input[-1]
    
  for i in range(len(input) - 1, 2019):
    if current not in tracker:
      tracker[current] = i
      current = 0
    else:
      diff = i - tracker[current]
      tracker[current] = i
      current = diff

  print(f"Answer: {current}")