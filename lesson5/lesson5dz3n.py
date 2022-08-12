import random
import re

with open('test_file.txt', 'w', encoding='utf-8') as f:
    n = [str(random.randint(0, 9)) for _ in range(2500)]
    n = str(random.randint(1, 9)) + ''.join(n)
    f.write(n)

with open('test_file.txt', 'r', encoding='utf-8') as f:
    number = f.readline()
    sample = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
             '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
    sequence = re.findall(sample, number)
    longest_sequence = []
    [longest_sequence.insert(0, i) for i in sequence if len(i) > len(longest_sequence)]
    print(longest_sequence[0])
