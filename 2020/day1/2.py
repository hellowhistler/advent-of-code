with open('input.txt') as f:
    numbers = [int(string) for string in f.read().splitlines()]

for i in numbers:
    for j in numbers[1:]:
        if i + j > 2020:
            continue
        for k in numbers[2:]:
            if i + j + k == 2020:
                print(i * j * k)
