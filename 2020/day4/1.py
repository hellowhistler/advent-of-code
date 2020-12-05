fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
required_fields = fields - {'cid'}

with open('input.txt') as f:
    data = f.read().strip()
passports = data.split('\n\n')


def extract_fields(passport: str) -> set:
    return set(field.split(':')[0] for field in passport.split())


valid_count = 0
for passport in passports:
    actual_fields = extract_fields(passport)
    if required_fields - actual_fields == set():
        valid_count += 1

print(valid_count)
