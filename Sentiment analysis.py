import nltk
from nltk.corpus import stopwords
from nltk.corpus import words as corpus
import json
from collections import Counter as count
import csv



#IMPORTANT
#------------------------------------------
#Download nltk if not downloaded.
#Uncomment line 15 and run program.
#This will open up a GUI window, hit download button. If not downloaded error will occur.
#nltk.download()
#Make sure to comment line 15 when running after downloaded


#Things to note before running program
#Program will take a ridiculous amount of time to run 
#Takes me aprrox. 17 minutes(I timed it) running 16gb of memory 
#-------------------------------------------


#Part 1
#Load the JSON data from the file using JSON reader
with open("yelp_academic_dataset_review_small.json") as dataset:
    data = json.load(dataset)

dump = json.dumps(data)  #converts to string
load = json.loads(dump)#[:999]  #converts to dictionary

#Store data of stars into 5 counts for each star
#Uses counter library 
stars_1 = count() 
stars_2 = count()
stars_3 = count()
stars_4 = count()
stars_5 = count()

#Part 2
#Extract all review texts and star ratings.
#Lemmatize the words.
#Filter out stop words and words that are not in the words corpus.
wordcorpus = set(corpus.words("en"))     #Create a set for wordcorpus
stopwords = set(stopwords.words("english"))  #Create a set for stopwords
lemmatizer = nltk.WordNetLemmatizer()        #Setup NLTK wordnet lemmatizer

for read in load:
    text =  read.get("text")  #gets text from file
    stars = read.get("stars") #gets stars from file
    words = nltk.word_tokenize(text)  #splits text into substrings
    words = [words_.lower() for words_ in words]  #makes words lowercase
    words = [lemmatizer.lemmatize(words_) for words_ in words if words_ not in stopwords and words_.isalnum()] 
    #^ lemmatize if in word corpus 
    if(stars == 1):
        stars_1 += count(words)
    elif(stars == 2):
        stars_2 += count(words)
    elif(stars == 3):
        stars_3 += count(words)
    elif(stars == 4):
        stars_4 += count(words)
    else:
        stars_5 += count(words)

#Sum of all counts
starsall = stars_1 + stars_2 + stars_3 + stars_4 + stars_5   #sets up calculation used later

#create sets for each star rating
a = set(stars_1)
b = set(stars_2)
c = set(stars_3)
d = set(stars_4)
e = set(stars_5)

#create a list of all stars
list_of_stars = list(starsall)

#Part 3
#If a lemma is used in fewer than 10 reviews, discard it.
for lemma in list_of_stars:   
    if(lemma not in wordcorpus or starsall[lemma] < 10):  #deletes lemma if not in corpus or < 10 reviews
        del starsall[lemma]
        if(lemma in a): #delete each lemma for star rating of 1
            del stars_1[lemma]
        if(lemma in b): #delete each lemma for star rating of 2
            del stars_2[lemma]
        if(lemma in c): #delete each lemma for star rating of 3
            del stars_3[lemma]
        if(lemma in d): #delete each lemma for star rating of 4
            del stars_4[lemma]
        if(lemma in e): #delete each lemma for star rating of 5
            del stars_5[lemma]



#For each lemma, calculate its average star rating.
for lemma in stars_2:
    stars_2[lemma] = stars_2.get(lemma)* 2 #multiply lemma star rating of 2 by 2 for average
for lemma in stars_3:
    stars_3[lemma] = stars_3.get(lemma)* 3 #multiply lemma star rating of 3 by 3 for average 
for lemma in stars_4:
    stars_4[lemma] = stars_4.get(lemma)* 4 #multiply lemma star rating of 4 by 4 for average
for lemma in stars_5:
    stars_5[lemma] = stars_5.get(lemma)* 5 #multiply lemma star rating of 5 by 5 for average

starsadd = stars_1 + stars_2 + stars_3 + stars_4 + stars_5 #add all star ratings in order to divide

for lemma in starsall:
    starsall[lemma] = float(starsadd[lemma] / starsall[lemma]) #divide added stars by star counts

#Store data in columns in order to csv write to each
column1 = []  
column2 = []

#Part 4
#Save the 500 most negative lemmas and 500 most positive lemmas
#and their respective sentiment levels in a one two-column CSV file
#sorted in the descending order of sentiment levels.
column1 += starsall.most_common()[:499] 
column2 += starsall.most_common()[:499]

column1 += starsall.most_common()[:-499-1:-1] 
column2 += starsall.most_common()[:-499-1:-1] 


lemmas = [x[0] for x in column1] #split lemmas from tuple
#print(lemmas)

levels = [x[1] for x in column2] #split levels from tuple
#print(levels)

#For the first 500 rows the most positive lemmas with their levels will append in descending order
#For the last 500 the most negative lemmas with their levels will append to the rows in ascending at first
#Instead of going from 1 onward we want descending order(reversed)
#Manupulation is needed 
#Flip the order of the last 500 lemmas(negatives)
#At row 501 there will be a significantly smaller value in order to start the most negative lemmas
sorted_levels = levels
sorted_levels.sort(reverse = True)


#zip data
zippy = zip(lemmas, sorted_levels)

with open("Sentiment analysis Team golf.csv", "w", newline="") as csvf:
    writer = csv.writer(csvf, delimiter=',')
    write = writer.writerow(["500 most positive/negative lemmas", "Sentiment levels"])
    writer = writer.writerows(zippy)


#sources
#https://towardsdatascience.com/text-preprocessing-with-nltk-9de5de891658
#https://realpython.com/python-nltk-sentiment-analysis/
#https://youtu.be/U8m5ug9Q54M-Python NLTK Tutorial | Sentiment Analysis Using NLTK | Python Training | Edureka