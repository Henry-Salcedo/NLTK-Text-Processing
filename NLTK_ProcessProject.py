# %% [markdown]
# # NLTK Text Processing

# %% [markdown]
# # Goal:
# 
# The purpose of this project is to uses natural language processing that was studies to perform a comparative analysis on 3 diffrent text files.
# 
# By first performing tokenization stemming, and lemmatization on all 3 for the 20 most common tokens in each text, then determine the subject of the texts.
# 
# After, uses the same 3 text and perform n-gram analysis that = '3', for each file and the new Text_4 file, and lastly determine weather or not one of the authors wrote the 4th text file.

# %% [markdown]
# ## Processing Text files (Tokenize, Stemming, and lemmatization).

# %%
# First import files for the tokenize, stemming, and lemmatization within the NLTK library.
import nltk
from nltk import tokenize 
from nltk import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter


# Open text files: RJ_Lovecraft, 2. RJ_Tolkein, 3. RJ_Martin, 4. Martin
with open('RJ_Lovecraft.txt', 'r') as f:
    lovecraft_text = f.read()
with open('RJ_Tolkein.txt', 'r') as f:
    tolkein_text = f.read()
with open('RJ_Martin.txt', 'r') as f:
    martin_text = f.read()
with open('Martin.txt', 'r') as f:
    martin_text2 = f.read()


# Order of text files: 
# 1. RJ_Lovecraft, 2. RJ_Tolkein, 3. RJ_Martin, 4. Martin |

# %% [markdown]
# #### Text 1: RJ_Lovecraft

# %%
# Tokenize the text files into sentences and words.
lovecraft_sentences = tokenize.sent_tokenize(lovecraft_text)
lovecraft_words = tokenize.word_tokenize(lovecraft_text)

# Then Stemming.
porter_stemmer = PorterStemmer()
lovecraft_stemmed_words = [porter_stemmer.stem(word) for word in lovecraft_words]

# Then Lemmatization.
wordnet_lemmatizer = WordNetLemmatizer()

# %%
# Also remove stop words, and punctuation.
stop_words = set(stopwords.words('english'))
lovecraft_filtered_words = [word for word in lovecraft_stemmed_words if word.lower() not in stop_words and word.isalnum()]


# Followed by the 20 most common toekens in the text file.
lovecraft_freq_dist = FreqDist(lovecraft_filtered_words)
lovecraft_common_tokens = lovecraft_freq_dist.most_common(20)
print("20 most common tokens in Lovecraft's text file:")
for token, frequency in lovecraft_common_tokens:
    print(f"{token}: {frequency}")


# %% [markdown]
# * The following shows Concepts of love, fate, and the classic names of Romeo/Juliet. WIth others following along theses main lines/concepts.
# * Text appears to be about Romeo and Juliet, as for it being the original story is to be determine. Could be a review of it or even a revised story telling of it.

# %% [markdown]
# #### Text 2: RJ_Tolkein

# %%
# Tokenize the RJ_Tolkein text file into sentences and words.
tolkein_sentences = tokenize.sent_tokenize(tolkein_text)
tolkein_words = tokenize.word_tokenize(tolkein_text)

# Then Stemming.
porter_stemmer2 = PorterStemmer()
tolkein_stemmed_words = [porter_stemmer2.stem(word) for word in tolkein_words]

# Then Lemmatization.
wordnet_lemmatizer2 = WordNetLemmatizer()
tolkein_lemmatized_words = [wordnet_lemmatizer2.lemmatize(word) for word in tolkein_stemmed_words]

# %%
# Remove stop words, and punctuation.
tolkein_filtered_words = [word for word in tolkein_lemmatized_words if word.lower() not in stop_words and word.isalnum()]

# Followed by the 20 most common toekens in the text file.
tolkein_freq_dist = FreqDist(tolkein_filtered_words)
tolkein_common_tokens = tolkein_freq_dist.most_common(20)
print("20 most common tokens in Tolkein's text file:")
for token, frequency in tolkein_common_tokens:
    print(f"{token}: {frequency}")

# %% [markdown]
# * Similar theme as the last, with Romeo/Juliet, but this instead shows feelings of sad/depressing (Could signify a similar connection of text with Text 1).
# * Should see if their is another method in which to determine the origin of the texts if either they are the same story or not. 
# * Additional context could be found in the files original names but should not be a leading factor.

