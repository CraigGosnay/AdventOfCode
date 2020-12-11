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

if __name__ == "__main__":
    print(checkvalid('aoc_input.txt'))
