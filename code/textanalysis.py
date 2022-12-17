import seaborn as sns
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from matplotlib import pyplot as plt
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
from textblob import TextBlob
from nltk.corpus import stopwords
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import wordcloud as wc


df=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\TV_Reviews.csv", sep=',')


vect = CountVectorizer(max_df=0.8, min_df=4, stop_words='english')
doc_mat = vect.fit_transform(df['body'].values.astype('U'))


Latent_Alloc = LatentDirichletAllocation(n_components=3, random_state=15)
Latent_Alloc.fit(doc_mat)


for i,topic in enumerate(Latent_Alloc.components_):
     print(f'Top 10 words for topic #{i}:')
     print([vect.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
     cloud=[vect.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
     zerocloud=wc.WordCloud(max_words=50,background_color='black',contour_color='black').generate(' '.join(cloud))
     plt.imshow(zerocloud,interpolation='bilinear')
     plt.axis("off")
     plt.show()
     print('\n')

top_val = Latent_Alloc.transform(doc_mat)
top_val.shape
# Adding topic number  column to df
df['topic#'] = top_val.argmax(axis=1)


df['topic#'].value_counts().plot(kind="bar")
plt.title("number of records per topic")
plt.xlabel("Topic #")
plt.ylabel("Number of records")

# plotting the frequency of topic1
plt.show()






reviews=df['body'].values.tolist()
pos_words=[]
neg_words=[]
fear_list=[]
trust_list=[]
joy_list=[]
sadness_list=[]
from nrclex import NRCLex
trust_fq=[]
fear_fq=[]
joy_fq=[]
sadness_fq=[]
positive_fq=[]
negative_fq=[]

for i in range(len(reviews)):
    emotion = NRCLex(reviews[i])
    trust_list.append(emotion.affect_frequencies['trust'])
    fear_list.append(emotion.affect_frequencies['fear'])
    joy_list.append(emotion.affect_frequencies['joy'])
    sadness_list.append(emotion.affect_frequencies['sadness'])
    pos_words.append(emotion.affect_frequencies['positive'])
    neg_words.append(emotion.affect_frequencies['negative'])


for i in range(len(reviews)):
    wordlist=reviews[i].split()
    for word in wordlist:
        word_emotion=NRCLex(word)
        trust_value=word_emotion.affect_frequencies['trust']
        fear_value=word_emotion.affect_frequencies['fear']
        
        joy_value=word_emotion.affect_frequencies['joy']
        sadness_value=word_emotion.affect_frequencies['sadness']
        positive_value=word_emotion.affect_frequencies['positive']
        negative_value=word_emotion.affect_frequencies['negative']
       
        #joy sadness
        if joy_value > 0:
            joy_fq.append(word)
        if sadness_value > 0:
            sadness_fq.append(word)
        #trust fear
        if trust_value>0:
            trust_fq.append(word)
        if fear_value >0:
            fear_fq.append(word)

        #pos neg
        if positive_value > 0:
            positive_fq.append(word)
        if negative_value > 0:
            negative_fq.append(word)
fear_df=pd.DataFrame()
fear_df['fear']=fear_fq
fear_df['fear'].value_counts().head(10).plot(kind="bar")
plt.show()



#WordCloud

fearcloud=wc.WordCloud(max_words=50,background_color='black',contour_color='black').generate(' '.join(fear_fq))
plt.imshow(fearcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

trustcloud=wc.WordCloud(max_words=50,background_color='black',contour_color='black').generate(' '.join(trust_fq))
plt.imshow(trustcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

positivecloud=wc.WordCloud(max_words=50,background_color='black',contour_color='black',collocations=False).generate(' '.join(positive_fq))
plt.imshow(positivecloud,interpolation='bilinear')
plt.axis("off")
plt.show()

Negtivecloud=wc.WordCloud(max_words=50,background_color='black',contour_color='black',collocations=False).generate(' '.join(negative_fq))
plt.imshow(Negtivecloud,interpolation='bilinear')
plt.axis("off")
plt.show()


