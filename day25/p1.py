def run(card_pub_key, door_pub_key):
  subject_number = 7
  mod_number = 20201227
  card_loops = 0
  door_loops = 0 # unused

  card_value = 1
  while card_value != card_pub_key:
    card_value *= subject_number
    card_value %= mod_number
    card_loops += 1

  encryption_key = 1
  for i in range(card_loops):
    encryption_key *= door_pub_key
    encryption_key %= mod_number

  print(f"Answer: {encryption_key}")