import fileinput
import sys
class Day1:
    def part1(filename):
        lst = []
        calories = 0
        for line in fileinput.input(filename,encoding='UTF-8'):
            if line.strip():
                calories = calories + int(line)
            else:
                lst.append(int(calories))
                calories = 0
                continue
        return lst
list = Day1.part1(sys.argv[1:])
list.sort()
print(list[-3:])
print(sum(list[-3:]))
        