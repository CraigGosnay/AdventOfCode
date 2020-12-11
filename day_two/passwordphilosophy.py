from collections import defaultdict

def parse_input(filepath: str) -> list:

    with open(filepath) as f:
        passwords = f.read().splitlines()

    r = []
    for p in passwords:
        s = p.split(':')
        s0 = s[0].split(' ')
        s1 = s0[0].split('-')
        lo = int(s1[0])
        hi = int(s1[1])
        ltr = s0[1]
        pwd = s[1].strip()
        r.append((lo, hi, ltr, pwd))
   # consider namedtuple
   # consider doing this live
    return r

def getvalidpwdcount(pwds: list) -> int:
    
    count = 0
    for i in pwds:
        lo = i[0]
        hi = i[1]
        ltr = i[2]
        pwd = i[3]

        d = defaultdict(int)

        for l in pwd:
            d[l] += 1

        if d[ltr] >= lo and d[ltr] <= hi:
               count += 1

    return count

def getvalidpwdcount_2(pwds: list) -> int:

    count = 0 
    for i in pwds:
        first = i[0] -1
        second = i[1] -1
        ltr = i[2]
        pwd = i[3]

        if pwd[first] == ltr and pwd[second] != ltr:
            count += 1
        elif pwd[first] != ltr and pwd[second] == ltr:
            count += 1
    
    return count

if __name__ == "__main__":
    print(getvalidpwdcount(parse_input('aoc_input.txt')))
    print(getvalidpwdcount_2(parse_input('aoc_input.txt')))