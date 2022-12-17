from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import nltk
nltk.download('vader_lexicon')

df=pd.read_table(r"C:\Users\svajjal\Documents\GitHub\project-deliverable-2-cowboys\data\TV_Reviews.csv", sep=',')



portstem = PorterStemmer()
df['stem_review'] = df['body'].apply(lambda a: " ".join([portstem.stem(text) for text in a.split()]))
print(df)
review_stemmed=df['stem_review'].values.tolist()


neg=[]
pos=[]
neu=[]
cmpd=[]
polarity=[]
analyzer = SentimentIntensityAnalyzer()
for rev in review_stemmed:
    vs = analyzer.polarity_scores(rev)
    neg.append(vs['neg'])
    pos.append(vs['pos'])
    neu.append(vs['neu'])
    cmpd.append(vs['compound'])
    if(vs['compound']>=0.05):
        polarity.append('positive')
    elif(vs['compound']<=-0.05):
        polarity.append('negative')
    else:
        polarity.append('neutral')



sent_df=pd.DataFrame()
sent_df['Review_stemmed']=review_stemmed
sent_df['neg']=neg
sent_df['pos']=pos
sent_df['neu']=neu
sent_df['compound']=cmpd
sent_df['polarity']=polarity
print(sent_df)

sent_df['polarity'].value_counts().plot(kind='bar')
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.title(" Review distribution based on sentiment")
plt.show()

from sklearn.metrics import ConfusionMatrixDisplay
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


reviews_fts = sent_df['Review_stemmed']
stop_words_eng=stopwords.words('english')
Tfidf_vect = TfidfVectorizer(max_features=2500, min_df=7, max_df=0.8, 
stop_words=stop_words_eng)
Reviews_transform_fts = Tfidf_vect.fit_transform(reviews_fts).toarray()
labels = sent_df['polarity']
train_x,test_x, train_y, test_y = train_test_split(Reviews_transform_fts, 
labels, test_size=0.25, random_state=0)
rand_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
rand_classifier.fit(train_x, train_y)
predictions = rand_classifier.predict(test_x)
con_matrix = confusion_matrix(test_y,predictions)
print(con_matrix)
ConfusionMatrixDisplay.from_estimator(rand_classifier, test_x, test_y)
plt.show()
print(classification_report(test_y,predictions))