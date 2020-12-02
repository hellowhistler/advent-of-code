with open('input.txt') as f:
    numbers = [int(string) for string in f.read().splitlines()]

for i in numbers:
    for j in numbers[1:]:
        if i + j == 2020:
            print(i * j)
            break
