from input_reader import read_input


def part1(input_data):
    fully_contained_count = 0
    for pairs in input_data:
        pair1, pair2 = pairs.split(',')
        pair1_start_end = pair1.split('-')
        pair2_start_end = pair2.split('-')
        first_pair_sections = []
        second_pair_sections = []

        if pair1_start_end[0] == pair1_start_end[1]:
            first_pair_sections.append(int(pair1_start_end[0]))
        else:
            for section in range(int(pair1_start_end[0]), int(pair1_start_end[1]) + 1):
                first_pair_sections.append(section)
        if pair2_start_end[0] == pair2_start_end[1]:
            second_pair_sections.append(int(pair2_start_end[0]))
        else:
            for section in range(int(pair2_start_end[0]), int(pair2_start_end[1]) + 1):
                second_pair_sections.append(section)

        if set(second_pair_sections).issubset(set(first_pair_sections)):
            fully_contained_count = fully_contained_count + 1
        else:
            if set(first_pair_sections).issubset(set(second_pair_sections)):
                fully_contained_count = fully_contained_count + 1

    print(fully_contained_count)


def part2(input_data):
    overlapped_count = 0
    for pairs in input_data:
        pair1, pair2 = pairs.split(',')
        pair1_start_end = pair1.split('-')
        pair2_start_end = pair2.split('-')
        first_pair_sections = []
        second_pair_sections = []
        if pair1_start_end[0] == pair1_start_end[1]:
            first_pair_sections.append(int(pair1_start_end[0]))
        else:
            for section in range(int(pair1_start_end[0]), int(pair1_start_end[1]) + 1):
                first_pair_sections.append(section)
        if pair2_start_end[0] == pair2_start_end[1]:
            second_pair_sections.append(int(pair2_start_end[0]))
        else:
            for section in range(int(pair2_start_end[0]), int(pair2_start_end[1]) + 1):
                second_pair_sections.append(section)

        overlapFound = False
        for section in first_pair_sections:
            if section in second_pair_sections:
                overlapped_count = overlapped_count + 1
                overlapFound = True
                break

        if not overlapFound:
            for section in second_pair_sections:
                if section in first_pair_sections:
                    overlapped_count = overlapped_count + 1
                    break
    print(overlapped_count)


if __name__ == '__main__':
    input_data = read_input(4, str, False)
    part1(input_data)
    part2(input_data)
