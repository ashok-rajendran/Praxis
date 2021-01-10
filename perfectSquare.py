from math import ceil, sqrt
import pandas as pd

pd.options.display.max_colwidth = 100
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.DataFrame()

def perfectSquares(l, r, df):
    number = ceil(sqrt(l))
    n2 = number * number
    number = (number * 2) + 1
    while ((n2 >= l and n2 <= r)):
        sqnm = ceil(sqrt(n2))
        #print(n2)
        new_row = {'A' : str(n2)}
        df = df.append({'A' : str(n2)}, ignore_index=True)
        n2 = n2 + number
        number += 2
    df2 = df.groupby(df.index // 10).agg(','.join)
    col_names = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
    sqValues = pd.DataFrame(columns=col_names)
    sqValues = sqValues.fillna(0)
    sqValues = df2["A"].str.split(pat=",", expand=True)
    sqValues.rename(columns={0:'One',1:'Two',2:'Three',3:'Four',4:'Five',5:'Six',6:'Seven',7:'Eight',8:'Nine',9:'Ten'},inplace=True)
    print(sqValues)

if __name__ == "__main__":
    l = 1
    r = 40000
    perfectSquares(l, r, df)

