import googletrans 
from textblob import TextBlob

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

for i,j in language.items():
    print('key :',i,'value :',j)
text1=input('Enter the words  :')
text2=input('Choose change language :')
for i,j in language.items():
    #print('key :',i,'value :',j)
    
    if text2==j:
        text1=TextBlob(text1)
        text1=text1.translate(to=i)
        print(text1)
    
#blob1 = TextBlob("Buongiorno!")
#print(blob1.translate(to='kn'))