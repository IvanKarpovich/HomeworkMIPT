import re

STRING = 'Шарик красный: 100\nШарик синий: 110\nКофе зерновой: 1000\nШарик пурпурный: 200\nКекс с изюмом: 200'
re.sub(r'(Шар.+\b\d+)\d', r'\1', string = STRING)