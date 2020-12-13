def run(inputfile):
  file = open(inputfile)
  data = list(x.strip('\n') for x in file.readlines())
  file.close()

  bus_ids = data[1].split(',')
  id_sequence = []
  for i in range(len(bus_ids)):
    if bus_ids[i] != 'x':
      id_sequence.append((int(bus_ids[i]), i))

  timestamp = int(data[0])
  step = 1

  while len(id_sequence) > 0:
    test = id_sequence[0]
    if (timestamp + test[1]) % test[0] == 0:
      step *= test[0]
      id_sequence.pop(0)
    else:
      timestamp += step      

  print(f"Answer: {timestamp}")
