with open('input.txt') as f:
    data = f.read().strip().splitlines()


def process_line(line: str) -> bool:
    minmax, char, string = line.split()
    low, high = map(int, minmax.split('-'))
    char = char.rstrip(':')
    count = (string[low - 1] == char) + (string[high - 1] == char)
    return count == 1


print(sum(map(process_line, data)))
