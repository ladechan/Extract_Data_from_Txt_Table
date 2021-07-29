import pandas as pd

df = pd.read_csv('M:\Lavanya\T3\input.txt', delimiter = "|")
header = "|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active"

datas = df.to_numpy()
ind = list()
datas = datas[:,1:]

for rows in datas:
    for items in rows:
        if (items == "IND"):
            ind.append(rows)

def ind_table(ind):
    df = pd.DataFrame(ind)
    df.to_csv('Table_India.csv', index=False, header = head)
    
def get_info(row):
    return row.split('|')[1:]

def datatocsv(df):
    df.to_csv('data.csv', index=False)


df = pd.DataFrame(datas)
datatocsv(df)
head = get_info(header)
ind_table(ind)
print("Completed")