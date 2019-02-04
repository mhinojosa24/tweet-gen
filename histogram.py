
'''
- What is the least/most frequent word(s)?
- How many different  awords used?
- What is the average (mean/median/mode) frequency of words in the text?


<--- FUNCTIONS --->

histogram()
    - takes a 'source_text' argument and return a histogram data structure that stores each unique word.

unique_words()
    - takes a histogram argument and returns the total count of unique words in the histogram.

frequency()
    - takes a word and histogram argument and returns the number of times that word appears in a text.
'''

import sys

text = "one fish two fish red fish blue fish"
file = "text_file.txt"

def histogram(source_text):
    '''
    # return stored data structured of each unique words
    dictionary = dict()
    with open('{}'.format(source_text), 'r') as f:
        text_file = f.read()
        text = text_file.split()

    '''
    text = source_text.split(' ')
    list_of_list = []
    sum_list = []

    for word in text:
        found = False
        for w in sum_list:
            if w[0] == word:
                found = True
                w[1] = w[1] + 1
                break
        if not found:
            sum_list.append([word, 1])


    print(sum_list)



def unique_words(histogram):

    values = histogram.values()
    sum = 0

    for value in values:
        sum += value

    print(sum)


def frequency(word, histogram):

    if word in histogram:
        appearance = histogram.get('{}'.format(word))
        print("{}: {}".format(word, appearance))
    else:
        print("Not Found")


def main():
    histo = histogram(text)
    # unique_words(histo)
    # word = sys.argv[1]
    # frequency(word, histo)


if __name__ == "__main__":
    main()
