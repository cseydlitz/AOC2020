import pandas as pd

in_data = 'in_data.csv'

def main(rise,run):
    df = pd.read_csv(in_data, header=None)
    input_dict = df.to_dict(orient='index')

    tree = 0
    indx = run
    skipRow = True
    for k,v in input_dict.items():
        if skipRow: 
            skipRow = False
        else:
            if k%rise == 0:
                row = list(v[0])
                if indx > (len(row)-1):
                    indx = indx - (len(row))
                if row[indx] == "#":
                    tree+=1
                indx+=run

    return tree

if __name__ == '__main__':
   r1 = main(1,3)
   r2 = main(1,1)
   r3 = main(1,5)
   r4 = main(1,7)
   r5 = main(2,1)

   print(r1*r2*r3*r4*r5)

