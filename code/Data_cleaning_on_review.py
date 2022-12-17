import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
reviews_df=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\TV_Reviews.csv", sep=',')

# Removing rows which does not have reviews
reviews_df=reviews_df[reviews_df['body'].notna()]
#reviews_df=reviews_df.reset_index(drop=True)
print(reviews_df)

#converting to lower case
reviews_df['body'] = reviews_df['body'].apply(lambda x: " ".join(x.lower() for x in x.split()))

#deleting stop words in body column
stop_words_eng=stopwords.words('english') +['im']+['fire']
reviews_df['body'] = reviews_df['body'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words_eng))

#remove punctuations
rem_pun = '[^\w\s]'
reviews_df['body'] = reviews_df['body'].str.replace(rem_pun,'')

#removing numbers from body column
num_pat = '\\b[0-9]+\\b'
reviews_df['body'] = reviews_df['body'].str.replace(num_pat,'')


#rmoving rows with Non english words in body column
reviews_df=reviews_df[reviews_df.body.map(lambda a: a.isascii())]


reviews_df.to_csv(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\TV_Reviews.csv",sep=',',index=None)

