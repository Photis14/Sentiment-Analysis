# Sentiment-Analysis

This program calculates the sentiment level of words based on user reviews from the Yelp academic dataset. Unlike standard sentiment analyzers, this program does not use VADER or any other pre-existing tool.

# Dataset
The program uses a dataset of Yelp reviews written by members, with a total of 156,602 reviews. Each review includes a text fragment and a star rating on a scale from 1 (worst) to 5 (best). The sentiment level of a word is determined by the average star rating of all reviews where the word is used.

# Processing Steps

The program loads the JSON data from the file and selects a small subset for practicing. The final run of the program includes all reviews. A JSON reader is used.
The program extracts all review texts and star ratings.
Each review is broken into individual words using the Natural Language Toolkit (NLTK).
The program lemmatizes the words.
Stop words and words that are not in the words corpus are filtered out.
For each lemma, the program calculates its average star rating. If a lemma is used in fewer than 10 reviews, it is discarded.
The 500 most negative and 500 most positive lemmas and their respective sentiment levels are saved in a two-column CSV file, sorted in descending order of sentiment levels.
The program uses a CSV writer to save the file.
Usage
To run the program, simply download the provided source code and run the main Python file. The program will automatically load the Yelp dataset, process it, and output a CSV file with the most negative and positive lemmas.

# Requirements
The program only uses core Python modules and NLTK. No other external libraries, such as pandas or numpy, are used.
Link to download json file(too large for github): https://www.dropbox.com/s/at6ltakpiictakf/yelp_academic_dataset_review_small.json?dl=0
