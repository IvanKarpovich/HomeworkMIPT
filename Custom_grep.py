from typing import List

def grep(pattern: str, file: str) -> List[str]:

    with open(file, 'r', encoding='utf8') as f:
        for line in f:    
            if line.find(pattern) != -1:
                print( line )

params = input().split()
grep( *params )

