import wordcloud
from matplotlib import pyplot as plt

f = open('textcontent.txt', 'r')
file_contents = f.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words we can use to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "in", "for", "I", "not", "they",
                           "been", "being", "have", "has", "had", "do", "does",
                           "did", "but",
                           "at", "by", "with", "on", "thy",
                           "from", "here", "when", "thou",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor",
                           "too", "very",
                           "can", "will", "just"]

    frequencies = {}

    # remove punctuation
    for letter in file_contents:
        if letter in punctuations:
            file_contents = file_contents.replace(letter, "")

    # split words
    file_words = file_contents.split(' ')
    for word in file_words:
        if word.lower() not in uninteresting_words:
            if word.lower() not in frequencies:
                frequencies[word.lower()] = 0
            frequencies[word.lower()] += 1

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
