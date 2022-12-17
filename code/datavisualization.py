
import pandas as pd
import numpy as np
df=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\Top_100_selling_TV.csv", sep=',')



from matplotlib import pyplot as plt

#Top 100 selling Tvs by brand
df_grpby_brand=df['Product_Brand'].value_counts()
df_grp_brand = pd.DataFrame(df_grpby_brand).reset_index()
df_grp_brand.columns.values[0] = 'Brand'
df_grp_brand.columns.values[1] = 'num_of_Tv'
brand=[]
no_of_prod=[]
brand.extend(df_grp_brand['Brand'].tolist())
no_of_prod.extend(df_grp_brand['num_of_Tv'].tolist())
plt.barh(brand,no_of_prod)
plt.tight_layout()
plt.title("Top 100 selling Tvs by brand")
plt.ylabel('Product_Brand')
plt.xlabel('Number of products')

plt.xticks(np.arange(0, max(no_of_prod) + 2, 3.0))
plt.show()

#pie chart
plt.pie(no_of_prod,labels = brand)
plt.show()

#screensize 
size_list=[]
size_list.extend(df['Product_Screensize'].tolist())
#print(df['Product_Screensize'].max)
print(min(size_list))
bins=[20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0]
plt.hist(size_list,bins=bins,edgecolor='black')
plt.tight_layout()
plt.title("Number of Tvs by Screen Size")
plt.xlabel('Screen Size in Inches')
plt.ylabel('Number of products')
plt.show()


#Price
price_list=df['product_Price']
print(min(price_list))
plt.hist(price_list,edgecolor='black')
plt.xticks(np.arange(0,max(price_list),100))
plt.yticks(np.arange(0,70,5))
plt.title("Number of Tvs by price")
plt.xlabel('price in USD')
plt.ylabel('Number of products')
plt.show()


#Resolution
df_grpby_resolution=df['Product_Resolution'].value_counts()
print(df_grpby_resolution)
df_grp_res = pd.DataFrame(df_grpby_resolution).reset_index()
df_grp_res.columns.values[0] = 'Resolution'
df_grp_res.columns.values[1] = 'num_of_Tv'
Resolution=[]
no_of_prod=[]
Resolution.extend(df_grp_res['Resolution'].tolist())
no_of_prod.extend(df_grp_res['num_of_Tv'].tolist())
plt.bar(Resolution,no_of_prod)
plt.tight_layout()
plt.title("Top 100 selling Tvs by brand")
plt.xlabel('Resolution')
plt.ylabel('Number of products')

plt.yticks(np.arange(0, max(no_of_prod) + 2, 3.0))
plt.show()