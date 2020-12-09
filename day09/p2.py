import fileinput

def run(inputfile):
  invalid_num = 556543474
  windows = []

  input = fileinput.input(files=inputfile)
  for line in input:
    num = int(line)

    to_drop = []

    for i in range(len(windows)):
      window = windows[i]
      window.append(num)
      total = sum(window)

      if total == invalid_num:
        answer = compute_answer(window)
        print(f"Answer: {answer}")
        input.close()
        return

      if total > invalid_num:
        to_drop.append(i)

    while len(to_drop) > 0:
      i = to_drop.pop()
      windows.pop(i)

    windows.append([num])

  input.close()

def compute_answer(window):
  window.sort()
  return window[0] + window[-1]