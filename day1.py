from input_reader import read_input


def part1(summedCalories):
    summedCaloriesPerElf(summedCalories)
    print(max(summedCalories))


def part2(inputData):
   summedCalories = summedCaloriesPerElf(inputData)
   summedCalories.sort(reverse=True)
   print(sum(summedCalories[:3]))



def summedCaloriesPerElf(inputData):
    summedCalories = []
    tempSum = 0
    for value in inputData:
        if value:
            tempSum = tempSum + int(value)
        else:
            summedCalories.append(tempSum)
            tempSum = 0
    summedCalories.append(tempSum)
    return summedCalories


if __name__ == '__main__':
    summedCalories = read_input(1, str, False)
    part1(summedCalories)
    part2(summedCalories)
