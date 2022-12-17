import pandas as pd
Top_selling=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\Top_100_selling_TV.csv", sep=',')
rev=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\reviews_total.csv", sep=',')
TV_Reviews=pd.merge(Top_selling,rev,on="Product_ID")
print(TV_Reviews)

TV_Reviews.to_csv(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\TV_Reviews.csv",sep=',',index=None)