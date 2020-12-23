class Cup(object):
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

  def set_next(self, next):
    self.next = next

class Cups(object):
  def __init__(self, initial_list, max):
    self.lookup = {}

    previous = None
    head = None

    for value in initial_list:
      node = Cup(value)
      self.lookup[value] = node
      
      if head == None:
        head = node

      if previous != None:
        previous.set_next(node)

      previous = node

    # extend to max
    for value in range(len(initial_list) + 1, max + 1):
      node = Cup(value)
      self.lookup[value] = node
      previous.set_next(node)
      previous = node

    # make a loop
    previous.set_next(head)

    self.current = head

  def remove3(self):
    removed = self.current.next

    cur = removed
    for i in range(3):
      self.lookup.pop(cur.value)
      cur = cur.next

    self.current.set_next(cur)

    return removed

  def get_node(self, value):
    return self.lookup.get(value)

  def insert3_after(self, node, to_insert):
    next = node.next
    node.set_next(to_insert)

    current = node
    for i in range(3):
      current = current.next
      self.lookup[current.value] = current
    
    current.set_next(next)

  def iterate(self):
    self.current = self.current.next

def run(input):
  max = 1000000
  initial = list(map(int, input))

  cups = Cups(initial, max)

  for move in range(10000000):
    if move % 100000 == 0:
      print(f"\rProgress: {int(move * 100 / 10000000 // 1)}%", end = '\r', flush = True)
  
    removed = cups.remove3()

    value = cups.current.value
    marker = None
    while not marker:
      value -= 1
      if value < 1:
        value = max
      marker = cups.get_node(value)

    cups.insert3_after(marker, removed)

    cups.iterate()

  one = cups.lookup[1]
  answer = one.next.value * one.next.next.value

  print(f"\nAnswer: {answer}")