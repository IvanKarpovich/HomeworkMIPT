class ConsoleIterator: #iterable and iterator
  def __init__(self):
    pass

  def __iter__(self):
    return self

  def __next__(self):
    next_int = input()
    if next_int.isdigit():
      return int(next_int)
    raise StopIteration


total_sum = 0

for number in ConsoleIterator():
    total_sum = total_sum + number

print(f"Sum of entered numbers is {total_sum}")
