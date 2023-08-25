import csv
import random

with open("parts.txt") as f:
    text = f.read()

parts_raw = [x.strip() for x in text.split(">")][1:]
parts = [('Type', 'Description', 'Rating1', 'Rating2', 'Rating3')]

for part in parts_raw:
    line = part.split("\n")[0].split(maxsplit=4)
    part_type = line[3]
    part_desc = line[4].strip("\"")
    parts.append((part_type, part_desc, '', '', ''))

random.shuffle(parts)

with open("parts.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(parts)
