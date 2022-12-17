#rating column
rating=[]
new_rating=[]
import pandas as pd
df=pd.read_table(r"C:\Users\svajjal\OneDrive\project deliverable 1\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv", sep=',')
rating.extend(df['product_Rating'].tolist())

print(len(rating))

for a in rating:
    a=str(a)
    new_rating.append(float(a[0:3]))
print(len(new_rating))
df['product_Rating']=pd.Series(new_rating)
print(df)
"""
#rating for review
rev_rating=[]
new_rev_rating=[]
rev_rating.extend(df['rating_for_review'].tolist())
print(len(rev_rating))
for a in rev_rating:
    if(a!=None):
        new_rating.append(str(a[0:3]))
    else:
        new_rating.append(a)
print(len(new_rev_rating))
df['rating_for_review']=pd.Series(new_rev_rating)
"""
#removing $
price=[]
new_price=[]
price.extend(df['product_Price'].tolist())
print(len(price))
for a in price:
    if(len(str(a))>1):
        rem=str(a).replace('$','')
        if(rem.find(',')):
            rem=rem.replace(',','')
        print(rem)
        new_price.append(float(rem))

    else:
        new_price.append(a)
print(len(new_price))
df['product_Price']=pd.Series(new_price)

#removing inches
inches=[]
new_inches=[]
inches.extend(df['Product_Screensize'].tolist())
for a in inches:
    if(len(str(a))>1):
        new_inches.append(str(a).rstrip(' Inches'))
    else:
        new_inches.append(a)
df['Product_Screensize']=pd.Series(new_inches)
df.to_csv(r"C:\Users\svajjal\OneDrive\project deliverable 1\project-deliverable-1-cowboys\data\Top_100_selling_TV.csv",sep=',',index=None)


