import re


def checkvalid(filepath: str) -> list:

    keys = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    valid = 0
    pp = []

    def validate(pp):
        for i in range(len(pp)):
            pp[i] = pp[i].split(':')[0]
        return all(k in pp for k in keys)        

    with open(filepath) as f:        
        for line in f:
            if line == "\n":
                valid += validate(pp)
                pp = []
                continue
            pp.extend(line.split())        
        valid += validate(pp) # for last passport
    return valid


def checkvalid_2(filepath: str) -> list:

    keys = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    valid = 0
    pp = []

    def validate(pp):
        d = {}
        for i in range(len(pp)):
            s = pp[i].split(':')
            d[s[0]] = s[1]
        if all(k in d for k in keys):
            if len(d['byr']) != 4 or int(d['byr']) < 1920 or int(d['byr']) > 2002:
                return False
            if len(d['iyr']) != 4 or int(d['iyr']) < 2010 or int(d['iyr']) > 2020: 
                return False
            if len(d['eyr']) != 4 or int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
                return False
            if re.search(r"^\d{1,3}[a-z]{2}", d['hgt'], flags=0) == None or d['hgt'][-2::] not in ['cm', 'in']:
                return False
            if d['hgt'][-2::] == 'cm':
                if len(d['hgt']) != 5 or int(d['hgt'][:3:]) > 193 or int(d['hgt'][:3:]) < 150:
                    return False
            if d['hgt'][-2::] == 'in':
                if len(d['hgt']) != 4 or int(d['hgt'][:2:]) > 76 or int(d['hgt'][:2:]) < 59:
                    return False
            if re.match(r"#[0-9a-f]{6}", d['hcl'], 0) == None:
                return False
            if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
            if re.match(r"^\d{9}$", d['pid'], 0) == None:
                return False
            return True
        else:
            return False

    with open(filepath) as f:        
        for line in f:
            if line == "\n":
                valid += validate(pp)
                pp = []
                continue
            pp.extend(line.split())        
        valid += validate(pp) # for last passport
    return valid

if __name__ == "__main__":
    print(checkvalid_2('aoc_input.txt'))
