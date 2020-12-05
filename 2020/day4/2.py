import re
import traceback

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
required_fields = fields - {'cid'}


def extract_fields(passport: str) -> set:
    return set(field.split(':')[0] for field in passport.split())


def passport_is_valid(passport: str) -> bool:
    fields = {}
    for field in passport.split():
        name, _, val = field.partition(':')
        fields[name] = val
    if not required_fields.issubset(set(fields)):
        return False
    if not fields_are_valid(fields):
        return False
    return True


def fields_are_valid(fields: dict) -> bool:
    try:
        if byr := fields.get('byr'):
            assert len(byr) == 4
            assert 1920 <= int(byr) <= 2002
        if iyr := fields.get('iyr'):
            assert len(iyr) == 4
            assert 2010 <= int(iyr) <= 2020
        if eyr := fields.get('eyr'):
            assert len(eyr) == 4
            assert 2020 <= int(eyr) <= 2030
        if hgt := fields.get('hgt'):
            try:
                val, unit = re.match('^([0-9]+)(cm|in)$', hgt).groups()
            except AttributeError as e:
                # This statement seems to be not-always true (weirdly enough)
                # hgt (Height) - a number followed by either cm or in: 
                raise AssertionError from e
            if unit == 'cm':
                assert 150 <= int(val) <= 193
            elif unit == 'in':
                assert 59 <= int(val) <= 76
        if hcl := fields.get('hcl'):
            assert re.match('^#[0-9a-f]{6}$', hcl) is not None
        if ecl := fields.get('ecl'):
            assert ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        if pid := fields.get('pid'):
            assert re.match('^[0-9]{9}$', pid) is not None
    except AssertionError as e:
        # print('for next invalid reason', fields)
        # traceback.print_exc()
        return False
    except Exception as e:
        print(fields)
        raise e
    return True


def count_valid_passports(file: str) -> int:
    with open(file) as f:
        data = f.read().strip()
    passports = data.split('\n\n')
    valid_count = 0
    for passport in passports:
        if passport_is_valid(passport):
            valid_count += 1
    print(file, 'has', valid_count, 'passports out of', len(passports))
    return valid_count


count_valid_passports('test_valid.txt')
count_valid_passports('test_invalid.txt')
count_valid_passports('input.txt')
