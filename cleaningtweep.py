import re     #This is used for removing URLs, mentions, hashtags, and other unwanted texts
import nltk   #This is a library used for working with human language
from nltk.corpus import stopwords   #This helps to remove unnecessary words (e.g "the" , "is", "and")
from nltk.tokenize import word_tokenize  #This is for breaking sentences into words
from nltk.stem import WordNetLemmatizer   #This is for taking words back into their baseforms (running will turn to run)

nltk.download ("stopwords") #This downloads a list of common words to remove
nltk.download("punkt")    #This downloads data needed for splitting texts/sentences into words
nltk.download('punkt_tab')  #This is a newer version of NLTK tokenization, the above line line "punkt" version is not sufficient anymore
nltk.download ("wordnet")   #This downloads data for taking words back into their baseforms


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def cleaning_tweet (text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE) #This is a reguarl expression that finds URLs, the "" means replace the pattern with empty string
    text = re.sub(r"@\w+|#", "", text) #This removes the mention and hashtags
    text = re.sub(r"\d+", "", text)    #This removes numbers
    text = re.sub(r"[^\w\s]", "", text) #This removes punctuations
    text = text.lower()                   #This converts texts to lowercase
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word)for word in tokens if word not in stop_words] #Lemmatize and remove stopwords
    return " ".join(tokens)

Example = "Wow!!! AI is amazing, isn't it? Check this out: https://example.com @Waji #MachineLearning"
cleaned_example = cleaning_tweet(Example)
print(cleaned_example)
    