# %% [markdown]
# #### Text 3: RJ_Martin

# %%
# Tokenize the text files into sentences and words for RJ_Martin.
RJmartin_sentences = tokenize.sent_tokenize(martin_text)
RJmartin_words = tokenize.word_tokenize(martin_text)

# Then Stemming.
porter_stemmer3 = PorterStemmer()
RJmartin_stemmed_words = [porter_stemmer3.stem(word) for word in RJmartin_words]

# Then Lemmatization.
wordnet_lemmatizer3 = WordNetLemmatizer()
RJmartin_lemmatized_words = [wordnet_lemmatizer3.lemmatize(word) for word in RJmartin_stemmed_words]

# %%
# Remove stop words, and punctuation.
RJM_filtered_words = [word for word in RJmartin_lemmatized_words if word.lower() not in stop_words and word.isalnum()]

# Followed by the 20 most common toekens in the text file.
RJM_freq_dist = FreqDist(RJM_filtered_words)
RJM_common_tokens = RJM_freq_dist.most_common(20)
print("20 most common tokens in Martin's text file:")
for token, frequency in RJM_common_tokens:
    print(f"{token}: {frequency}")

# %% [markdown]
# * This text file is showing similar concepts once more but instead shows an empthsis with secrets, garden, feud, and addtional names being mention slightly more than prior.
# * If it is about Romeo/Juliet this appears to be talking more towards the twist and turns that appear within the story.
# * With the mention of more names suggest involvement with it.
# * Once more further evaluation reguarding text origin should be looked into.

# %% [markdown]
# ## N-gram Analysis

# %% [markdown]
# ### Text 1

# %%
# Perform N-gram analysis on the text files with n = 3.

lovecraft_trigrams = nltk.trigrams(lovecraft_filtered_words)
print("Trigrams in Lovecraft's text file:")
Counter(lovecraft_trigrams).most_common(20)

# %% [markdown]
# ### Text 2

# %%
# Perform N-gram analysis on the text files with n = 3.

tolkein_trigrams = nltk.trigrams(tolkein_filtered_words)
print("Trigrams in Tolkein's text file:")
Counter(tolkein_trigrams).most_common(20)

# %% [markdown]
# ### Text 3

# %%
# Perform N-gram analysis on the text files with n = 3.

RJmartin_trigrams = nltk.trigrams(RJM_filtered_words)
print("Trigrams in Tolkein's text file:")
Counter(RJmartin_trigrams).most_common(20)

# %% [markdown]
# ### Text 4: Martin (Filtering)

# %%
# Tokenize the text files into sentences and words.
martin = tokenize.sent_tokenize(martin_text2)
martin_words = tokenize.word_tokenize(martin_text2)

# Then Stemming.
porter_stemmer4 = PorterStemmer()
martin_stemmed_words = [porter_stemmer4.stem(word) for word in martin_words]

# Then Lemmatization.
wordnet_lemmatizer4 = WordNetLemmatizer()
martin_lemmatized_words = [wordnet_lemmatizer4.lemmatize(word) for word in martin_stemmed_words]

# %%
# Remove stop words, and punctuation.
martian_filtered_words = [word for word in martin_lemmatized_words if word.lower() not in stop_words and word.isalnum()]

# Followed by the 20 most common toekens in the text file.
martian_freq_dist = FreqDist(martian_filtered_words)
martian_common_tokens = martian_freq_dist.most_common(20)
print("20 most common tokens in Martin's text file:")
for token, frequency in martian_common_tokens:
    print(f"{token}: {frequency}")

# %% [markdown]
# ### Text 4

# %%
martin2_trigrams = nltk.trigrams(martian_filtered_words)
print("Trigrams in Tolkein's text file:")
Counter(martin2_trigrams).most_common(20)

# %% [markdown]
# ## Determine if text file 4 has any relation with at least one of the first 3 text files.
# It appears that the file does not show exact connections with the first 3 text files.
# * Its text appears to contain words that are not exactly connected.
# * Some do appear like some connection with words with text file 1 ('whisper','realm', and 'ancient'), with text file 2 & 3 having a few similar words.
# * From what was compiled it appears that text 1 (), and text 4 () share a common n-gram of words that could suggest that it is connected to the same auther, while not the same context as it appears to be entirly diffrent than one another with text 1 concepts leaning towards romeo/juliet story and this in line with a potential medival/fantasy potential line instead.
# 


