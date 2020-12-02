with open('input.txt') as f:
    data = f.read().strip().splitlines()


def process_line(line: str) -> bool:
    minmax, char, string = line.split()
    low, high = map(int, minmax.split('-'))
    char = char.rstrip(':')
    count = string.count(char)
    if not low <= count <= high:
        return False
    return True


print(sum(map(process_line, data)))
