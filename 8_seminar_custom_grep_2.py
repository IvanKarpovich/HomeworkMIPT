from typing import Iterable

#генератор с использованием yield
def grep(pattern: str, file: str) -> Iterable[str]:
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            if pattern in line: 
                yield line #последним элементом во всех строках кроме последней будет '\n'

for line in grep(pattern="How could I know", file="Lost_in_Space.txt"):
    print(line)
