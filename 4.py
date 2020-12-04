with open('4-input.txt') as file:
    data = file.read()

passports = data.strip().split('\n\n')


def is_valid_1(passport):
    passport = passport.replace('\n', ' ')
    terms = {
        term.split(':')[0].strip(): term.split(':')[1].strip()
        for term in passport.split(' ')
    }

    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if required - set(terms):
        return False
    else:
        return True


def is_valid_2(passport):
    passport = passport.replace('\n', ' ')
    terms = {
        term.split(':')[0].strip(): term.split(':')[1].strip()
        for term in passport.split(' ')
    }

    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if required - set(terms):
        return False

    try:
        # years
        terms['byr'] = int(terms['byr'])
        if terms['byr'] < 1920 or terms['byr'] > 2002:
            return False
        terms['iyr'] = int(terms['iyr'])
        if terms['iyr'] < 2010 or terms['iyr'] > 2020:
            return False
        terms['eyr'] = int(terms['eyr'])
        if terms['eyr'] < 2020 or terms['eyr'] > 2030:
            return False

        # height
        terms['hgt_num'] = float(terms['hgt'][:-2])
        terms['hgt_unit'] = terms['hgt'][-2:]
        if terms['hgt_unit'] == 'cm':
            if terms['hgt_num'] < 150 or terms['hgt_num'] > 193:
                return False
        elif terms['hgt_unit'] == 'in':
            if terms['hgt_num'] < 59 or terms['hgt_num'] > 76:
                return False
        else:
            return False

        # hair and eye colour
        if terms['hcl'][0] != '#':
            return False
        elif len(terms['hcl']) != 7:
            return False
        else:
            # if this doesn't error, we're okay
            int(terms['hcl'][1:], 16)

        if terms['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        # passport ID
        if len(terms['pid']) != 9:
            return False
        else:
            # if this doesn't error, we're okay
            int(terms['pid'])
    except:
        return False
    return True


print('part 1')
count = 0
for passport in passports:
    if is_valid_1(passport):
        count += 1
print('answer: {}'.format(count))


print('\n')
print('part 2')
count = 0
for passport in passports:
    if is_valid_2(passport):
        count += 1
print('answer: {}'.format(count))
