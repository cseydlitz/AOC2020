import pandas as pd
import pprint
import re

in_data = 'in_data.csv'

valid_dict = {}

def part_one(in_list):

    comp_list = []
    valid = 0
    for l in in_list:
        is_valid = False
        if isinstance(l,float):
            if len(comp_list) == 8:
                is_valid = True
            elif not [i for i in comp_list if "cid" in i] and len(comp_list) == 7:
                is_valid = True

            if is_valid:
                valid+=1
                valid_dict[valid] = {}
                for i in comp_list:
                    kv = i.split(':')
                    valid_dict[valid][kv[0]] = kv[1]
            comp_list.clear()
        else:
            comp_list.extend(l.split(' '))
    return valid


def part_two():
     
    eye_clr = ['amb','blu','brn','gry','grn','hzl','oth']
    pattern = re.compile("[a-z0-9]+")
    valid = 0

    for k,v in valid_dict.items():
        if 1920 <= int(v['byr']) <= 2002:
            if 2010 <= int(v['iyr']) <= 2020:
                if 2020 <= int(v['eyr']) <= 2030:
                    if len(v['pid']) == 9:
                        if v['ecl'] in eye_clr:
                            if v['hcl'][0] == "#" and len(v['hcl']) == 7 and pattern.fullmatch(v['hcl'][1:]) is not None:
                                try:
                                    if "cm" in v['hgt'] and 150 <= int(v['hgt'][0:3]) <= 193:
                                        valid+=1
                                    elif "in" in v['hgt'] and 59 <= int(v['hgt'][0:2]) <= 76:
                                        valid+=1
                                except ValueError:
                                    pass
    return valid

def main():
    df = pd.read_csv(in_data, header=None, skip_blank_lines=False)
    input_dict = df.to_dict(orient='list')

    p1 = part_one(input_dict[0])
    p2 = part_two()

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()
