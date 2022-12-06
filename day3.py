from input_reader import read_input


def part1(rucksacks):
    priorities_lower = {chr(ord('a') + i): i + 1 for i in range(26)}

    duplicates = 0
    for rucksack in rucksacks:
        comp1 = rucksack[:len(rucksack) // 2]
        comp2 = rucksack[len(rucksack) // 2:]

        for char in set(comp1):
            if char in comp2:
                if char.isupper():
                    lower_case = char.lower()
                    duplicates = duplicates + priorities_lower[lower_case] + 26
                else:
                    duplicates = duplicates + priorities_lower[char]
    print(duplicates)


def part2(rucksacks):
    priorities_lower = {chr(ord('a') + i): i + 1 for i in range(26)}

    duplicates = 0
    for index in range(0, len(rucksacks), 3):
        first_set = set(rucksacks[index])
        second_set = set(rucksacks[index + 1])
        third_set = set(rucksacks[index + 2])

        for char in first_set:
            if char in second_set:
                if char in third_set:
                    if char.isupper():
                        lower_case = char.lower()
                        duplicates = duplicates + priorities_lower[lower_case] + 26
                    else:
                        duplicates = duplicates + priorities_lower[char]
    print(duplicates)


if __name__ == '__main__':
    input_data = read_input(3, str, False)
    part1(input_data)
    part2(input_data)
