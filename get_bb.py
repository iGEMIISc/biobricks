with open("parts.txt") as f:
    text = f.read()

parts_raw = [x.strip() for x in text.split(">")][1:]
parts = []
desc_lens = {}

for p in parts_raw:
    id = p.split(maxsplit=1)[0]
    part_type = p.split("\n", maxsplit=1)[0].split()[3]
    description = p.split('"', 1)[1].split('"', 1)[0]

    if len(description) not in desc_lens:
        desc_lens[len(description)] = 0
    desc_lens[len(description)] += 1

    parts.append({
        "id": id,
        "type": part_type,
        "description": description
    })


# Create a plot on the distribution of description lengths

# import matplotlib.pyplot as plt

# plt.bar(desc_lens.keys(), desc_lens.values())
# plt.xlabel("Description length")
# plt.ylabel("Number of parts")
# plt.title("Distribution of description lengths")
# plt.show()


# Parts with descriptions of length 0 to 4 (708 such parts)
# These are poor descriptions, and should be modified!

for_improvement = [x for x in parts if len(x["description"]) < 5]

# Parts with descriptions of length over 80 (758 such parts)
# These are good descriptions, and should be used for training!

for_training = [x for x in parts if len(x["description"]) > 80]

print(len(for_improvement), len(for_training))

