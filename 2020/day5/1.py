def decode_string(encoded: str, zero: str, one: str) -> int:
    as_binary = encoded.replace(zero, '0').replace(one, '1')
    return int(as_binary, 2)


def decode_seat(seat: str) -> tuple:
    row = decode_string(seat[:7], 'F', 'B')
    col = decode_string(seat[-3:], 'L', 'R')
    seat_id = 8 * row + col
    return row, col, seat_id


with open('test.txt') as f:
    data = f.read().strip().splitlines()

for d in data:
    print(d, *decode_seat(d))

with open('input.txt') as f:
    data = f.read().strip().splitlines()

rows, cols, seat_ids = zip(*[decode_seat(d) for d in data])

print(max(seat_ids))
