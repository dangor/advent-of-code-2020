def run(inputfile):
  file = open(inputfile)
  data = list(x.strip('\n') for x in file.readlines())
  file.close()

  earliest = int(data[0])
  time = earliest
  bus_ids = list(map(int, filter(lambda x: x != 'x', data[1].split(','))))

  while True:
    for id in bus_ids:
      if time % id == 0:
        answer = (time - earliest) * id
        print(f"Answer: {answer}")
        return
    time += 1