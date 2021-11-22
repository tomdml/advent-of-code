import re

with open('input.txt') as fp:
    entries = fp.read().split('\n\n')
    entries = [[pair.split(':') for pair in entry.split()] for entry in entries]
    entries = [{key: value for key, value in entry} for entry in entries]


def filter_keys_present(entries):
    required_keys = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    return [entry for entry in entries if entry.keys() >= required_keys]


def filter_keys_valid(entries):

    def check(entry):
        hgt = entry['hgt']
        checks = [
            1920 <= int(entry['byr']) <= 2002,
            2010 <= int(entry['iyr']) <= 2020,
            2020 <= int(entry['eyr']) <= 2030,
            150 <= int(hgt.strip('cm')) <= 193 if hgt.endswith('cm')
            else 59 <= int(hgt.strip('in')) <= 76 if hgt.endswith('in')
            else False,
            re.match('#[0-9a-f]{6}', entry['hcl']),
            entry['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
            len(entry['pid']) == 9 and entry['pid'].isdigit()
        ]

        return all(checks)

    return [entry for entry in filter_keys_present(entries) if check(entry)]


print(len(filter_keys_present(entries)))
print(len(filter_keys_valid(entries)))
