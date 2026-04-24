# NLTK-Text-Processing
The objective of this assignment is to first pre-process 3 text files using tokenize, stemming, and lemmatization, then follow up by checking the n-grams of the 3 text file with the new 4th text file to see if I could identify a potential connection between the first 3 files.


## Puropse
Main focus on handling NLTK Text Processing seeing how tokenize, stemming, lemmatization, and n-gram. Using such functions to evalulate text processing.

This project's aim was to focus on “NLTK” to process text files.
The project reads 4 diffrent text files (RJ_Lovecraft, RJ_Tolkein, RJ_Martin, and Martin) that was given by instructor from unknow source for the project.
The goal is to process the text via the 4 methods, then determine if text file 4 has any potential connection with the other 3 files being written by the same author.
  
Key analyses include:

- Tokenize, stemmed, and lemmated each 3 text files in their own individual sections. 
- Remove stop-words along with puncuation after each text files.
- Before N-gram'ing the 4th performed the same functions as the 3 files before hand.
- Through process noting potential connections to what the text were eluding to and brief summary in reguards to the final noting of potential connection that text 4 (Martin) has with the prior 3.
  
## Class Design
The project main areas are the processing text section when 3 of the 4 files are ran through the functions (token. stem, lemmate, and stopword removal), N-gram analysis that also contains the 4th text files run like the past 3 before n-gram, and ending off with a summary analysis of the potential connection file 4 might have:

For each part for processing the 3 files and later file 4 (First files used were loaded in and files open prior to processing).
- Tokenized the text into sentence, then tokenized words.
- Stemming the prior tokenized file.
- Taking stemmed text through lemmatization.
- Removed stop words, and puncuation noise.
- Generating the 20 most common tokens from each file.

  N-gram section
  - Generated n-gram on the 4 files (after the 4 text is processed does it get n-gramed).

- Then reviewing project:
- Brief conclusion as to the potential connecting text 4 has with one or more of the other text files.

## Class Attributes and Methods

### Processing: 
**Attributes:**
- nltk – Library imports for natural language processing (imported individually).
* Following after library for each text files.
- RJ_Lovecraft.txt, RJ_Tolkein.txt, RJ_Martin.txt – Input text files for the initial reference data.
- stop_words – Set of common words and punctuation filtered out after processing.
- tokens – List of individual words and sentences derived from the raw text.
  
**Methods:**
- nltk.sent_tokenize() – Splits the raw text into a list of sentences.
- nltk.word_tokenize() – Breaks sentences down into individual word units.
- stemmer.stem() – Reduces words to their root form (Stemming).
- wordnet.lemmatizer() – Maps words back to their dictionary base (Lemmatization).
- .most_common(20) – Identifies the top 20 most frequent tokens per file.


---

### N-gram: 

**Attributes:**
- lovecraft_trigrams, tolkein_trigrams, RJmartin_trigrams, and martian2_trigrams – The 4th text file used for the connection test.
- Counter(fileName_trigrams).most_common(20) – Sequences of contiguous words generated for pattern matching.

**Methods:**
- nltk.ngrams() – Generates n-gram sequences from the processed tokens.
- Analysis conclusion of potential file connections.
  
---

## Limitations
- I limited myself to what I learn in a class related to the project, using only NLTK functions.
- Due to minimal experience in usage designs while modified could uses more enhancments when more experience is accumulated.
- Should move function section .txt file 4 with others 3 files (placement following instructions provide to guide through the goals).
  
- Focused mainly on how to uses the NLTK functions for word processing, and understand what each on does to the .txt file. 

## Post Implementation/Conclusions
These are some of the implementation/Thoughts post methods to highlight the areas that I improved and/or discussed upon the initial methods (Following are notes on each plot for part 1, and the paragragh for the loans section in one place):

### Text files review:

#### Text 1 (RJ_Lovecraft)-
- The following shows Concepts of love, fate, and the classic names of Romeo/Juliet. WIth others following along theses main lines/concepts.
- Text appears to be about Romeo and Juliet, as for it being the original story is to be determine. Could be a review of it or even a revised story telling of it.

#### Text 2 (RJ_Tolkein)-
- Similar theme as the last, with Romeo/Juliet, but this instead shows feelings of sad/depressing (Could signify a similar connection of text with Text 1).
- Should see if their is another method in which to determine the origin of the texts if either they are the same story or not. 
- Additional context could be found in the files original names but should not be a leading factor.

#### Text 3 (RJ_Martin)-
- This text file is showing similar concepts once more but instead shows an empthsis with secrets, garden, feud, and addtional names being mention slightly more than prior.
- If it is about Romeo/Juliet this appears to be talking more towards the twist and turns that appear within the story.
- With the mention of more names suggest involvement with it.
- Once more further evaluation reguarding text origin should be looked into.

#### Text 4 (Martin)/Summary of connection-
- It appears that the file does not show exact connections with the first 3 text files.
- Its text appears to contain words that are not exactly connected.
- Some do appear like some connection with words with text file 1 ('whisper','realm', and 'ancient'), with text file 2 & 3 having a few similar words.
- From what was compiled it appears that text 1 (), and text 4 () share a common n-gram of words that could suggest that it is connected to the same auther, while not the same context as it appears to be entirly diffrent than one another with text 1 concepts leaning towards romeo/juliet story and this in line with a potential medival/fantasy potential line instead.
