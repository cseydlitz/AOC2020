import pandas as pd
import pprint

in_data = 'in_data.csv'

def main():
    df = pd.read_csv(in_data, header=None, skip_blank_lines=False)
    input_dict = df.to_dict(orient='list')
    in_list = input_dict[0]

    comp_list = []
    valid = 0
    for l in in_list:
        if isinstance(l,float):
            if len(comp_list) == 8:
                valid+=1
            elif not [i for i in comp_list if "cid" in i] and len(comp_list) == 7:
                valid+=1
            comp_list.clear()
        else:
            comp_list.extend(l.split(' '))

    print(valid)

if __name__ == '__main__':
    main()
