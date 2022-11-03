from typing import List

def grep(pattern: str, file: str) -> List[str]:
    found_lines = []
    with open(file, 'r', encoding='utf8') as f:
        for line in f:    
            if pattern in line:
                found_lines.append(line)
    return found_lines

params = input().split()
grep( *params )

