import pprint
import pandas as pd

in_data = 'input_data.csv'

def part_one(input_dict):
    tot_valid = 0

    for k,v in input_dict.items():
        validation_letter = v[1][0]
        pw = v[2]
        raw_range = v[0].split('-')
        char_min = int(raw_range[0])
        char_max = int(raw_range[1])

        tot_char = pw.count(validation_letter)
        if char_min <= tot_char <= char_max:
            tot_valid+=1
    return tot_valid

def part_two(input_dict):
    tot_valid = 0

    for k,v in input_dict.items():
        validation_letter = v[1][0]
        pw = v[2]
        raw_index = v[0].split('-')
        index1 = int(raw_index[0]) - 1
        index2 = int(raw_index[1]) - 1

        if (pw[index1] == validation_letter) is not (pw[index2] == validation_letter):
            tot_valid+=1
    return tot_valid

def main():
    df = pd.read_csv('input_data.csv',header=None, delim_whitespace=True)
    input_dict = df.to_dict(orient='index')
    
    part_one_valid = part_one(input_dict)
    part_two_valid = part_two(input_dict)

    print(part_one_valid)
    print(part_two_valid)

if __name__ == '__main__':
    main()
