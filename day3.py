from input_reader import read_input


def part1(rucksacks):
    prioritiesLower = {chr(ord('a') + i): i + 1 for i in range(26)}

    duplicates = 0
    for rucksack in rucksacks:
        comp1 = rucksack[:len(rucksack) // 2]
        comp2 = rucksack[len(rucksack) // 2:]

        for char in set(comp1):
            if char in comp2:
                if char.isupper():
                    lower_case = char.lower()
                    duplicates = duplicates + prioritiesLower[lower_case] + 26
                else:
                    duplicates = duplicates + prioritiesLower[char]
    print(duplicates)


if __name__ == '__main__':
    input_data = read_input(3, str, False)
    part1(input_data)
