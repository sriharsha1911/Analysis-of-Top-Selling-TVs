
import pandas as pd
df=pd.read_table(r"C:\Users\svajjal\OneDrive\project deliverable 1\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv", sep=',')
df.loc[df['product_Name'].str.contains('Amazon',case=False), 'Product_Brand'] = 'Amazon'
#print(df)


# updating screen size for amazon tv
size=[]
num_row=[]
num_row.extend(df.index[(df['product_Name'].str.contains('Amazon',case=False) )])
#print(num_row)
prod_size=[]
a=df.loc[df['product_Name'].str.contains('Amazon',case=False)]
#print(a)
size.extend(a['product_Name'].tolist())
#print(size)
for element in size:
    spl=element.split(' ')
    
    prod_size.append(spl[3].rstrip('"'))
#print(prod_size)

for elem in num_row:
    i=0
    df.loc[elem, ['Product_Screensize']] = [prod_size[i]]
    i=i+1
print(df)

#removing Goove product which is not a tv
df.drop(df[df.Product_Brand =='Govee'].index, inplace=True)
#Changing rsolution for Amazon tvs
df.loc[df['Product_Brand']=='Amazon', 'Product_Resolution'] = '4K'
## Dropping Non TV products
df=df.drop(38)
df=df.drop(60)
print(df)

df.to_csv(r"C:\Users\svajjal\OneDrive\project deliverable 1\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv",sep=',',index=None)

